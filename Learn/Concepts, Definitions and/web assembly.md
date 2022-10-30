# web assembly

portable binary-code

a standard (not an implementation)

think how x86/arm/etc assembly targets specific hardware devices — well the web VM can be thought of as another environment. Instead of compiling general code to a x86/arm assembly, it can be compiled to web assembly where it can run in a browser (for example) running with any hardware architecture 

emscripten uses LLVM/Clang (see [[compiler megathread]]) to compile C/C++ to web assembly. webassembly is a compilation target / backend 

wasm is a virtual instruction set architecture

each runtime environment has a different set of APIs for interacting with it

wasm itself doesn't allow any "ambient" access to the host — but it's possible through the "embedder"

- [ ]  what is embedder

### some concepts

functions - pretty much standard function stuff

tables - array of values with a particular type, but only allows functions currently?

linear memory - contiguous mutable array of raw bytes

modules - contains definitions for functions, tables, linear memory

embedder - something about how it embeds into host environment

### phases

decoding - decodes binary into internal web assembly module format

validation - makes sure the module is meaningful and safe, performs some (?) type checking

execution 

- instantiation - modules *instances* have their own state and execution stack (??), also it initializes globals, memories, tables, gives definitions to imports, invokes modules start function if defined
- invocation - invokes a specific function in a module

### stack machine

WASM execution is defined in terms of a stack machine *although the browser compiles it to something more efficient*

- [ ]  what is more efficient

validation ensures that if say that you're going to return one value, then one value exactly is left on the stack

# WAT

WebAssembly Text

it's the actual assembly you think of with web assembly I believe

looks kind of like lisp. It's a tree with nodes. The type of node is identified by the first word inside the `(`

These are known as S-Expressions

### functions

function signature look like this:
`(func (param i32) (param i32) (result f64) ... )`

you can have n-params and n-results

the `...` is where the local var declarations and body would be

parameters and local vars have the same scope of course — parameters are just local args that are passed in, really

in the body, `local.get 0` `local.get 1` etc. refers to the parameters/locals by index, but they can also be referred to by name using `$` prefix. for example `(param $p1 i32)` can be referenced `local.get $p1`

functions need to be exported which can be done with `(export ...)`

You can use wasm functions in the browser but somehow you can also pass down JS functions to wasm and have it run the js function. Not sure how that works under the hood though...

### interaction with js

you can share global variables, functions, etc. It's still confusing to me how all of this works. maybe [[]] might have some info

### memory

for wasm, it's just a large array of bytes that can grow over time.

exposes the raw contents of stored values as bytes

### tables

store references

not immediately sure why we can't just store those in linear memory. is this a fair confusion?

The reasoning for tables is:

```
WebAssembly needed a type of call instruction to achieve this, so we gave 
it call_indirect, which takes a dynamic function operand. The problem is that 
the only types we have to give operands in WebAssembly are (currently) 
i32/i64/f32/f64.

WebAssembly could add an anyfunc type ("any" because the type could hold 
functions of any signature), but unfortunately this anyfunc type couldn’t 
be stored in linear memory for security reasons. Linear memory exposes the 
raw contents of stored values as bytes and this would allow wasm content to 
arbitrarily observe and corrupt raw function addresses, which is something 
that cannot be allowed on the web.
```

I don't really understand this.

- [ ]  Can't the function pointer just be an arg that gets passed in. I must be missing something fundamentally.
- [ ]  so we can expose and corrupt values in our linear memory but not function addresses?

# Streaming

- [ ]  web assembly can be streamed and compiled on the fly? [https://youtu.be/3LWgbjVWLug?t=1079](https://youtu.be/3LWgbjVWLug?t=1079) "compiled in multiple threads" but it's already compiled...?