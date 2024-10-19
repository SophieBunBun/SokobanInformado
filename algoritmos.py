from searchPlus import *
from sokoban import *
from ProblemaGrafoHs import *


def beam_search_plus_count_jack(problem, W, f):
    """Beam Search: search the nodes with the best W scores in each depth.
       Return the solution and how many nodes were expanded."""
    f = memoize(f, 'f')
    node = Node(problem.initial)
    if problem.goal_test(node.state):   # start from root
        return node, 0
    frontier = PriorityQueue(min, f)    # frontier is a priorityqueue of the ones that might be interesting to check
    frontier.append(node)

    explored = set()    # to keep track of all explored; fast check to not waste time in parsing for comparisons
    visited_not_explored = {node.state} # to compare similar states from different paths

    """frontier will be destroyed over time as we check all possibile states along
    the heuristic in f; when it's all over, return how many attempts were made so
    it's not in vain"""
    while frontier:
        node = frontier.pop()
        print(node.solution())
        explored.add(node.state)    # "explored" just means judging if it's the end
        if(problem.goal_test(node.state)):  # Cave Johnson, we're done here?
            return node, len(explored)
        if (node.state in visited_not_explored):
            visited_not_explored.remove(node.state) # literally just explored this state, move on
        for child in node.expand(problem):
            if child.state not in explored: # not explored means we add to the list
                if child.state not in visited_not_explored:
                    frontier.append(child)
                    visited_not_explored.add(child.state)
                else:
                    if child in frontier:
                        incumbent = frontier[child]
                        if f(child) < f(incumbent):
                           del frontier[incumbent]
                           frontier.append(child)
        frontier = get_W_best(frontier, W, f)   # purge unwanted children
    return None, len(explored)

def get_W_best (queue, W, f):
    freeman = PriorityQueue(min, f)
    for x in range(W):
        if len(queue) > 0:
            freeman.append(queue.pop())
    return freeman

def beam_search_plus_count(problem, W, f):
    """Beam Search: search the nodes with the best W scores in each depth.
       Return the solution and how many nodes were expanded."""
    f = memoize(f, 'f')
    node = Node(problem.initial)
    if problem.goal_test(node.state):   # start from root
        return node, 0
    frontier = PriorityQueue(min, f)    # frontier is a priorityqueue of the ones that might be interesting to check
    frontier.append(node)

    explored = set()    # to keep track of all explored; fast check to not waste time in parsing for comparisons
    visited_not_explored = {node.state} # to compare similar states from different paths

    """frontier will be destroyed over time as we check all possibile states along
    the heuristic in f; when it's all over, return how many attempts were made so
    it's not in vain"""
    while frontier:
        newFrontier = PriorityQueue(min, f)
        while frontier:
            node = frontier.pop()
            explored.add(node.state)    # "explored" just means judging if it's the end
            print (node.solution())
            print (W)
            if(problem.goal_test(node.state)):  # Cave Johnson, we're done here?
                return node, len(explored)
            if (node.state in visited_not_explored):
                visited_not_explored.remove(node.state) # literally just explored this state, move on
            for child in node.expand(problem):
                if child.state not in explored: # not explored means we add to the list

                    if child.state not in visited_not_explored:
                        newFrontier.append(child)
                        visited_not_explored.add(child.state)
                    else:
                        if child in newFrontier:
                            incumbent = newFrontier[child]
                            if f(child) < f(incumbent):
                                del newFrontier[incumbent]
                                newFrontier.append(child)
        frontier = get_W_best(newFrontier, W, f)   # purge unwanted children
    return None, len(explored)
            
    

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