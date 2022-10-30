# Hack VM

Virtual Machines

VM idea was reinvigorated with Java/C#, but it's an old idea.

VMs can be implemented different ways, for example:

- software interpreters
- special purpose hardware
- translating VM programs into machine language on target platform

VM gives access to common libraries which may be almost considered an operating system. Provides languages unified services like memory management, GUI Utilities, string functions, etc.

It seems close to this IR (Intermediate Representation) concept although I'm not sure where exactly the lines are drawn just quite yet.

Hack VM is modeled after the JVM.

Without a VM (or similar concept), you need a separate full blown compiler for each language/machine language pair.

### Benefits of VMs

- by breaking it into two stages, when you need to support a new platform, you only have to change the virtual machine implementation (BE)
    - [ ]  NOTE: if BE is virtual machine implementation, what is FE
- since languages can compile to the same VM, you can get code interoperability (say a function in one language can call a function in another language — using an agreed upon syntax, of course)
    - [ ]  I would love to see an example of this
- efficiency improvements to the VM benefit all the languages that use it

# Part 1

VM Translator

- will be able to translate VM arithmetic and memory access to Hack Assembly (or machine code directly? not sure yet)

"There are several possible software paradigms on which to base such a language implementation. One of the key questions regarding this choice is where will the operands and the results of the VM operations reside?"

- [ ]  What does this even mean?

Basically, arithmetic and boolean expressions can all be converted into a series of stack commands. It seems this can be implemented in raw assembly perfectly fine. So I'm not immediately sure why we have to start using this data structure. Let's go along with it for now...

VM files are `*.vm` where each line is a vm command (similar to asm that we built, honestly)

### arithmetic and logic commands

![[/Untitled.png]]

### memory access commands

push/pop

There are 8 separate *memory segments* although I'm not immediately sure what that means. Segments seems to be different stacks? So like 8 different stacks to push/pop in? Probably not.

I feel like they introduced this a bit too soon. Not sure what's going on.

Actually, the stacks are initialized when a function runs. It's like various memory locations for when functions run?

 

![[/Untitled 1.png]]

VM commands like `push argument 2` or `pop local 1` have the structure

- *push/pop* *[segment] [index]*
    - push/pop - simple, either one or the other
    - segment - can refer to any of the ones above in the list
    - index - a non-negative number
- [ ]  how do those two commands above "store the value of the function's third argument in the function's second local variable"
    - It pushes the third argument... WHERE?

manages a stack/heap somehow... lol it's going quick!

### program flow and function calling commands

6 more commands

- program flow commands
    - label - declares a label like `label something`
    - goto - unconditional jump like `goto something`
    - if-goto - conditional, not exactly sure how it works yet though
- function calling commands
    - function - declaration, also specifies number of locals like `function myFunc 5`
    - call - invoke a function, specifying a number of args... like `call myFunc 3`
        - [ ]  but what are the values of those args...?
    - return - transfer control back to the calling function

### program elements in the Jack-VM-Hack Platform

jack is basically like Java — high level language that we're going to build

VM Translator is applied to a directory of .vm files and generates a single assembly program.

"This assembly program does two main things. First, it emulates the virtual memory segments of each VM function and file, as well as the implicit stack. Second, it effects the VM commands on the target platform. This is done by manipulating the emulated VM data structures using machine language instructions—those translated from the VM commands. If all works well, that is, if the compiler and the VM translator and the assembler are implemented correctly, the target platform will end up effecting the behavior mandated by the original Jack program."

- [ ]  I don't know what any of this means. Are we talking about any given program or a specific one? I didn't write an assembly program that emulates virtual memory segments, but instead does raw simple arithmetic/memory operations. I guess that's what we're doing to do next?

Seems like we're focusing on the next chapters too much. 

### VM Standards

regarding the mapping of VM → target platform, the *standard mapping* is a guideline for getting this done (I know, it's vague for now). Why?

- public contract that regulates how VM-based programs (like a java program) interact with programs produced by compilers that don't use that VM (like a C program)
- standardized tests - tests that conform to the standard mapping

- [ ]  I'm not entirely sure where the lines of this formality work or what it is really saying. Is it saying, "engineer the VM wisely" or is there some idea of "standard mapping as it relates to other VMs" (like other VMs share the same guidelines? or more generally that there is a good way of going about this)

### RAM

I'm starting to get confused on R0-R15 (some of these addresses go by different names as well, `this` `that` `sp` etc.). I don't understand why they overlap. Seems like they should be separate. In hack assembly, we were using r1, r2, etc. just willy nilly, but they seem like they're going to have a dedicated purpose going forward. Also, I know they are called "virtual registers" but they aren't registers at all (hack computer only has two registers implemented as circuits, A and D). Not sure what the point of referring to them as register-like is.

![[/Untitled 2.png]]

These locations in memory really just point to other places. They store the pointer to a block of contiguous information called a segment (or at least it appears that way)

## building this thing...

stage 1

- 9 stack arithmetic and logic commands
    - add/sub are easy since our ALU provides direct operations for them (`M+D` for example), but the others, not, and, lt, gt, etc. aren't as immediately obvious to me
    - solving `eq` `lt` `gt`
        - I don't think it's possible to use jumping because you need to be able to return to the instruction you left off at, and that doesn't seem to be possible without having access to the program counter (which I don't think you get with hack assembly). The trouble is: without jumping, I don't know of a better way — using the table of 28 computations, I don't think it's possible to achieve.
        - so I looked at a few examples from the internet and they both did what I had originally thought of which was making a unique label to represent the current position and then go back
