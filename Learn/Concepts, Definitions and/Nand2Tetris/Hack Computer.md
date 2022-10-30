# Hack Computer

for nand2tetris course

is von Neumann platform

- CPU that has processing functionality (ALU, registers) and control unit (instruction register and program counter)
- memory for data and instructions
- external storage
- input/output mechanisms

### memory

two different address spaces that are 16-bit wide and have 15-bit addresses

1. instruction memory
2. data memory
- [x]  why only 15-bit addresses? maybe the first bit determines instruction vs. data memory?
    - the first bit in the instruction is used to specify whether the instruction is an A or C instruction (see below)

### registers

only two registers (lol)

A - addresses (and data)

D - data

Because of it being 16-bit with 15-bit addresses, all interaction with memory goes through the A register implicitly. Similarly, if we want to jump to a different place in instruction memory, we need to load A first, then jump next. 

### instructions

These two steps can be referred to as "address instruction" (A-Instruction) and "compute instruction" (C-instruction).

A instructions **start with a 0 bit**. The rest of the bits are the 15-bit address of the memory

- [x]  how does it know if it's loading or storing...?
    - I think it's always storing, the loading is done with C instructions?
        - [ ]  is this right?
- [ ]  can these also be used for static values? like `@5` then on the next line instead of referring to `M` (the value at address in the A register), refer to `A` as a literal value (maybe like `D=D-A`

C instructions are more complicated. They **start with a 1 bit** but then have 2 more 1s for some reason. The other 13 bits are

- **comp** (7 bits) (computation) - instructs ALU what to compute
    - 7 bits allows for 128 different functions but I think only 28 are defined in Hack
    
    ![[/Untitled.png]]
    
    NOTE: it's probably no accident that it lines up with 
    
    ![[/Untitled 1.png]]
    
- **dest** (3 bits) (destination) - where to store the computed value
    - 1 means store it there, 0 means don't store it there
    - A - D - M
    
    ![[/Untitled 2.png]]
    
- **jump** (3 bits) - whether or not to jump
    - [x]  but jump where to?
        - requires that to be loaded into the A register
    - 000 → never jump
    - 111 → always jump
    - 001 → jump if ALU output (from **comp**) is greater than 0
    - etc.
    
    ![[/Untitled 3.png]]
    

### symbols

symbols (like variables?) - refer to memory locations

3 kinds

1. **pre-defined symbols**
    - special subset of RAM addresses can be directly referred to by these pre-defined symbols
        - virtual registers R0 - R15 (addresses 0-15)
            - This closely resembles ARM, which they probably did intentionally. Since the hack CPU only has 2 registers, it's probably convenient to refer to these common memory locations as "virtual registers"
        - predefined pointers - SP, LCL, ARG, THIS, THAT (addresses 0-4 - NOTE: overlap with R0-R4)
        - I/O pointers - SCREEN (0x4000 → 16384), KBD (0x6000 → 24576)
            - NOTE: I think those are starting addresses
2. **label symbols**
    - user-defined goto symbols `(MYLOOP)`
        - MYLOOP refers to the memory location of the next instruction
        - can only be defined once but can be used anywhere (even before it is define)
3. **variable symbols**
    1. user-defined variable whose address starts at 16 (0x0010)

# I/O

two peripheral devices, screen and keyboard

drawing pixels on screen is achieved by writing binary values into a memory segment associated with the screen

listening to keyboard is done by listening to a memory segment associated with the keyboard

these are called memory maps

### Screen

256 rows high x 512 pixels wide? That's 131,072 pieces of information. Since it's black and white, each pixel can be represented with a 1 or 0. If that's the case, then it would take 8,192 16-bit memory registers to hold the contents of the screen at any given time

### Keyboard

whenever you press a button down, it's ascii value shows up in RAM[24576] (also known as KBD)

# Binary Code Files

composed of text lines... really..!?? lol

Each line is a sequence of 1/0 ascii text characters

I guess this is to simulate how "programming a computer" used to work? Like feeding punch cards into a mainframe?

stored as `my_program.hack` or whatever

- [ ]  idea: make a mainframe that can simply process hack instructions?

NOTE: file's nth line is stored in address n of instruction memory

- [x]  what does this really mean though?
    - I think it simply means that it's contiguous. But besides that, it also says that "the count of both program lines and memory addresses starts at 0". I still don't know what that really means. If it starts at memory address 0, then doesn't that override r0?!?!?!?
        - [x]  This is a fundamental misunderstanding I have about computers
            - To clear this up a bit... For the sake of the hack computer described here, the code is executed from ROM which should guarantee that that memory block is completely assigned to one application. Maybe RAM address are after ROM addresses?
                - [ ]  still a little unclear, even for Hack Computer

# Assembly Langage Files

stored like `my_program.asm`

### Assembly Language

A lot already described above. Here are some random bits of information.

- lines in hack assembly that are used to declare symbols do not generate lines of machine code
- constants must be non-negative and always written in decimal notation
- user defined symbols just can't start with a digit... basically...
- comments are `//`
- white space characters are ignored, empty lines ignored
- mnemonics must be uppercase
- variables are case-sensitive, convention is labels uppercase, variable names lowercase

# QUESTIONS

- [ ]  how do address spaces not collide (where is the stack, instructions stored... do they collide with for example R0-R15, etc. or the keyboard location / memory map (whatever that means)
- [ ]  why is the address register and pc on the negative edge of the clock?

# Ending notes

this computer's design is different because it keeps separate spaces for ROM and RAM. Instructions/program counter is a different memory space than the RAM. But in more standard general purpose computers, they are stored in the same space. And fetch/execute is done in two cycles. I was confused initially (may still be a little confused...) because I thought there were 2 or 3 stages (fetch, decode, execute) from reading about this stuff before. But this computer may have been exceptional because they kind of get merged into one tick (or one tick tock?). 

The "downside of doing it this way is that programs cannot be changed dynamically"

- [ ]  why?
    - get a piece of paper and map this out?