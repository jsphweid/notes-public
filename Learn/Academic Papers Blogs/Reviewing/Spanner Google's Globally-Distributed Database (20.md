# Spanner: Google's Globally-Distributed Database (2012)

[[65b514eda12d025585183a641b5a9e096a3c4be5.pdf]]

*semi-relational, replicated, query language, general transactions, single instance over multiple datacenters*

created in response to popularity of Megastore, 

globally distributed database, mainly focused on managing cross-datacenter replicated data

first customer was F1 - Google’s advertising backend

- originally used sharded mysql but every reshard took years to complete

applications can control the nature of the replication

assigns **globally** meaningful commit timestamps to transactions

- uses TrueTime API
    - .now() fn returns [earliest, latest] as opposed to a single timestamp, generally small uncertainty
    - after(t) - returns true if t has definitely passed
    - before(t) - returns true if t has definitely not arrived
    - [ ]  but why is all this necessary?
        - reading [http://www.bailis.org/blog/linearizability-versus-serializability/](http://www.bailis.org/blog/linearizability-versus-serializability/)
            - Linearizability == atomic consistency
                - writes should appear to be instantaneous
                    - if a write happens, then reads, reads should reflect that write
            - Serializability
                - [ ]  i don’t really understand this
                    - says it is “Isolation” in ACID, reading wikipedia
                        - lower level isolation means many people can access at once, but bad stuff could happen (dirty reads, i.e. reading uncommitted transaction on objects, and other things)
                        - higher level isolation require more resources / blocking
                        - it’s all about **when do changes made by one operation become visible to others**
                    - wikipedia doesn’t help me understand this article really… it’s something about order
            - final thoughts on this for now…
                - if you have T1 and T2 where T1 is a write then T2 is a read that comes *during*, we could have T1 → T2, or T2 → T1, but if it’s strict, then T2 will have to come after T1 (even if T1 takes longer to commit? because it was started earlier)? I think….
        - keeping track of uncertainty is necessary for correctness while keeping the band of uncertainty small is necessary for performance. (it’s generally smaller than 10ms)
        - they have atomic clocks and gps in datacenters running this truetime service
        - ????

## Implementation

**directory** - unit of data movement

**universe** - spanner deployment

- very small number of these… basically alpha/beta/prod?

**zones** - similar to a cluster of bigtable servers? could be multiple per datacenter

- unit of physical isolation
    - [ ]  like the “Isolation” above?
- has zonemaster and 100-1000s of zoneservers

placement driver - organizes movement of data across zones

### spanserver

***EACH***  is responsible for 100-1000 instances of a data structure called a ***tablet***

- similar to bigtable tablets
    - bag of mappings `(key: string, timestamp: string) → string`
    - says it assigns timestamps to data *unlike* Bigtable… I thought bigtable uses timestamps
- uses Colossus (which replaced GFS in 2010)
- uses standard db files Btree-like, WAL

I need to really understand Paxos…

[[Paxos]]

Don’t really understand Paxos yet but continuing to read the paper for now

paxos + lock table provide transactionality, but when a transactions occasionally involves more than 1 Paxos Group (set of replicas, presumably spanservers?), then a Transaction Manager is used. My impression of what this is is basically Paxos on top of Paxos?

### directories (buckets)

when keys in the bag of key-value mappings have a similar prefix

controls the data placement, and allows an application to optimize

high level Spanner operations might move these directories around to be closer to requestor or to put things in the same Paxos Group

smallest unit whose geographic-replication properties (i.e. *placement*) can be specified by the application

directories are actually sharded though

### aside

this semi-relational db is interesting… in the table definitions you have to specify things like “INTERLEAVE IN” which describes the locality of the data, and informs spanner how to collocate the data

![Untitled](Spanner%20Google's%20Globally-Distributed%20Database%20(20/Untitled.png)