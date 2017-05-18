import collections
import random


class DynamicDie(collections.defaultdict):
    
    def __init__(self):
        collections.defaultdict.__init__(self, int)
    
    def add_side(self, side):
        self[side] += 1
    
    def total_sides(self):
        return sum(self.values())
    
    def roll(self):
        random_num = random.randint(0, self.total_sides())
        total_pos = 0
        for side, qty in self.items():
            total_pos += qty
            if random_num <= total_pos:
                return side


class MarkovChain(collections.defaultdict):
    """ Yet another markov chain implementation.
        This one differs in the sense that it is able to better support
        huge amounts of data since the weighted randomization doesn't rely
        on duplicates.
    """
    
    # Sentinals 
    # Discussion here: http://stackoverflow.com/questions/1677726
    class START(object):pass
    class END(object):pass
    
    def __init__(self):
        collections.defaultdict.__init__(self, DynamicDie)
    
    def add(self, iterable):
        """ Insert an iterable (pattern) item into the markov chain.
            The order of the pattern will define more of the chain.
        """
        item1 = item2 = MarkovChain.START
        for item3 in iterable:
            self[(item1, item2)].add_side(item3)
            item1 = item2
            item2 = item3
        self[(item1, item2)].add_side(MarkovChain.END)
    
    def random_output(self, max=100):
        """ Generate a list of elements from the markov chain.
            The `max` value is in place in order to prevent excessive iteration.
        """
        output = []
        item1 = item2 = MarkovChain.START
        for i in range(max-3):
            item3 = self[(item1, item2)].roll()
            if item3 is MarkovChain.END:
                break
            output.append(item3)
            item1 = item2
            item2 = item3
        return output
