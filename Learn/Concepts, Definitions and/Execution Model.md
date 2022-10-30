# Execution Model

mostly from [here](https://en.wikipedia.org/wiki/Execution_model)

the manner in which various units of work are scheduled for execution

C language details part of its execution model that statements end with a semicolon and each one gets executed after the last in sequence. That's just a specification of an execution model — i.e. not an implementation. I guess the implementation is a compiler turning it into a sequence of instructions that execute in sequence by the processor.

- [ ]  Is the compiler the implementation or the executable? It's just semantics at this point but it's interesting...

For C, obviously if statements/while statements can make statements go outside the usual sequence; the sequence isn't static. These dynamic choices would be "implemented inside the language's runtime system, which may be a library [runtime library?] [..] or embedded directly into the executable, such as by inserting branches"

- [[ ]  this is confusing because I really don't understand why runtime library is a thing — it feels like a different usage of the term runtime altogether and I don't know why it's being used here. I feel like the  runtime  in  runtime library  means  available at runtime  which is different from what I think a [Runtime System]]  is (like node). It's kind of like the differences when people talk about OS. It's so broad and vague at some point that I don't know what is actually being discussed.