# The Chubby lock service for loosely-coupled distributed systems (2006)

[[chubby-osdi06.pdf]]

- [x]  what is the purpose of a lock service?
    - let separate systems agree on some state
    - limit access to shared resources (files, databases, etc.) to a single machine
    - allow its clients to synchronize their activities and to agree on basic information about their environment
    - primary focus is reliability and availability
    - deal with the problem of electing a leader from a set of otherwise equivalent servers
        - [[Google File System [[(2003)]]]] uses to appoint a GFS master server
    - [[Big Table]] uses it to elect master but ALSO allow master to discover servers it controls and to permit clients to find master
        - interesting usage…
    - store metadata

chubby instance/cell and replicas usually in the same datacenter

interface is similar to a simple file system

before chubby, systems required human intervention

## Distributed Consensus Detour

Split Brain

- when two nodes lose connection to each other and can’t communicate, they both think they are primary
    - solution is to add more nodes. More nodes = less likely that situation happens

Two Phase Commit

Three Phase Commit

MVCC - used by postgres

Saga - (microsoft)

Paxos Agreement [https://www.youtube.com/watch?v=d7nAGI_NZPk](https://www.youtube.com/watch?v=d7nAGI_NZPk)

- majority of nodes come into agreement
- consensus is agreeing on one result
- roles
    - proposers
    - accepters
    - learners
- paxos nodes can take multiple roles (maybe even all)
- paxos nodes must know how many nodes a majority is

PAUSING reading the paper… I need something simpler

[[]]

[https://lamport.azurewebsites.net/pubs/paxos-simple.pdf](https://lamport.azurewebsites.net/pubs/paxos-simple.pdf)

[[]]