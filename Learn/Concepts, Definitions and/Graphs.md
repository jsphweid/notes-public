# Graphs

Can be represented via an ordered pair of set of vertices/nodes and a set of edges

- G = (V, E)
    - E is represented by the two nodes it connects (either **undirected** or **directed**)
        - unordered E is {a, b} whereas ordered is (a, b) (and/or possibly (b, a) if it goes the other way too)

Weighted graph

- edges have weights/cost/strength

Edges can point to themselves ("self-loop")

Multi-Edge graphs are when there is a node with more than one edge to the same node

Path - sequence of nodes

Acyclic - graph with no cycle (tree)

- directed acyclic graph

Simple Cycle - no repetition other than start/end

Adjacency Matrix - list of list that has pretty good efficient lookup for nodes/edges, BUT takes up a lot of space if list is really big. And it wastes a lot of data if the number of connections per node is small 

![[/Untitled.png]]

Adjacency List - like the matrix except without the redundant 0's