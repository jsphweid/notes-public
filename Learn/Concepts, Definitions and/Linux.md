# Linux

*free UNIX*

embraces unix "everything is a file" (EXCEPTION - network devices)

- block files - device file - randomly accessible
- character files - device file - serial stream for input/output
- directory files
- regular files
- more...

### Linux Modules

insert module - `insmod`

remove module - `rmmod`

## Drivers

1. can be statically built into the kernel on disk
2. can be inserted as module at runtime
- [ ]  can you choose which one when you compile? or are they written a certain way?

generally it's a part of the OS when you install the OS, in fact, if you look at the massive codebase, most (literally) is about drivers