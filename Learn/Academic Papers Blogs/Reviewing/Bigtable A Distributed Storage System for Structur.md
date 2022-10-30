# Bigtable: A Distributed Storage System for Structured Data (2006)

[[bigtable-osdi06.pdf]]

gives clients dynamic control over data layout and format

dev time was 2.5 years

bigtable - sparse, distributed, persistent, multi-dimensional sorted map

- indexed by row key, column key, and timestamp
- value is uninterpreted array of bytes

also reading [this](https://medium.com/swlh/building-dynamodb-brick-by-brick-237e0008b698)

Anyways

![Untitled](Learn/Academic%20Papers%20Blogs/Reviewing/Bigtable%20A%20Distributed%20Storage%20System%20for%20Structur/Untitled.png)

This is presumably a snippet of how Google actually works (or did in 2006). Columns are pages that point to the row. I bet it can get very wide then… Notice how the contents have multiple versions with different timestamps

reads/writes are atomic — meaning only one operation can be performed at a time

### rows

a row range is called a ***tablet*** — i.e., a range of partitions??

they used reversed hostname components because it makes it easy to have locality in the data

- [ ]  this is always a source of confusion for me… As intense locality == hot partition to some extent, right? Wouldn’t you want to spread load to as many machines as possible?

### columns

I mentioned earlier how wide this table can get… well notice they are prefixed with “anchor:"

- this is known as a column ***family***
    - families have same type (usually) and data gets compressed (interesting!)
- number of distinct families should be small (like 100), but actual columns is unbounded
- usual form is `family:qualifier`

### timestamps

real time in microseconds or assigned by client

- [x]  wonder what happens when duplicate?
    - seems like duplication is allowed unless clients don’t want it to happen

stored in decreasing order so latest is always at top

client has a lot of control as to how versioning is handled

basically a ‘garbage collection’ mechanism

# API

provides scanner which can scan across multiple families/rows/etc. 

provides single row transactions (probably more by now)

supports cells to be used as integer counters

- [ ]  what does this mean exactly?

allows scripts *in the address spaces of servers* - Sawzall 

- [ ]  what does this mean?
- could it be like dynamodb VTL???

can be integrated with MapReduce

# How it’s built

built on top of [[Google File System [[(2003)]]]] 

- stores logs and data files

Bigtable data is stored in Google SSTable file format

- persistent ordered immutable map
- I believe they are occasionally combined but never modified
    - SSTable Compaction
- SSTable contain sequence of blocks (usually 64KB in size)
    - block index stored at end, loaded into memory

## components

- library linked into every client
- one master server
- many tablet servers

Honestly it seems similar setup to GFS 

- master and chunk servers
- master and tablet servers

### master servers

seem like they manage tablets servers and files

### tablet servers

10-1000 tablets per tablet server

handles read/write requests to the tablets it has loaded

splits tablets when they become too large

big table cluster

 → many tables

 → each table split into many tablets

- split at row boundaries

table has 1 tablet initially then each tablet is 100-200MB in size

if a machine that has a tablet fails, the tablet just goes to a different machine

watching this [https://www.youtube.com/watch?v=2cXBNQClehA](https://www.youtube.com/watch?v=2cXBNQClehA)

### 3-level lookup

TOP - bootstrapped from lock service, never splits(?), points to META0

META0 - find owner of META1 tablet

META1 - holds locations of all tablets (can be split like other tablets)

Information in TOP is cached

# Tablets

## A Single Tablet

(a single machine may *serve* hundreds of tablets)

(kinda like my chunks

if a write comes in, puts in a queue that a writing thread handles

- write data to GFS
- one it is committed
    - in memory on the chunk server
        - “most data we’re writing [writing only to memory] is a sufficient level of safety”
        - [ ]  but it *eventually* gets flushed to disk, right?
- write log for thousands of machines with millions of tablets, millions of logs writing at a time
    - not ideal so they use shared logs, each tablet server writes 1 log for all tablets
    - but then updates for all tablets are in 1 file
    - uhh 46:30 in the video but ya

SSTable

- sorted
- keys are (row, column, timestamp) triples
- so finding an entire row’s data is a matter of contiguous read with row

Family names in columns and sparse columns facilitate joins

### Metadata tablets and 3-tier B+-Tree like structure

1. A root metadata tablet is stored in a chubby file… This tablet is never split
    - [ ]  is this one per table?
2. It stores the location of all the other metadata tablets?
3. Each of those other metadata tablets stores the location of the actual content tablets

Metadata tablets are stored in memory (with GFS?), the tablet locations are also cached by the client. If it’s not in the cache it may have to get info from chubby lock file and each of the metadata tablets, so a few roundtrips.

### Tablet Assignment

one tablet exists on a single tablet server at a time

- [ ]  doesn’t this make a single tablet server a bottleneck?

Tablet Servers

- they create a unique file in a certain Chubby dir. The master monitors this dir to ‘discover’ new tablet servers
- server acquires a lock on this unique file
    - it’ll stop serving the tablets if it loses the lock
    - if file exists, it’ll try to reacquire a lock, but if the file is gone, the server di

### Tablet Serving

tablet state updates are committed to a log in GFS

recently committed updates get stored in memory, older ones are stored in SSTable files (als on GFS)

a tablet can recover itself by reading this information in the log from some redo point

write

- write operations arrive at the tablet server, which checks that the request is well-formed and authed (gets data from a chubby file)
- gets committed to a commit log and contents inserted into memtable

read

- well formed and authed
- reads from SSTable and memtable (which are both sorted), so merge is fast

### Compaction

when memtable gets a certain size, it’s frozen and converted to SSTable as a new memtable is created

- [ ]  how does this not impact read/writes? (paper says they can continue during this)
- [x]  I need more info on the SSTables, how are they organized
    - oh the compaction step periodically merges SSTable/memtable information into a new organized SSTable
    - [ ]  but I still want to know more

there is major and minor compaction, minor is when it happens to a few SSTables, major is when it happens to all

- major compaction also removes deleted data so it doesn’t keep taking up space?

### Locality Group

uhh something about making reads go in memory and having some control over that

### Compression

each block in SSTable can be compressed. That means you don’t have to read the entire SSTable to decompress correctly

can save 10:1 because locality of data makes local data similar (and hence compressable)

### Commit logs

a server keeps a single commit log for all its tablets to reduce the number of files and hence number of disk seeks (and also something like reduces effectiveness of group commit optimizations)

but since they are inter-mingled, recovery is tricky. to avoid many tablet servers having to read the whole log file over and over to look at the tablet it cares about recovering, the log file is ordered (this process is distributed) which means now each new tablet server only has to read the part of the file that is relevant

## Uses

Google Analytics

- raw click table (200TB) - handles incoming data
- summary (20TB) - periodically scheduled jobs look at raw click table and make summaries

Google Earth

- table to preprocess data
- other tables for serving client data