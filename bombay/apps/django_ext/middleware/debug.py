from django.db import connection
import re
from operator import add
import sys
import tempfile
from django.conf import settings
import hotshot, hotshot.stats
try:
    from core.log import logger
except ImportError:
    import logging as logger
try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

class SQLMiddleware:
    """
    This middleware logs all db queries through the logger.
    """
    def process_response(self, request, response):
        for query in connection.queries:
            logger.debug(query['sql'])
        return response

# Orignal version taken from http://www.djangosnippets.org/snippets/186/

words_re = re.compile( r'\s+' )

group_prefix_re = [
    re.compile( "^.*/django/[^/]+" ),
    re.compile( "^(.*)/[^/]+$" ), # extract module path
    re.compile( ".*" ),           # catch strange entries
]

class ProfileMiddleware(object):
    """
    Displays hotshot profiling for any view.
    http://yoursite.com/yourview/

    You'll see the profiling results in your log file.

    WARNING: It uses hotshot profiler which is not thread safe.
    """
    def process_request(self, request):
        self.tmpfile = tempfile.mktemp()
        self.prof = hotshot.Profile(self.tmpfile)

    def process_view(self, request, callback, callback_args, callback_kwargs):
        # turn on debugging in db backend to capture time
        debug = settings.DEBUG
        settings.DEBUG = True

        # get number of db queries before we do anything
        n = len(connection.queries)

        value = self.prof.runcall(callback, request, *callback_args, **callback_kwargs)

        # compute the db time for the queries just run
        queries = len(connection.queries) - n
        if queries:
            dbTime = reduce(add, [float(q['time']) for q in db.db.queries[n:]])
        else:
            dbTime = 0.0

        # restore debugging setting again
        settings.DEBUG = debug

        logger.debug("\nDB Profile\nQueries: " + str(queries) + "\ndb Execution Time: "+str(dbTime))
        return value

    def get_group(self, file):
        for g in group_prefix_re:
            name = g.findall( file )
            if name:
                return name[0]

    def get_summary(self, results_dict, sum):
        list = [ (item[1], item[0]) for item in results_dict.items() ]
        list.sort( reverse = True )
        list = list[:40]

        res = "      tottime\n"
        for item in list:
            if sum:
                res += "%4.1f%% %7.3f %s\n" % ( 100*item[0]/sum, item[0], item[1] )
            else:
                res += "%4.1f%% %7.3f %s\n" % ( 0, item[0], item[1] )

        return res

    def summary_for_files(self, stats_str):
        stats_str = stats_str.split("\n")[5:]

        mystats = {}
        mygroups = {}

        sum = 0

        for s in stats_str:
            fields = words_re.split(s);
            if len(fields) == 7:
                time = float(fields[2])
                sum += time
                file = fields[6].split(":")[0]

                if not file in mystats:
                    mystats[file] = 0
                mystats[file] += time

                group = self.get_group(file)
                if not group in mygroups:
                    mygroups[ group ] = 0
                mygroups[ group ] += time

        return " ---- By file ----\n\n" + self.get_summary(mystats,sum) + "\n ---- By group ---\n\n" + self.get_summary(mygroups,sum)

    def process_response(self, request, response):
        self.prof.close()

        out = StringIO()
        old_stdout = sys.stdout
        sys.stdout = out

        stats = hotshot.stats.load(self.tmpfile)
        stats.sort_stats('time', 'calls')
        stats.print_stats()

        sys.stdout = old_stdout
        stats_str = out.getvalue()

        profiling_info = response.content

        if response and response.content and stats_str:
            profiling_info = stats_str

        profiling_info = "\n".join(profiling_info.split("\n")[:40])

        profiling_info += self.summary_for_files(stats_str)

        logger.debug("\n"+profiling_info)

        return response