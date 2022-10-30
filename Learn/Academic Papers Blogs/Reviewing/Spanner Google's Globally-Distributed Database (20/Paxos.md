# Paxos

watching [https://www.youtube.com/watch?v=s8JqcZtvnsM](https://www.youtube.com/watch?v=s8JqcZtvnsM)

getting computers that can talk to each other to agree on something

majority of nodes in agreement

that video isn’t grounded enough

watching this instead [https://www.youtube.com/watch?v=tw3gsBms-f8](https://www.youtube.com/watch?v=tw3gsBms-f8)

### The Consensus Problem

1. multiple clients can send requests to a system
2. the system must choose which to handle next
3. the system is implemented by multiple computers (distributed)
4. they must choose a single request even if some computers fail
    - [x]  what does “choose a single request mean” — to process next?
        - yes, and this is what paxos does

Abstracting it…

forget about clients and requests, instead just think of choosing values, so we can move into a mathematical domain

Paxos is efficient but correct mainly

### Mathematical Model

execution of the system is represented by a **behavior**

**behavior ****is a sequence of **states**

a **state** is a [particular] assignment of values of variables

stopping at 14:37

resuming briefly

**Initial** Formula - all possible first states

**Next-State** Formula - given a state, all possible *next* states

**Initial**

Initially no value is chosen (chosen set is empty)

to be continued…