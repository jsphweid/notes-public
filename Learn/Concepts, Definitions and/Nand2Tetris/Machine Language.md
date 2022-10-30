# Machine Language

mostly from chapter 4: nand2tetris

where hardware meets software

focus on these things

1. processor
    - i.e. CPU, does logic and arithmetic operations on these "words" described below
    - uses either registers or RAM (depends on arch) as a source and destination for these
2. memory
    - "words" at addresses
        - **word** is a unit of data
            - width is commonly 32-bit or 64-bit these days
3. registers
    - since memory addresses themselves can be 32 or 64 bit, this can create long instructions for CPU. Also it's further away.
    - registers are closer and simpler to describe, so they are just faster plainly
    

### machine code example

four 4-bit fields could comprise a single instruction on a 32 bit computer as an example

it would look like 0100 1100 1001 1101, which may mean `set R3 R1+R9` just depends on the hardware

set in this case would just be a mnemonic, just a stand-in for 0100 in this case.

### ways of accessing memory in assembly

aside: I have a bit of trouble understanding how a whole address (32 bit) can fit in a 32 bit instruction, since there are other things in the instruction most likely. Guess an instruction can be bigger than the word size? We'll find out!

1. direct addressing
    - express the address or a symbol that means the address
        - [ ]  how would this look in ARM assembly?
2. immediate addressing
    - stuff that is inlined into the instruction code
        - [ ]  why does n2t even put this in "addressing memory" maybe because a program's instructions are kept on the stack, which is memory? but when you inline it, you don't really have to worry about it...?
3. indirect addressing
    - a pointer to a pointer?
    - probably more commonly, an array with an index, which is translated as an array pointer with an index offset

### branching

jump somewhere that isn't the next line, basically

- if, then etc.
- jump to subroutine (different label)
- loops

often conditional jumps (jumping while factoring in a boolean value) are part of a command, but in other languages it's a part of the previous command

- I feel like I've seen the whole "previous command" pattern in ARM