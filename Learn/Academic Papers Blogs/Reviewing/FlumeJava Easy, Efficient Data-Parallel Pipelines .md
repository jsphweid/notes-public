# FlumeJava: Easy, Efficient Data-Parallel Pipelines (2010)

[[35650.pdf]]

from [here](https://www.youtube.com/watch?v=AZht1rkHIxk), it’s the basis of DataFlow

addresses the many MapReduces that it takes to get a job done sometimes

- then you have to have more glue code, delete intermediate results, etc.

underlying primitives are MapReduces

creates an execution graph of sorts, maybe like tensorflow?

- deferred evaluation
    - creates an execution plan, then optimizes it

easier to test

java

“Parallel Collections”

- represented as java classes
- abstract away the details of how the data is stored (in memory, disk, external, etc.)
- can test with small in-memory, but in production uses external disks for example — based on the size of the data (which it learns from the execution plan)

[[MapReduce  Simplified Data Processing on Large Clusters (2004)]] 

- implemented in c++ but libraries exist to allow this to be invoked by other languages
    - for example, Java via JNI ([[Foreign Function Interface]])

## Details

central class is `PCollection<T>`

- can be created in-memory from a Java Collection<T>
- text files are `PCollection<String>` and binary “record-oriented” file is `PCollection<T>` given a spec how to decode each binary record into a java object

then there is `PTable<K, V>`

- subclass of `PCollection<Pair<K, V>>` (basically a type synonym)
- unordered bag of pairs

manipulating a `PCollection` is invoking data-parallel operations on it, there are just a few but you can build others from those

- primitives:
    - **parallelDo()**
        - seems like you can output 0 or more things per element, which feels unusual for a `map`
    - **groupByKey()**
        - `PTable<K,V>` → `PTable<K,Collection<V>>`
        - multi-map to uni-map
            - [x]  what’s that mean?
                - multi-map is like a dict where values are list/sets
                - says input “which can have many key/value pairs with the same key”
                    - how can they have the same key, wouldn’t it just overwrite?
                - **I guess a Table isn’t completely like a python dict, it’s “is just an unordered bag of pairs”**
        - “captures the essence of the shuffle step of MapReduce”
            - [ ]  what does this mean? I need to know more about the shuffle step
    - **combineValues()**
        - works on `PTable<K,Collection<V>>` combining the V’s into a single V
        - apparently like a ParallelDo but has a more efficient implementation
        - uses MapReduce “combiner”
            - [x]  what is MR Combiner
                - it’s that thing that allows simplification of intermediate values [[MapReduce-Simplified-Data-Processing-on-Large-Clusters-2004-c0b5a3e218e140b993fb99d5ee0d599c#fbdd8df6b98e4a8e83b7473f254659ec](MapReduce Simplified Data Processing on Large Clus]] often times it *is* the reduce function but just runs on the mapper servers
    - **flatten()**
        - like flattening a list of lists (but instead it’s `PCollection<T>`’s of course)
            - does it without copying… just creates a new view somehow
- derived
    - count (seems kinda like Counter)
    - join (creates unimap from *multiple* tables, values become tuples of collections (yes tuples of collections)
    - top (return great N elements)

everything is *deferred* or *materialized*

`PObject`

java object of type T? (`PCollections<T>`)

way of introspecting data?

- [ ]  tbh, I really didn’t understand this

## Optimizing

series of independent graph transformations

some optimizations

- parallelDos
    - producer/consumer fusion
    - sibling fusion - when two nodes use same parent,
- sink flattens - since flatten is merge between two sets effectively, when it comes right before a group by key, it can pretty much be dropped

watch more [here](https://www.youtube.com/watch?v=AZht1rkHIxk)

left off at page 7