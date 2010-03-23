#!/usr/bin/env python

import os, random, subprocess, getpass

CHARS = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
BLACKLIST = (
    'jquery',
    '.tar.gz',
    'admin/css',
    'admin/img',
    'admin/js',
    '/.git/'
)

def replace(repl, text):
    text = text.replace('/gitignore', '/.gitignore')
    for key, value in repl.iteritems():
        text = text.replace('$$$$%s$$$$' % (key,), value)
    return text

def main():
    repl = {}
    
    cur_user = os.getlogin()
    
    pn = raw_input('Project name: ')
    repl['PROJECT_NAME'] = pn
    
    repl['NAME'] = raw_input('Administrator name  [%s]: ' % cur_user) or cur_user
    repl['EMAIL_ADDRESS'] = raw_input('Administrator e-mail address: ')
    
    repl['SECRET_KEY'] = ''.join([random.choice(CHARS) for i in xrange(50)])
    
    dest_dir = raw_input('Destination directory (currently at %s): ' % (os.getcwd(),)) or os.getcwd()
    dest_dir =  os.path.realpath(os.path.expanduser(dest_dir))
    dest = os.path.join(dest_dir, repl['PROJECT_NAME'])
    
    os.makedirs(dest)
    
    for root, dirs, files in os.walk('./skel/'):
        for filename in files:
            source_fn = os.path.join(root, filename)
            dest_fn = replace(repl, os.path.join(dest, root.replace('./skel/', ''), replace(repl, filename)))
            try:
                os.makedirs(os.path.dirname(dest_fn))
            except OSError:
                pass
            print 'Copying %s to %s' % (source_fn, dest_fn)
            should_replace = True
            for bl_item in BLACKLIST:
                if bl_item in dest_fn:
                    should_replace = False
            data = open(source_fn, 'r').read()
            if should_replace:
                data = replace(repl, data)
            open(dest_fn, 'w').write(data)
            os.chmod(dest_fn, os.stat(source_fn)[0])
    repl['virtenv'] = raw_input('Virtual environment name (e.g. %s): ' % pn) or pn
    
    print "Bootstrapping the virtual envirionment..."
    subprocess.call(['%s/setup/_bootstrap.sh' % dest,], shell=True)
    print "Making the virtual environment (%s)..." % repl['virtenv']
    create_env_cmds = [
        'source virtualenvwrapper_bashrc', 
        'cd %s' % dest,
        'mkvirtualenv --no-site-packages --distribute %s' % repl['virtenv'],
        'easy_install pip'
    ]
    create_pa_cmd = [
        'source virtualenvwrapper_bashrc',
        'cat > $WORKON_HOME/%s/bin/postactivate '\
        '<<END\n#!/bin/bash/\ncd %s\nEND\n'\
        'chmod +x $WORKON_HOME/%s/bin/postactivate' % (repl['virtenv'], dest,repl['virtenv'])
    ]
    subprocess.call([';'.join(create_env_cmds)], env=os.environ, executable='/bin/bash', shell=True)
    subprocess.call([';'.join(create_pa_cmd)], env=os.environ, executable='/bin/bash', shell=True)
    print "Installing requirements..."
    subprocess.call(['$WORKON_HOME/%s/bin/pip install -r %s' \
        % (repl['virtenv'], os.path.join(dest, 'setup', 'requirements.txt'))],
        env=os.environ, executable='/bin/bash', shell=True)

if __name__ == '__main__':
    main()