# Runtime System

like v8/node/etc.

- [ ]  do REPLs fit into that category

"implements portions of an execution model" - [[Execution Model]] 

What makes runtime systems hard to understand is that there doesn't seem to be a baseline commitment to what it provides for every language. Each language has a different form of runtime system that provides a range of features from the language's execution model.

*typically* it involves managing the stack and heap, maybe garbage collection, threads, etc.

This makes me think in C, the runtime system is often the OS (or maybe that's runtime environment)

"The runtime system of the C language is a particular set of instructions inserted by the compiler into the executable image" which manage the process stack (?), create space for local vars (?), and copy function parameters onto the top of the stack

Another definition I like: "any behavior not directly attributable to the program itself"