- push constant x (should help testing the other commands)

stage 2

- full push/pop implementation, handle all 8 memory segments
    1. constant segment already handled
    2. handle `local` `argument` `this` `that`
        1. what do these MEAN!? they are just dedicated places to store stuff
    3. handle `pointer` `temp` (allow modification of the bases of the `this` and `that`
    4. handle `static`

- [ ]  Another big question I have is... why is the VM (or "this" VM) stack-based. Are there non-stack based VMs?
    - maybe it's because stack based is the best way to do all these things so we implement it at the first layer of abstraction that we can? (right above assembly)
    - it's generic and extremely minimal and just works?
    - the other popular one seems to be register-based. In register processing, operands for operations are stored in registers and the registers are referred to in the instruction. Which is honestly how assembly works, right? Obviously the number of registers is highly system-dependent, so writing solutions around that might be more optimal but less portable. Stack processing seems very portable because you don't need to make a lot of assumptions about the hardware architecture. Operands are referred to by a single pointer (the stack pointer) as it moves back and forth.
    
- [ ]  Why is this/that mapped to locations 3-4 on hack ram... but location 0 and 1 also point to those...??? why are they even separate?

# Program Control

the more a language is capable of abstractions, the more low level work must be done to manage it

### terms

**subroutine**, **function** - basically the same thing? subroutine maybe has no return? (maybe should be called **procedure**)

**co-routine** - a function with yield basically... picks up where last execution left off in a way

When executing a function, there is a surprising amount of bookkeeping that needs to be done, like:

- passing parameters from the caller to the called subroutine
- saving state of the caller before switching to execution of the subroutine
- creating space for the local variables in the subroutine
- jumping to execute the subroutine
- returning values from the subroutine to the caller
- recycling memory after it returns
- reinstating the state of the caller
- pick up where it left off
- [ ]  is this why recursion is slower but more elegant sometimes? Because all of this bookkeeping has to be done for every recursion loop

frame - all memory segments that support a function's operation

- they are stacked on each other on the stack

"At the VM level, all functions in all files are seen by each other and may call each other using the function name" 

- [ ]  is this a hack vm thing?

Here's how a function gets called:

1. caller pushes all arguments to stack
2. caller invokes `call`
    - when it's called, the function
        - sees the arguments that were pushed
        - but `local` variables has been allocated and initialized to 0s.
        - `static` sees whatever file it's in. the working stack it sees is empty
            - [ ]  what does this mean...
        - `this` `that` `pointer` `temp` are all empty
    - before returning, it should push a value onto the stack (presumably the return value)
3. when it returns, arguments pushed to stack have disappeared and all that remains is the return value
    - [ ]  says "that always exists"... wtf does that mean
4. caller's memory segments — argument, local, this, that, static, pointer — remain as they were before and temp segment is undefined

At this point, I can't clearly visualize how all the stacks/segments work together... hoping it will be more clear as I go along

Here's a decent drawing 

![[/Untitled 3.png]]

# VM Code, a short story

```wasm
function main
	push constant 4 // push arg
	call fact 1 // transfer execution to fact, 1 is probably the number of args?

function fact 2 // declare function called fac with 2 local variables
	push constant 1 // get a 1
	pop local 0 // store =result variable with a 1
	push constant 1 // get a(nother) 1
	pop local 1 // store a 2nd local var in location 1, j=1
label loop // basic loop is eval whether to go on, then multiply if you make it that far
	push constant 1 // get a 1
	push local 1 // pushes the value of local 1 to the stack
	add // i.e. j+1
	pop local 1 // now assign... j=j+1
	push local 1 // put it back? (but it's still stored in the previous place?)
	push argument 0 // put the arg that was passed in on the stack (does it need to be put back?)
	gt // eval last two (local 1, i.e. j, argument 0, i.e. 4)
	if-goto end // if the last operation was true... i.e. when 5 > 4, then go to end label below
	push local 0 // this is the =result number
	push local 1 // iteration number
	call mult 2 // 2 args (right above, of course)
	pop local 0 // so it puts the result on top of the stack, and this puts that value back to local 0 (=result)
	goto loop // start loop over
label end
	push local 0 // push this to the top of the stack and return

=========================================================

say 3*4
function mult 2 // function with symbol mult that has 2 local vars.. (where are args accounted for)
	push constant 0 // start with 0 for some reason
	pop local 0 // store that 0 in local 0, probably for (sum)
	push argument 1 // get the 2nd arg (4)
	pop local 1 // put 2nd arg in local 1
label loop // define label to eventually jump to
	push constant 0 // start with 0 again... to compare in a sec
	push local 1 // get that 2nd arg (4 initially...)
	Eq // see if 0 == 2nd arg
	if-goto end // if they are equal... end
	push local 0 // get 1st local var (sum), initially 0
	push argument 0 // get 1st arg (3 initially)
	Add // and 1st local 0 (which is initially 0) to 1st arg (3)
	pop local 0 // store it back in the (sum)
	push local 1 // put up 2nd arg (4 initially)
	push constant 1 // a 1
	Sub // decrement essentially
	pop local 1 // put back in local 1 (i)
	goto loop
label end
	push local 0
	return
```

# First pass at doing ch. 8

(just realized how disorganized this is...)

We need to define the function somewhere. The test script doesn't even call it though... How does this thing even execute...

We just need to focus on defining it. All we really need to implement is the `function` and `return`

# Variables and what they are used for

pointer

# Final Questions

Even after doing this I'm not exactly sure