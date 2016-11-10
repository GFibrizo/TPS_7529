#coding=utf-8

import itertools
import sys

def read_distance_matrix(file_name):
    '''file_name: the name of a file that stores a matrix. Each line is a row
    and columns are separated by whitespace.
    Returns a dictionary with the following format
    {Vertex:{neighbour: distance, neighbour: distance,...}...'''
    with open(file_name) as f:
        distances = {}
        current_vertex = 0
        for line in f:
            vertex_distances = line.rstrip("\n").split()
            distances[current_vertex] = {}
            for vertex, distance in enumerate(vertex_distances):
                distances[current_vertex][vertex] = int(distance)
            current_vertex += 1
        return distances

def every_path(vertexes):
    '''Vertexes is an iterable object.
    Returns a list with every possible combination of destination and path that
    lead there. Path is a frozenset. 
    The elements on the list are ordered by
    step because in order to get the minimum cost path of, for example, step 3,
    minimal costs of step 2 are needed and so on.
    [(destination, path), (destination, path)]'''
    paths = []
    for x in xrange(1, len(vertexes)):
        for vertex in vertexes:
            combinations = itertools.combinations(vertexes, x)
            for combination in combinations:
                set_comb = frozenset(combination)
                if vertex in set_comb:
                    continue
                else:
                    paths.append((vertex, set_comb))
    return paths

def update_cost_and_parent(destination, through, distances, min_cost):
    '''destination: vertex number
    through: frozenset of vertexes that must be visited in the path
    distances: {Vertex:{neighbour: distance, neighbour: distance,...}...
    min_cost: {(destination, through): {distance: x, parent: y}}
    Updates the min_cost dic'''
    parent = -1
    cost = float("inf")
    for vertex in through:
        copy_set = set(through)
        copy_set.discard(vertex)
        copy_set = frozenset(copy_set)
        possible_parent = vertex
        possible_cost = min_cost[(possible_parent, copy_set)]["distance"] + distances[possible_parent][destination]
        if possible_cost < cost:
            cost = possible_cost
            parent = possible_parent
    min_cost[(destination, through)] = {"distance": cost, "parent": parent}


def tsp(file_name, origin):
    '''file_name: the name of a file that stores a matrix. Each line is a row
    and columns are separated by whitespace.
    origin: int with the vertex number that is the origin city
    Return the minimum cost of the Travelling Salesman Problem alongside
    with the path in a tuple. I.E: (min_cost, [vertex0, vertex1, ...]'''
    distances = read_distance_matrix(file_name)
    vertexes = set(distances.keys())
    vertexes.discard(origin)
    min_cost = {}
    #Setting up the min_cost dict with the distance of origin to every vertex
    for vertex in vertexes:
        min_cost[(vertex, frozenset())] = {"distance": distances[origin][vertex], "parent": origin}
    
    paths = every_path(vertexes)
    for path in paths:
        update_cost_and_parent(path[0], path[1], distances, min_cost)
    # Setting the cost of travelling to every vertex and returning to origin
    update_cost_and_parent(origin, frozenset(vertexes), distances, min_cost)
    min_cost_result = min_cost[(origin, frozenset(vertexes))]["distance"]
    
    #Adding 1 because the matrix starts with row and column 0 while the
    #cities are numbered from 1 on
    min_path = [origin + 1]
    last_visited = origin
    copy_set = set(vertexes)
    while len(copy_set) != 0:
        last_visited = min_cost[(last_visited, frozenset(copy_set))]["parent"]
        #Adding 1 because the matrix starts with row and column 0 while the
        #cities are numbered from 1 on
        min_path.append(last_visited + 1)
        copy_set.discard(last_visited)
    #Appending the origin because the while doesn't appends the path from origin
    #to a vertex without going thru any other vertex
    min_path.append(origin + 1)
    
    #Reversing the min_path list because the while appends the last vertexes
    #first. A stack would be a better structure to store this but ¯\_(ツ)_/¯
    return (min_cost_result, min_path[::-1])

if __name__ == '__main__':
    min_cost, min_path = tsp(sys.argv[1], int(sys.argv[2]) - 1)
    print "The minimum cost is:", min_cost
    print "The most effective path is:", "->".join([str(x) for x in min_path])

