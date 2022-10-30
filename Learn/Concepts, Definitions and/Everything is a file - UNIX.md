# "Everything is a file" - UNIX

watching this to understand the [philosophy](https://www.youtube.com/watch?v=dDwXnB6XeiA) more

[everything is "just a stream of bytes"](https://yarchive.net/comp/linux/everything_is_file.html) - linus

["If you can read on it, it's a file."](https://yarchive.net/comp/linux/everything_is_file.html) - also linus

### exercise

start up vim in the background like `vim &`, note the number.... then go to `/proc/{the_num}`... it's a whole directory full of stuff talking about the process

- [x]  Isn't it slow to have everything as a file (like a running program) since it puts stuff on disk?
    - [x]  or is part of the linux os (in this case) not running on disk somehow?
        - apparently [proc](https://unix.stackexchange.com/a/203951) doesn't reside on disk....... NICE

### file descriptors

- [x]  what is it
    - every time a file is opened, an int is added and you're given a number which is a handle to the file. The OS keeps track of that number and relates it to your opened file (through a pointer?)
        - [ ]  is this number the same as proc number?
    - if you close the file, the file descriptor / number is removed
    - [ ]  why don't you just have an address
        - an int is more opaque? I have no idea really
    - **you'll need it to make future calls to kernel space... it's like an ID**