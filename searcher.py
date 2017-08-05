#
# searcher.py (Final Project)
#
# classes for objects that perform state-space search on Eight Puzzles
#
# name: Azu Eleonu
# email: aeleonu@bu.edu
#
# If you worked with a partner, put his or her contact info below:
# partner's name:
# partner's email:
#

import random
from state import *

class Searcher:
    """ A class for objects that perform random state-space
        search on an Eight Puzzle.
        This will also be used as a superclass of classes for
        other state-space search algorithms.
    """
    ### Add your Searcher method definitions here. ###
    def __init__(self, init_state, depth_limit):
        """ constructs a new Searcher object by initializing states, tested, and depth limit. """
        self.states = [init_state]
        self.num_tested = 0
        self.depth_limit = depth_limit
        
        

    def __repr__(self):
        """ returns a string representation of the Searcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        if self.depth_limit == -1:
            s += 'no depth limit'
        else:
            s += 'depth limit = ' + str(self.depth_limit)
        return s


### Add your other class definitions below. ###

    def should_add(self, state):
        """ takes a state object and returns True if the called Searcher should
            add state to its list untested states. """
        if self.depth_limit != -1 and state.num_moves > self.depth_limit:
            return False
        elif state.creates_cycle() == True:
            return False
        else:
            return True

    def add_state(self, new_state):
        """ takes a single State object called new_state and adds it to the Searcher's list of
            untested states. """
        self.states += [new_state]

    def add_states(self, new_states):
        """ Takes a list of state objects and processes the elements one line at a time. """
        for x in new_states:
            if self.should_add(x) == True:
                self.add_state(x)

    def next_state(self):
        """ chooses the next state to be tested from the list of 
            untested states, removing it from the list and returning it
        """
        s = random.choice(self.states)
        self.states.remove(s)
        return s

    def find_solution(self):
        """  performs a full random state-space search, stopping when the goal state
             is found or when the Searcher runs out of untested states. """
        while len(self.states) > 0:
            s = self.next_state()
            self.num_tested += 1
            if s.is_goal() == True:
                return s
            else:
                self.add_states(s.generate_successors())
        return None
        
class BFSearcher(Searcher):
    """ Class for searcher objects that perform breadth-first search (BFS)
        instead of random search. """
    def next_state(self):
        """ overrides next_move method inherited from Searcher. """
        b = self.states[0]
        self.states.remove(b)
        return b

class DFSearcher(Searcher):
    def next_state(self):
        """ overrides next_move method inherited from Searcher. """
        s = self.states[-1]
        self.states.remove(s)
        return s

class GreedySearcher(Searcher):
    def __init__(self, init_state, heuristic, depth_limit):
        """ constructor for a GreedySearcher object
            inputs:
             * init_state - a State object for the initial state
             * heuristic - an integer specifying which heuristic function should
             be used when computing the priority of a state
             * depth_limit - the depth limit of the searcher
        """
        self.heuristic = heuristic
        self.states = [[self.priority(init_state), init_state]]
        self.num_tested = 0
        self.depth_limit = depth_limit
    
    def priority(self, state):
        """ takes a state object and returns the priority of that state. """
        if self.heuristic == 1:
            b = state.board.distance()
            b *= -1
            return b
        else:
            b = state.board.distance()
            b *= -1
            return b
            
    def add_state(self, state):
        """ overrides add_state method inherited from Searcher. """
        self.states += [[self.priority(state), state]]

    def next_state(self):
        """ overrides next_move method inherited from Searcher. """
        s = max(self.states)
        self.states.remove(s)
        return s[1]
    
    
class AStarSearcher(Searcher):
    """ class for searcher objects that perform A* search. """
    def __init__(self, init_state, heuristic, depth_limit):
        """ constructor for a GreedySearcher object
            inputs:
             * init_state - a State object for the initial state
             * heuristic - an integer specifying which heuristic function should
             be used when computing the priority of a state
             * depth_limit - the depth limit of the searcher
        """
        self.heuristic = heuristic
        self.states = [[self.priority(init_state), init_state]]
        self.num_tested = 0
        self.depth_limit = depth_limit
        
    def priority(self, state):
        """ Overrides priority in GreedySearcher. """
        if self.heuristic == 1:
            b = state.board.distance() * -1
            return b
        else:
            b = state.board.distance() + state.num_moves
            b *= -1
            return b

    def add_state(self, state):
        """ overrides add_state method inherited from Searcher. """
        self.states += [[self.priority(state), state]]
        
    def next_state(self):
        """ overrides next_move method inherited from Searcher. """
        s = max(self.states)
        self.states.remove(s)
        return s[1]
