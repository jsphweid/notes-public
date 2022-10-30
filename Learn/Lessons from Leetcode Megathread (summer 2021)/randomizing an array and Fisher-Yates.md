# randomizing an array and Fisher-Yates

give a random number generator, how do you shuffle a list...

one way would be to generate a random index... then pop the item from list... but that’s slow as it involves popping at a particular index (O(n)). 

another way would be assigning a random float to each element then sorting by the random float

(from here [https://www.youtube.com/watch?v=4zx5bM2OcvA](https://www.youtube.com/watch?v=4zx5bM2OcvA))

The fisher yates is a one pass (no sorting or pop(n)) where you have a pointer at the end and you decrement it through some copied list. As you decrement, you find a random index in the un-decremented space and swap that one with the current decrement.