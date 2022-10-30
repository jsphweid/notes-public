# cores vs. threads vs. processes

physical cores are like separate machines on the CPU. They all operate at the same time processing a queue of instructions. Those queues are threads. A single core may be listening to many different threads at once in a way but only processing one at a time. It switches between theme strategically.

multi-process is splitting the execution environment for your program. Threads are similar but it's splitting less, it's just splitting where it is in the code. 

- [ ]  what exactly is not being split in threads that is being split in processes
    - processes have separate memory spaces

if you're running multi-threaded, you can often run into problems with shared memory. You may need to introduce some locking mechanism

reading [this](https://towardsdatascience.com/multithreading-vs-multiprocessing-in-python-3afeb73e105f)

### Concurrency vs. Parallelism

Concurrency - two or more tasks are *progressing* at the same time

Parallelism - two or more jobs are literally executing simultaneously

### Multithreading vs. Multiprocessing

multithreading - for i/o intensive tasks

multiprocessing - for CPU intensive tasks (if you have multiple cores)

watching [this](https://www.youtube.com/watch?v=KVKufdTphKs)

Multithreaded applications can have all sorts of problems with shared state. Locks are a common solution. Without this lock, you can have race conditions when you multi-thread. In particular, reference counting can get mixed up such that you suddenly have more or less references than you 'should' have. This means that an object in memory may never get freed or get freed too soon. Both of these are bad. That's why having 1 or more "locks" to hold to get access to certain things is necessary.

Deadlocks are when you have multiple threads trying to acquire the same locks but they are both waiting on each other.

Python has a SINGLE Global Interpreter Lock. GIL. This lock gives you "access" to the python interpreter. That means only one thread can access the interpreter of a time. For IO this is fine, but for CPU bound tasks it's not, because it effectively makes your program single-threaded.

- [x]  what does "access to python interpreter" mean?
    - access to python objects
    - changing reference counts
    - the python interpreter, is it kind of like the node event loop?

python extensions and what not *drop the GIL* when they are making OS calls (writing/reading file/socket/etc.) and then reacquiring it after. This is the space where another thread that needs the GIL can operate.

Apparently there was a bug in GIL code that rarely released the GIL, but it was patched in like 3.2 or something.