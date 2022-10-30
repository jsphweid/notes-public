# LevelDB

[https://github.com/google/leveldb](https://github.com/google/leveldb)

written by jeff and sanjay

uses [[SSTable]] 

c++

PERFECT FOR LEARNING!

Taking notes on the [[]]

# Impl

### log files

updates go to log file — when they reach a certain size, an SSTable gets created

a copy is kept in memory for quick reads

### SSTables

at first a few SSTables are created… There may be overlapping keys (level-0)

But once the num files exceeds a certain threshold, all level-0, they get promoted into level-1, which seem to be the exact same types of files but with a guarantee that there are no overlapping keys(?). And also the size of that whole level is kept track of. When that overall level size reaches a certain point, an SSTable in that level gets mixed in with the next level above. And the level sizes increase up exponentially

- [x]  every time something is swallowed into the next level, it re-writes the *entire* level?
    - no, only the affected ones it seems, “all overlapping files from the next level”
    - even if the next level up only overlaps partially, it still rewrites everything.
    - level-0 files are special here because there may be more than just the one file that needs to be dissolved..
        - [ ]  what does pick more than 1 really mean?
- [x]  what happens when the values are so big or a single key has so much data it’s far greater than 2MB?
    - the files get as big as they need to to store it
- [ ]  deletion markers???

This happens in the background (somehow), but if the user is still writing, then potentially a lot of level-0 files would build up. This adds costs to the read

### Manifest

stores key ranges of all files in each level and other metadata

every time db is re-opened, a new manifest file is created

formatted as log

- [ ]  what happens when this gets really big?

# [[]]

Batch brings transactionality effectively?

writes happen async, originally I thought this meant that it goes to the log file immediately but later on writes it to SSTables… but I don’t think that’s what async means here — because data loss is possible unless you set a sync option in WriteOption

- “it returns after pushing the write from the process into the operating system”
    - [x]  what does this mean?
        - looks like it just calls fsync (os-level write any dirty buffers to disk) afterwards

### Concurrency

I don’t really get this

DB can only be opened by one process at a time (leveldb acquires lock from OS to ensure this)

But it can still be used across multiple threads but it’s not quite that easy… and it depends

- [ ]  need to do more research….

### Snapshots

allow you to freeze the state the the db, but don’t keep them around for long because they can consume a lot of resources… it must be interesting how this works. Actually I think this is like that snapshot array problem on leetcode

### Iteration

you can iterate over all key/values (or subset, or reverse), easy 

### Slice

the keys and values (array of bytes). Slice is just a pointer to the external byte array and its length

it’s cheaper to refer to it as slice as opposed to strings because you don’t have to copy (potentially large amounts of) data

### Comparator

you can have custom comparators, it’s not too complicated (say your key is really two 4-byte numbers, you want to sort by the first number and break ties with the second)… can make backwards compatibility a bit tricky, however

### Block Size

what is the purpose of this?

uncompressed default size is 4096, which is a special number for HDD? but it gets compressed…?

adjacent keys go into the same block, it becomes a unit of transfer

### Compression

on by default since it’s zippy and really fast

disabled for uncompressible data

- [ ]  what does that mean? and how can it be?

can be disabled, but only in rare cases is this faster

- [ ]  what are those rare cases?

### Filters

says that because of the way it’s organized on disk, a single GET may “involve multiple reads from disk”

- [ ]  how? it seems like a key-value pair can should only be located in 1 file
    - maybe it’s talking about reading log, then SSTable?
- stores some bits of each key in memory? which makes a lot less reads somehow
    - [ ]  how
- keep in mind that custom comparators probably need a custom filter policy

### Checksums

- checksums are stored but you can control how aggressively they are verified

# Log Format

**sequence of 32KB Blocks**, tail may be shorter though

each block is a **sequence of Records.** i.e. a block may contain one or more records

Record

- outline
    - checksum - 4 bytes
    - length - 2 bytes
    - type - 1 byte
        - 1-FULL, 2-FIRST, 3-MIDDLE, 4-LAST
            - FULL - entire user record is supplied
            - FIRST - split
            - MIDDLE - split
            - LAST - split
    - data - byte array of ‘length’
- 7 bytes + data
    - if less than 7 bytes left on block, this is the ‘trailer’ — zero bytes, skip
    - exactly 7 bytes left on block
        - zero data - ??
        - nonzero data - emit FIRST record, then emit all of user data in subsequent block
            - [x]  why go through this pain
                - think about if something is large than 32KB, ya gotta split it. You just gotta support splitting
- apparently this is close to [[Records (RecordIO, TFRecord, LevelDB [[Logs)]]]]

# Table Format

structure

- datablocks
    - key/value pairs stored in sorted order partitioned into blocks
    - optionally compressed
        - [ ]  hmm… I wonder how that changes other things
- meta blocks
    - [ ]  what are these for?
    - optionally compressed like data blocks
    - “stats” metablock contains lots of stats
- meta index block
    - one entry for every other meta block
        - key - meta block name
        - value - BlockHandle pointing to the meta block
- index block
    - one entry for every other data block
        - key - string that is ≥ last key in THAT data block and before the first key in the successive data block
        - value - BlockHandle for that data block
- fixed sized footer
    - BlockHandle of the meta index block
    - BlockHandle of the index block
    - magic number
    - padding too though??
- filter stuff???
    - [ ]  too complicated for now, revisit later

# Specifics

let’s trace stuff

### compaction

### put

1. formulates as a batch
    1. write batch put
        1. sets count, increments by 1
        2. focuses on creating this `rep_`
            - [x]  what does rep even mean? (
                - representation? internal key?
                    - [x]  8+4+1 + length prefixed slice key + length prefixed slice val
                - basically it’s a representation of all the writes and/or deletes that need to be done in just a minimal byte string
            1. sequence: fixed64
                - [ ]  still don’t know what this is for… but I think it’s related to versions
            2. count: fixed32
                - [x]  the number of operations?
                    - yes num operations in the batch
            3. data: record of length count (above)
                1. record
                    - value (varstring varstring)
                        - key, then value are recorded
                    - deletion (varstring)
                        - just key is recorded
                    - NOTE: all the recording is done as `LengthPrefixedSlice` which means there is a [[Varint]] followed by the actual data of the slice
                - [x]  what are varstrings?
                    - variable length followed by the data in bytes
                    - for example, high level 4data or 5dataa or 6dataaa
                        - the number is itself variable length ([[Varint]]), then the data is stored immediately after the number, again a PUT saves both `key and value` whereas a delete is just the `key`
2. actually writes it (”applies specific updates to database”)
    - creates a writer with the updates, gets a lock, puts writer on a queue
        1. temporarily release lock until writer as at front of queue (or it’s somehow done)
            - [ ]  how exactly would it be “somehow done”?
    - make room for write
        - allow_delay is true when there **are** updates in the write
            - [ ]  why would there not be updates?
                - I believe this fn may be called to “force” a compaction
            - delay if L0 is close (8) to having max files (12), 1ms, but only do this max 1 time
            - [ ]  what does this help with?
                - spreads latency around a bit, because once we hit hard limit it delays the write “a few seconds” — that’s a lot, but I guess it’s just how long compaction takes?
            - if enough room in memtable (under 4MB), then return
            - if immutable memtable exists (i.e. previous memtable is being processed)
                - still compacting going on apparently, wait
                - [x]  is imm when memtable is full and ordered and about to be written to disk?
                    - when mem is full and needs to be dumped it is
            - too many L0 files
                - wait
            - otherwise
                - “attempt to switch to a new memtable and trigger compaction of old”
                    - [ ]  asserts prev log number is 0… why?
                - get a handle to a new writable file with a new file number
                    - if this fails, calls `ReuseFileNumber` with the new log number to “avoid chewing through file number space in a tight loop”
                        - [ ]  what does that mean exactly?
                - may trigger compaction
                    - see [[compaction]]
    - get last sequence number
        - [ ]  I still don’t really understand this
    - build batch group (i.e. a `WriteBatch`), see if we can combine any of the other writer’s work in the batch
        - limit size if small
            - [ ]  max size is originally 1MB, but it might be reduced (down to max 260KB) if it’s under 130KB
                - [ ]  what is max size even mean here
                - [ ]  why?
    - rewrite sequence num?
    - unlock, add to log (optionally sync it), then lock again
        - [ ]  why can we unlock?
            - it says because “`&w` is currently responsible for logging and protects against concurrent loggers and concurrent writes into `mem_`"
                - `&w` is a Writer (struct), which requires the mutex to be constructed… so is it saying that anything that touches it uses a lock whenever appropriate?
    - add to log
        - formulates `rep_` as a slice
        - chunks it up into [[block size]] and emits each as an (unsynced) physical record
            - formats header
            - computes [[CRC (cyclic redundancy [[check)]]]]
            - writes it
                - adds it to a buffer if it’s small
                - otherwise it does at least 1 through buffer then unbuffered
                - [ ]  why does it go through this trouble? why not just do the whole thing unbuffered? We’re going to flush the thing anyways…???
            - example this is the log after one write (key=”foo” val=”v1”). this is a full block
            
            ```
            00000000  f1 a9 f7 18 14 00 01 01  00 00 00 00 00 00 00 01  |��.............|
            00000010  00 00 00 01 03 66 6f 6f  02 76 31                 |.....foo.v1|
            ```
            
            - `f1 a9 f7 18 14 00 01`
                - `f1 a9 f7 18` crc checksum
                - `14 00` length (20 bytes)
                - `01` type
            - `01 00 00 00 00 00 00 00 01 00 00 00 01 03 66 6f 6f 02 76 31` (20 bytes)
                - `01 00 00 00 00 00 00 00 01 00 00 00 01`
                    - `01 00 00 00 00 00 00 00` - sequence
                    - `01 00 00 00` - count of items in the batch
                    - `01` - is a write (and not delete)
                - `03 66 6f 6f 02 76 31` - 3 foo 2 v1 basically
    - add to memtable
        - calls iterator (which is just loop with callback) and goes over all writes and deletes
            - each
                - add to mem table
                    - implemented as a [[skip list]], basically a linked list with Ologn search/insert
                    - creates buffer in similar way to how it is on disk with the exception that in between the key and value (uses varlen), there are 8 bytes for the type+sequence (yes, they are combined
                        - [ ]  why is it done like this?
                    - [ ]  why isn’t this protected by mutex?
                        - I believe the reason is that only one thread writes anyways…?
                        - [ ]  where does it create these threads though?
                - increment sequence
                    - [ ]  ??
    - deal with failure, update sequence
        - [ ]  incomplete
    - pop writers off?
        - [ ]  incomplete

### get

1. establishes a lock (?)
2. gets snapshot (if none specified, just gets latest)
3. gets current version
    - [ ]  not really sure what this means?
        - live iterators need a consistent view, so we need versions
            - [ ]  are these similar to snapshots?
4. increase ref counts for both memtables and current version
    1. mem - memtable
    2. imm - (may be null) immutable memtable
    3. current version
        - [ ]  still not sure
5. read file
    1. release lock
    2. lookup
        1. checks mem, then imm, then actual storage (?)