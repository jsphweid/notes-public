# brief C primer

C standard lib is implemented by each OS? or OS is responsible for some part of it? 

POSIX C library is a superset of the C lib. I get confused. Who is responsible for malloc?

static functions are not visible outside of the file (you can think *private*)

char literal uses single quotes

printf - %s → string, %c → char

`const` means variable is read-only

static allocation

- neither auto allocated on stack or dynamically allocated on heap
- static keyword is not necessary
- declared outside function body
- stored in [https://en.wikipedia.org/wiki/.bss](https://en.wikipedia.org/wiki/.bss)
    - it's kind of like stuff in .data but it's uninitialized

the `->` is for getting an item off `some_struct` when some_struct is a pointer to a struct, else use `.` like other languages it seems

C is pass by value... if you want a function to change things on a struct for example, you're going to have to pass a pointer to the function and use `->`'s

- [ ]  what does `return ~0;` really do?
- [ ]  what's the point of declaring a static var inside of a function?
- [ ]  when should you generally use signed/unsigned