from searchPlus import *
from sokoban import *
from ProblemaGrafoHs import *

def beam_search_plus_count(problem, W, f):
    """Beam Search: search the nodes with the best W scores in each depth.
       Return the solution and how many nodes were expanded."""
    f = memoize(f, 'f')
    node = Node(problem.initial)
    if problem.goal_test(node.state):   # start from root
        return node, 0
    explorable = PriorityQueue(min, f)    # frontier is a priorityqueue of the ones that might be interesting to check
    explorable.append(node)

    explored = set()    # to keep track of all explored; fast check to not waste time in parsing for comparisons
    win = None

    """frontier will be destroyed over time as we check all possibile states along
    the heuristic in f; when it's all over, return how many attempts were made so
    it's not in vain"""
    while explorable:
        explorable, explored, win = level(explorable, explored, problem, W, f)
        if win != None: break
    return win, len(explored)

"""
Repeat until we've found all options to be in explored
execute for each level

for any given level, there are at most W given nodes
expand them all, keep only the W highest
repeat"""

def level(explorable, explored, problem, W, f):
    visited_not_explored = set()
    children = PriorityQueue(min, f)

    while explorable:   # for every one of this level's expandable nodes
        node = explorable.pop() 
        if(problem.goal_test(node.state)):
            return explorable, explored, node
        explored.add(node.state)
        if (node.state in visited_not_explored):
            visited_not_explored.remove(node.state) # just explored
        for child in node.expand(problem):
            if child.state not in explored:
                if child.state not in visited_not_explored:
                    visited_not_explored.add(child.state)
                    children.append(child)
                else:
                    if child in children:
                        incumbent = children[child]
                        if f(child) < f(incumbent):
                            del children[incumbent]
                            children.add(child)
    children = get_W_best(children, W, f)
    return children, explored, None


def get_W_best (queue, W, f):
    freeman = PriorityQueue(min, f)
    for x in range(W):
        if len(queue) > 0:
            freeman.append(queue.pop())
    return freeman

def beam_search(problem, W, h=None):
    """Beam graph search with f(n) = g(n)+h(n).
    You need to specify W and the h function when you call beam_search, or
    else in your Problem subclass."""
    h = memoize(h or problem.h, 'h')
    return beam_search_plus_count(problem, W, lambda n: n.path_cost + h(n))

def IW_beam_search(problem, h):
    """IW_beam_search (Iterative Widening Beam Search) começa com beam width W=1 e aumenta W iterativamente até
    se obter uma solução. Devolve a solução, o W com que se encontrou a solução, e o número total (acumulado desde W=1)
    de nós expandidos. Assume-se que existe uma solução."""
    W = 0
    totallength = 0
    done = None
    while done == None:
        W = W+1
        done, length = beam_search(problem, W, h)
        totallength += length
    return done, W, totallength