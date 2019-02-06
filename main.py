from __future__ import print_function
import heapq
import sys
from math import sqrt


def print_graph(graph):
    print("=" * 100)
    for row in graph:
        print('[ ', end='')
        for val in row:
            print(str(val).rjust(3) + ', ', end='')
        print(']')


def print_path(dim, path):
    graph = [['  ' for _ in range(dim)] for _ in range(dim)]
    for c in path:
        graph[c[0]][c[1]] = '##'
    print_graph(graph)


############################################################
# COST
############################################################
def d_elevation(a, b, graph):
    return abs(graph[a[0]][a[1]] - graph[b[0]][b[1]])


def hn(c1, c2, elevation):
    # Ensure we receive coordinates, therefore len == 2
    if len(c1) == 2 and len(c2) == 2:
        x = abs(c2[0]-c1[0])
        y = abs(c2[1]-c1[1])
        return x + y + elevation
        #return int(sqrt(x**2 + y**2)) + elevation
    return 0


def current_cost(curr, start, parent, graph):
    cost = 0
    prev = curr
    while curr != start:
        cost += (1 + d_elevation(curr, prev, graph))
        prev = curr
        curr = parent[curr[0]][curr[1]]
    return cost


############################################################
# BEST FIRST SEARCH
############################################################
def graph_search(start, finish, graph, algorithm):
    # initialize priority queue/heap to start position
    pq = [(0, start)]

    # create visited matrix
    # 0 = unvisited, 1 = visited
    unvisited = dim * dim
    visited = [[unvisited for _ in range(dim)] for _ in range(dim)]
    visited[start[0]][start[1]] = hn(start, goal, 0)

    parent = [[0 for _ in range(dim)] for _ in range(dim)]
    expanded = 0

    while pq:
        curr = heapq.heappop(pq)[1]
        if curr == finish:
            break
        else:
            # enqueue valid neighbours(nb)
            for i in [-1, 1]:
                if 0 <= (curr[0] + i) < dim:  # up/down
                    nb = [curr[0] + i, curr[1]]
                    elevation = d_elevation(curr, nb, graph)
                    if visited[nb[0]][nb[1]] == unvisited and elevation <= 4:
                        cost_val = hn(nb, finish, 1 + elevation)
                        if algorithm == 'a*':
                            cost_val += current_cost(curr, start, parent, graph)
                        visited[nb[0]][nb[1]] = cost_val
                        parent[nb[0]][nb[1]] = [curr[0], curr[1]]
                        expanded += 1
                        heapq.heappush(pq, (cost_val, nb))
                if 0 <= (curr[1] + i) < dim:  # left/right
                    nb = [curr[0], curr[1] + i]
                    elevation = d_elevation(curr, nb, graph)
                    if visited[nb[0]][nb[1]] == unvisited and elevation <= 4:
                        cost_val = hn(nb, finish, 1 + elevation)
                        if algorithm == 'a*':
                            cost_val += current_cost(curr, start, parent, graph)
                        visited[nb[0]][nb[1]] = cost_val
                        parent[nb[0]][nb[1]] = [curr[0], curr[1]]
                        expanded += 1
                        heapq.heappush(pq, (cost_val, nb))

            # print_graph(visited)

    # print visited and parent graphs for debug
    print_graph(visited)
    #print_graph(parent)

    # ensure we found a path by ensuring that we reached the finish
    if curr != finish:
        return []

    # determine path traversed to finish
    path = []
    curr = finish
    while curr != start:
        path.append(curr)
        curr = parent[curr[0]][curr[1]]
    path.append(start)
    path.reverse()
    #print("Length of Best Path: {}".format(current_cost(finish, start, parent, graph)))
    print("Number of Nodes Expanded:",expanded)
    return path


############################################################
# MAIN
############################################################

# declare variable
dim = 0
origin = []
goal = []
matrix = []

# read file into variables
filename = sys.argv[1]
with open(filename, 'r') as f:
    for index, line in enumerate(f):
        # remove extraneous characters
        line = line.strip().replace('[', '').replace(']', '').replace(',', ' ').split()
        # convert char to int
        line = [int(i) for i in line]

        # place into correct variable
        if index == 0:
            dim = line[0]
        elif index == 1:
            origin = line[0:2]
            goal = line[2:4]
        else:
            matrix.append(line)

shortest_path = graph_search(origin, goal, matrix, 'bfs')
print("=" * 75)
if shortest_path == []:
    print("No path exists.")
else:
    print_path(dim, shortest_path)
    print(shortest_path)

shortest_path = graph_search(origin, goal, matrix, 'a*')
print("=" * 75)
if shortest_path == []:
    print("No path exists.")
else:
    print_path(dim, shortest_path)
    print(shortest_path)

print("=" * 75)
