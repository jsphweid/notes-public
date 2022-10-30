# ARM Assembly

assembly for ARM processors (RISC ISA)

This will be 32-bit.

Each arm instruction is basically 32 bits wide.

ARM mode and Thumb mode

- thumb mode means it allows thumb instructions which are 16 bits wide as opposed to 32 bits. This could be potentially faster if your "code is smaller and target has slow memory"

# instruction

general formula is:

`MNEMONIC{S}{condition} {Rd}, Operand1, Operand2`

### harder things

Operand2 is someone flexible because it can be used like:

- literal value (like `#5` which is a literal int 5)
- data reference? (from memory, probably resolves to a memory address? like `=somestr`)
- values in other registers potentially? (probably directly like `r3`)

conditions, linked to [[cpsr]]

# registers

r0-r12 - general purpose

r7 - holds syscall number

r13 - stack pointer (sp) (stores functions??)

r14 - link register - when a function gets called, it stores the *next* location of memory from where the function was initiated from

- honestly I was kind of thinking this was what r13 did...

r15 - program counter (pc) - incremented by the size of the instruction executed (32 bits except 16 bits in thumb mode) - it's always pointing to the instruction 2 instructions away... (x86 is always the next instruction)

- [x]  I wonder why this is
    - I think it has to do with how it was originally designed and is somehow still in here... see [here](https://stackoverflow.com/a/24092329/4918389). But I don't really understand it other than, pipelines were simpler back then and this was somehow useful but today it's much more complicated and this is basically potentially meaningless...

# mnemonics

### mov

basic usage is `mov dest value`

### swi

software interrupt see [[making syscalls]]

### sub

subtract without carry

# making syscalls

actually, this is a mechanism for applications to call OS routines

it seems the actual instruction that's going to be called is on r7, and arguments will be on other registers

# directives

- [ ]  are these really "directives"..?

- `.text` - it's where all the code goes. has a label (like `.data`)
- `.global` - help it find the start of the program and may give the program external linkage (in simple single file single execution scripts may not be necessary..?)
- `.data` - there is a label like `myvar:` then a type like `.asciz` (which means ascii with null terminated string... I think), then the value of the thing.

# other useful things

# - pound sign is a byte offset? or perhaps a literal. According to [this](http://kerseykyle.com/articles/ARM-assembly-hello-world), it's a literal

[ ] - get the value of something... inside is likely a register with an address in it

@ - single line comment

/**/ - block comment

# mov vs. ldr

are similar, but `mov` can save an instruction if you inline a value? like `mov r0 #1`

# debugging

you can debug with `gdb`

# printing to the console

[https://peterdn.com/post/2019/02/03/hello-world-in-arm-assembly/](https://peterdn.com/post/2019/02/03/hello-world-in-arm-assembly/)

a print is executed through a syscall

some useful info for what value r0 should be probably [here](https://stackoverflow.com/questions/12902627/the-difference-between-stdout-and-stdout-fileno)

# CPSR (current program status register)

holds status via 4 bits

# word

32-bit words are used in a 32-bit microprocessor

each of the units is a word

# weird

to deal with weird size constraint issues, the assembler sometimes (? or all the time?) transforms certain literal values into a position/value (with a rotation concept)

- [ ]  maybe investigate this more
    - I feel like I have read a lot about it but there aren't enough examples and clear explanations to make it more obvious to me