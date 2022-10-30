# compiler megathread

languages get compiled to assembly for a specific architecture. Assembly is assembled to machine code.

# GNU Project

this is more of an ethos/manifesto by rms promoting free software. if you make an OS free (for example), then it follows that tools built on/for that OS are also free. So the project is loosely "let's deliberately make a bunch of free stuff". GNU's goal originally was to be an OS, but they mainly made tools — it (the kernal) wasn't really "made" until Linus made it independently and it was later licensed under GNU License

# GNU Toolchain

aides in Linux/embedded/etc. development but certain parts can be used with windows/mac/etc

# GCC

can compile a lot of different languages to a lot of different architectures and operating systems

it's a tool on the [[GNU Toolchain]]

It supports various "frontends" like C, C++, Go, etc.

# LLVM

also is a toolchain basically (like above GNU/GCC stuff) but seems more high level. Oddly GCC is more restrictive in licensing. Hardware manufacturers own the part of their code that deals with their stuff. 

# Clang

c language frontend for LLVM (C Parser). it's a little slower but more clear to understand compared to gcc. Chris L looked at gcc as a starting point but wanted to improve. They built it to be more portable/modular and have more tools so they could be leveraged by IDEs in various ways. According to Chris, he wrote a register allocator and someone much smarter came around and made it better — replaced that module. This is really difficult to do in gcc apparently.

# Cuda

allows programmers to directly use the GPU. It's an API. It's more complicated than that, but I think that works for now.

# Compiling process

more around [here](https://youtu.be/yCd3CzGSte8?t=1165), start with high level language and things get "lowered".

→ language → AST → intermediate representations, blocks of straight-line operations (instead of a nested tree) with conditional branches between blocks, like assembly but very language independent 

# Optimizations

- register optimization was an early priority. You might see `int x = 5` but an optimizing may decide how to store that — maybe it's being used so often that it should be loaded into a register instead of read from memory, but maybe there are competing variables that should be stored there... the compiler has to figure that out
- scheduling - moving instructions around so the processor can keep its pipelines full instead of getting blocked

### metrics to optimize for

1. code size - embedded space
2. execution time
3. memory pressure

# Compilation types

- AOT - Ahead of Time - like c/c++, can provide very big improvements but not necessarily some (like PGO below)
- [[JIT Compilation]]  - Just in Time - compiled but not until
    - it has to be - this may be bogus
    - determined to be optimal through profile guided optimization (PGO)
- Interpreted - No compiling really

# object file

- compiler or assembler can generate these object files
    - it's mostly machine code but can contain (external) symbols that are required for it to work. A linker is a tool that looks for these symbols and know how to pull it all together from other object files