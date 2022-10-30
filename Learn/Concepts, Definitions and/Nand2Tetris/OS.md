# OS

The Jack OS is more like a standard library for Jack that an OS. It's a pretty loosely used term it seems... kind of like VM.

Unlike other OS's, this OS is aware of its hardware platform

## memory

different variables are allocated at different times

static variables may be allocated at compile time

local variables are allocated on the stack each time a subroutine begins running

for objects/arrays whose size can only be determined at runtime, it's not allocated until runtime via the heap — the OS helps with this

c++, Jack, etc. don't have garbage collection and so it's the programmer's (not the language runtime) responsibility to handle it

### memory allocation algorithm

imagine a linked list where each node represented a segment of memory

- that's already kind of weird since don't we start with 1 big segment of unallocated memory?

each segment contains a pointer to the next segment and the length of this segment

- [0:10] where 0th is segment length, 1st is pointer to next segment

when asked for a block of memory of a certain size, there are two simple algorithms: *best fit* and *first fit*

- best fit - finds one large enough with smallest waste
- first fit - finds first one that is large enough (who cares about the waste)

once it finds a suitable block (or segment?), I'm assuming it is plucked from the linked list, if there is a lot of waste, it can cut off what it needs and reattach the remainder in the same spot (probably, create a new segment?)

then when it is returned, it's put at the end

The problem with this is after a while you have a lot of smaller blocks not in contiguous order, so a defrag operation is periodically needed — it can be done when there is not a large enough segment, or every time an object is de-allocated, whatever

With lists/str/etc things that can change in size, usually a maximum amount is stored. Even if the string shortens, it still has that full segment reserved

### input/output

handled by OS via device drivers (screen, keyboard, etc.)

raster graphics means pixels (as opposed to vector graphics) — each pixel is a number or group of numbers

raster scanning is left to right on down the page

in hack, a memory map is used

- [ ]  how do other computer systems use this?

drawing characters on a screen — it's a bitch and makes you appreciate how rich computers are with features... Basically every character gets a bitmap (set of pixels) that represent each character and when it needs to be displayed (on hack platform), then the contents of that bitmap are mapped onto memory

### real OS

multi-threading and multi-processing

storage

CLI / UI

security

communication

user code vs. OS code

- OS code is privileged

# Writing an OS in C

[This post](https://stackoverflow.com/questions/1096682/what-kind-of-c-is-an-operating-system-written-in) covers an interesting topic — how do you write an OS in C if many parts of C seemingly *depend* on OS? For example, `malloc` calls the OS, but when you're writing an OS in C, can you just not use that feature?

Answer: basically a lot of those C standard library functions are simply unusable when you're writing an OS