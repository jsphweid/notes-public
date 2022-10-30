# Graphs

things I've messed up before

- a graph has loops (otherwise it's basically a tree) — you might have to have some defense against this
- a bi-directional graph must have ends connected both ways

### Dijkstra

finding the best route

### Minimal Spanning Tree

prim's algorithm - one I first learned, makes decent sense, is very fast

- pick random point and just keep searching for the next cheapest option

kruskal's algorithm - uses union find

- sort edges then start making groups. every time you encounter something that is in a previous group, but the new nodes in there. If both nodes are a part of different groups, those groups need to be combined as well