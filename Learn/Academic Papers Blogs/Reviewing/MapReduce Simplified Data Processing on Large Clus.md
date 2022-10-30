# MapReduce: Simplified Data Processing on Large Clusters (2004)

[[mapreduce-osdi04.pdf]]

basically there are simple tasks but they become complicated because of the distributed nature of the computation

hides this complexity in the form of a library

it’s a programming model — restricts

### how it works

1. splits input into M pieces, 16-64MB per piece
2. starts up program on many clusters
    1. one of these is the master, rest are workers
    2. assigns idle workers these map or reduce tasks
3. output of map function is buffered in memory, but occasionally written to disk, partitioned in R regions (using some hash function)
    - location is forwarded to master, which forwards the location to reduce workers
    - this location is local and hence the map task might need to be ran again if there is a failure
4. when reduce workers have all data, it sorts the data (possibly externally if too big) and send it to reduce function
    - [ ]  they have to get it from many machines, right?
5. outputs all to R files on a global file system

Tries to schedule tasks on a machine where input file(s?) already is. Apparently this significantly network usage

### stragglers

because of various reasons a single task can take a lot longer (bad HD, busy server, etc.), so when the MR operation is close to completion, it starts backup tasks for the remaining in-progress tasks. For a few percent extra utilization overall, it prevents a 44% slowdown for overall task

### extras

1. custom partitioning, useful for when you want the ending data to be local (like urls)
2. within give partition, intermediate key/value pairs are ordered, which makes it easy to generated a sorted output file
3. combiner function - basically like a reduce that operates on the map function machine, can cut down on the sometimes insane repetition of key/values - often times it IS the reduce function (but of course MapReduce framework treats them differently)
4. counter - can have custom counters that piggy back off status response and also