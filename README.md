# A Visualization of A* and GBFS 

##This project was implemented to understand the optimality and efficiency differences between A* and GBFS. 

##GBFS 

Best-first search algorithm visits next state based on heuristics function f(n) = h with lowest heuristic value (often called greedy). 
It doesn't consider cost of the path to that particular state. All it cares about is that which next state from the current state 
has lowest heuristics.


##A*

A* is a popular algorithm for path-finding that is used heavily in AI. It is a modified version of Dijkstra's algorithm 
with an added heuristic. It addresses the inefficiences of Dijkstras, where every neighbour node connected to the current set 
is considered. A simple example to illustrate its efficiency is to consider an NxN manhattan grid where every edge has a weight
of 1. In this project, I chose to use the Euclidean distance + path cost of each candidate node from the target node as my greedy metric. 

> Using the test data supplied, you can run either algorithm and get a feel for how the algorithms tackle the same problem. 
