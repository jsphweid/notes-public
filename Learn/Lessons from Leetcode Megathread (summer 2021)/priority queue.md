# priority queue

min heap - top item to poll is the smallest

max heap - top item to poll is the largest

heap is just the binary tree structure (doesn't have to be binary tree actually?)? it's the underlying data structure for a priority queue

you could implement a priority queue using other methods... (obviously), it's just an ADT

- It's a better solution when you need to something but not everything perhaps.... Example. You have a 1000 things, and you want to get the 5 smallest things. sorting would make it nlogn, but with heapq, it's n+klogn where k is 5... much better as 5logn than 100logn
- also better at adding things in and taking them out
- NOT better when you need every item sorted and it never changes after that
- but if you're just sorting something then say popping all the items off, heapq is better because the logn operation you're paying for is on a list that is getting smaller every time...  although when I tested this with really large lists they seem to be roughly equal...?

with the python lib, all fn's in `heapq` operate on an existing list!