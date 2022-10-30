# disjoint sets

two or more sets with nothing in common (hence "disjoint")

it's more in the vein of branches of unique nodes, not necessarily sets as a python native data structure

[https://en.wikipedia.org/wiki/Disjoint-set_data_structure](https://en.wikipedia.org/wiki/Disjoint-set_data_structure)

also called "union find"

- find - tell us which set something belongs to
    - it's likes nodes in a tree, it finds the parent
- union - groups sets together
    - it's like grouping branches together
    

when we come across a new node that needs to connect, we find the ancestor of the connecting node and the current node. Find out which one is bigger (has larger rank), and assign the whole branch to that one.

path compression is the act of tying a node directly to the root, presumably so subsequent calls to find yield a much quicker path...