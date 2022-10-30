# think about all the things I've learned and how it might relate to this project

Status: Not started

- verilog is an HDL that represents black box 'functions' more or less as "modules" — you can hook up inputs/outputs... what if this did something similar? Or what if we could define each function once and generate everything from there>...!?
- LLVM is like an ecosystem / "infrastructure technology" (around [here](https://youtu.be/yCd3CzGSte8?t=1886)) that can be leveraged by people for uses that it wasn't originally designed for.
    - it's very modular.
        - He could write a register allocator (for example) and someone much smarter than him could come along and write something better without it affecting too much. That's actually quite important — understand the thing well enough to know how it fits together but don't worry too much about optimizing the hell out of it — just make it easier for smarter people to do that.
        - Hardware manufacturers own the part of their code that deals with their stuff (it would be nice if model owners could do the same with this idea)
    - work with good people - Chris Lattner was always working with great people
- functions everywhere
    - syscalls are just functions to a service at the os level. if you want to print something to the console,
- Lex fridmen chris lattner no 2 towards end talking about software 2.0. That’s pretty much what I want to build
-