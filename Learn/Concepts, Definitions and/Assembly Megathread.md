# Assembly Megathread

language that is very low level... compiles directly to computer instructions

I'm not going to organize this document. Everything is going to be in the timeline that I learned it more or less...

- [x]  how portable?
    - not very, seems like you're writing for a particular CPU in mind
        - [ ]  is this 100% true?
            - probably not as different CPUs can probably fall under the same type... like x86?
- how does compilation happen?
    - using a utility program

## instruction set architectures (ISAs)

[https://www.youtube.com/watch?v=NNgdcn4Ux1k](https://www.youtube.com/watch?v=NNgdcn4Ux1k)

An instruction set architecture is an abstract model, a CPU is an *implementation*

This abstract model, or interface, is the contract between software and hardware

ISAs are how software talks to hardware

- [ ]  So in a way, you can swap out talking about ISA and CPU?

### types of ISAs

RISC-V, ARM - based on RISC (reduced instruction set computer)

x86 - based on CISC (complex instruction set computer)

Most are proprietary (x86, ARM), but 10 years ago, an open source one came along (RISC-V)

Apple is transitioning away from x86 to go to ARM

So when Chris Sawyer wrote Roller Coaster Tycoon 99% in x86 assembly, he was targeting a specific ISAs which (presumably) any computer that had a CPU that implemented that architecture could run.

CISC seems like it does more for you, RISC is more manual because the processor knows how to do fewer things ("reduced"). Since CISC does more, the code size is less since the processor will know complex operations (not just add/multiply/etc, but things like polynomial divide, sort list, etc.). RISC only interacts with memory through read/store operations, CISC interacts with memory much more intimately and automatically, it seems.

### Why we settled on CISC in the 80s originally

Sounds like the reason we settled originally on CISC was it made it easier to write assembly, because people were still writing assembly. OS's were written in assembly until Unix, which was written in C

- [ ]  confirm this?

C allowed the instruction set to be hidden from the programmer, so the compiler could write the simple instructions

Intel cleverly translated complex instructions (from compiler) to simple instructions to take advantages of RISC ideas. Intel profited hugely from this PC era boom.

### Where does PowerPC come in?

Seems like ARM, just another proprietary RISC ISA.

### Why RISC is (probably) better

in general, more instructions run, but overall it's faster because it takes fewer cycles to run an instruction

The benefit seems mostly around the fixed clock size

- [ ]  need to learn more about clock cycles/sizes/etc.
    - [https://www.youtube.com/watch?v=3PcO10iAXTk](https://www.youtube.com/watch?v=3PcO10iAXTk)
        - a cycle is a single electrical pulse in a CPU
        - can do a basic task (accessing/writing data to memory, etc)
    - [https://www.youtube.com/watch?v=Z5JC9Ve1sfI](https://www.youtube.com/watch?v=Z5JC9Ve1sfI)
        - fetch/decode/execute - one thing per tick? really?
        - registers - like memory but on the actual CPU, stuff that it needs to do the job that it's doing right now
    - [https://www.youtube.com/watch?v=gLsdS0zQ82c](https://www.youtube.com/watch?v=gLsdS0zQ82c)
        - 4th stage is write-back?
        - he describes the 4 stages as 1 instruction. so 4 clock cycles per instruction (back then)
        - but then they evolved to have a pipeline where there was something at each stage at each cycle, so there is overlap like ford mass production, something new coming off the line every cycle. THIS IS A PIPELINE. The length is known as *pipeline depth*
        - you can even split up a stage into smaller stages and grow the pipeline
        - can have extra circuitry to process non-dependent operations in parallel (known as pipeline *width*), but takes more space/power

### Metrics

how do you measure? (ISA/CPU?)

how long does it take a program to run

1. how many instructions did it execute
2. how long did each instruction take to run
    - 3.1Ghz or whatever - speed of the clock
        - 2.5Ghz, 4 nano seconds (actually I think it's 0.4 ns)

3. how many clock cycles per instruction

That's what he named from the video, but it really seems like it should be 2, not 3. 3 is just 2 part 

# How it works so far (big picture)

C **compiles** code and translates it into **assembly language** (instructions). Each ISA (x86, ARM, RISC-V) has their own instructions required for that instruction set.

- [ ]  who makes the compilers?

- [ ]  how does this fit into other parts of the computer? ASIC?

# Compilers

[f](https://www.youtube.com/watch?v=lXdx0X2WHfY)rom [here](https://www.youtube.com/watch?v=lXdx0X2WHfY)

> Compilers do two things; they represent things and they transform things
> 
- [ ]  as Moore's law ends, gains will still be made in other ways, like custom accelerators...?
- [ ]  the way he talks about (8:30ish in) "We'll be the best implementers" sounds similar to how geohot talks about "commai will always be the best implementers of this open source idea" (not sure where the video of it is, but I think he said something like this). It's just interesting model... Like how can you guarantee that?

- [ ]  Asked Embedded guy Brian questions about the types of Instruction Sets he uses

CISC is basically dead except for Intel

The future thought with open source RISC is you get one standard instruction set and since licensing is not restrictive, you will get lots of different kinds of optimized chips/silicone implementing that ISA.

# Which to learn...

### RISC-V

If I want to learn RISC-V, I'm going to need an emulator or an actual raspberry-pi-like device that runs on the RISC-V instruction set... not sure those exist.

### x86

This would be the easiest. It's the most ubiquitous and runs on my macbook pro

### ARM

This would be fairly easy to run on a raspberry-pi or new M1 Macbook

I think for now, it makes sense to go with ARM. 

# Verilog

text representation of digital circuits (not really a programming language)

watching [https://www.youtube.com/watch?v=q1QwC3YlHG0](https://www.youtube.com/watch?v=q1QwC3YlHG0)

- seems kind of like terraform?
- seems declarative
- order doesn't matter

but why? for testing?

can be used to simulate

# Assembly

different from languages because assembly is just really a stand-in for straight machine code. We call various instructions "mnemonics" — they're not a higher