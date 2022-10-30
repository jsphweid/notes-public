# Google File System (2003)

[[gfs-sosp2003.pdf]]%207b1844dfa9fe4e28b846c285b639d717/gfs-sosp2003.pdf)

originally called BigFiles, actually made by Larry and Sergey at Stanford

designed with component failure in mind

files are typically very large because having many small files is “unwieldy”

files are typically just appended to instead of mutating existing data

optimized for

- large streaming reads (1MB or more)
- small random reads (few KB)

relaxed consistency model

some applications will even order their reads so it advances steadily through instead of going back and forth

must handle multiple clients concurrently appending to the same file

- [ ]  mentions producer-consumer queues and many way merging… need more info

favors bandwidth over low latency

familiar but not POSIX

in addition to CRUD, it can:

- snapshot - low cost file/dir copy
- record append - allows multiple clients to add data to same file concurrently while preserving atomicity. GFS decides the offset as opposed to a regular append where the application chooses the offset based on where it perceives the current end to be
- (write) - data is written at an application specified offset

### client

### chunk server

linux box that stores files on the disk

does not cache because linux’s buffer cache already does that

communicates to master via heart beats

### master

## Read

1. client asks master for filename and byte offset, but specifies byte offset in chunk index. this is possible because chunks are known fixed size (64 MB)
    - [ ]  if a bunch of misc files are 2 MB, would 32 of them go in one chunk?
    - [ ]  “Lazy space allocation avoids wasting space due to internal
    fragmentation, perhaps the greatest objection against such
    a large chunksize” What does this mean?
2. master replies with chunk handle and chunk server locations
    - [x]  what is a handle?
        - probably just the id of the chunk to get from the chunk servers
3. client requests chunks via handles and it also knows

## Write

If we are writing/appending to a chunk, we have to write to all the replicas

1. master grants a *lease* to one of the replicas called **primary**
2. replica picks an order for all operations and the other replicas must follow

- [ ]  need to understand more about dataflow
    - but the goal is to utilize as much capacity as possible, avoiding any bottlenecks

# Metadata on Master server

all of this is kept in memory

1. file and chunk namespaces
    - [ ]  what are these
    - stored in operation log as well
2. mapping from files to chunks
    - stored in operation log as well
3. location of each chunk’s replicas
    1. **NOT** stored in operation log as well, instead the master asks all chunk servers at startup and whenever a chunk server joins the cluster
    2. truth is stored ultimately on chunkserver… keeping them in sync would be unnecessarily difficult. 

There are jobs in the background that go over the memory periodically and perform tasks… for example if a chunk server failed and something needs to be re-replicated, it can find that and re-run

64MB requires less than 64 bytes of metadata (somehow)

### Operation Log

similar to databases, like a write-ahead log, commits state to a log before making the change visible to clients

# Consistency

- [ ]  what are namespaces?
    - [ ]  locking?
- [ ]  what are file regions?
    - [ ]  **consistent** file regions
        - all clients see same data regardless of which replica they read from
    - [ ]  **defined** file regions
        - [ ]  consistent but also everyone sees the same thing?
        

I really need to re-review a lot of this

could read how hadoop works

# Master Operation

multiple master operations can run simultaneously and locks help ensure everything is kept straight

### locks

When reading/writing/etc, you must acquire read/write locks. For example, you shouldn’t be able to copy a directory and delete it’s parent during the middle of the copy. 

Their example:

if `/home/user` is being snapshotted to `/save/user`, you shouldn’t be able to create a file in `/home/user/foo`

- snapshot from `/home/user` to `/save/user` requires:
    - read locks on `/home` and `/save`
        - [x]  why?
            - prevents directory from being deleted
    - write locks on `/home/user` and `/save/user`
- file creation on `/home/user`
    - read locks on `/home` and `/home/user`
    - write lock on `/home/user/foo`

## Deletion and GC

whenever something is deleted, it’s shadow deleted, only fully deleted days later possibly