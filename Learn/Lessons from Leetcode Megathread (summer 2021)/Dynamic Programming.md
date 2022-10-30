# Dynamic Programming

watching [https://www.youtube.com/watch?v=oBt53YbR9Kk](https://www.youtube.com/watch?v=oBt53YbR9Kk)

view everything as a tree. Use a tree to brute force all possible solutions but use memoization to drastically reduce the compute time

# memoization

saving function outputs for future runs

### time/space analysis

often with trees, the time is **at minimum** (other significant factors can be added) the size of the tree which is generally the number of branchings to the depth power. In other worse, something with 2 branchings of depth 5 will be `2^5`. Of course if each fn call does something like copy some list or other expensive operation, that may also need to be factored in. Finally when you add memoization, it cuts down quite a bit on the computation but exactly how it does so depends on the algorithm. It may change something from `2^5` to `5^2`, for example

# tabulation