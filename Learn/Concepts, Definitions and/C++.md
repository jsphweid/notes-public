# C++

because my team at G uses it

## for loops

`for (int i = 0` etc.

## Array vs. Vector

seems a bit like Array vs. Slice in Go

arrays are fixed size whereas vectors are not

Arrays are fixed size but have a lower memory footprint and access elements faster

C++ introduced vector and “templatized array”

- “(templatized array) is a normal array wrapped in an object”
    - has extra features, like able to keep track of size (unlike normal array)

## implicit conversions

seems like cpp will implicitly convert types… for example, you have a class that 

## Some sort of implicit conversion?

basically, say a function takes in a const ref of a certain class. Instead you pass in a string. Obviously the types aren’t correct. BUT you can have a constructor on that class that accepts a string and it will know to automatically use that overloaded constructor

- [x]  ask someone about this — not sure what it is called
    - it’s called implicit conversions… you can prevent this by putting “explicit” in front of the class method. Google discourages implicit conversions but I learned about it from their code…
    - I don’t think you can implicitly convert a string using `std::string`, but you can go to `char*`
    - [ ]  how does the const ref thing work with implicit conversion? const ref isn’t supposed to make new things, but you kinda have to if you want to convert a `char*` to a new object, right?

## Template

std::bitset<8>, the <8> is a template? 

- [ ]  need a lot more info on this….

## Pointers vs. References

references `int&` are something that the compiler takes care of — doesn’t actually use memory in runtime I believe

pointers `int*` consume runtime memory in stack or heap depending on how it’s declared

## Threads

`std::` has a lot of neat stuff to make threading easy

mutex (mutual exclusion object) helps create a lock

- [ ]  what is the difference between lock and mutex really

condition variables help sync threads

- cv.wait takes a lock and a optional predicate function
    - lock seems to be like a wrapper around a global mutex var
        - [x]  what are the various wrappers and what is the diff between them?
            - lock_guard - can’t be used with wait
                - is more of a one time thing
                - locks when initialized then unlocked when it goes out of scope
            - unique_lock - actually you need this for wait
                - can lock/unlock
                - doesn’t immediately lock if you pass in `std::defer_lock` as 2nd arg
                    - can lock later with `std::lock` — helpful when locking multiple locks at once
    - [x]  what happens when no predicate is used?
        - it’ll simply awake when notified or spurious wakeup
        - there are times when [no predicate is slightly more optimal](https://stackoverflow.com/a/35013353/4918389)
    - [x]  how long does it wait until retrying?
        - cv.wait will temporarily release the lock until cv is true
        - I don’t think it just loops endlessly, the OS schedules it by putting it in some queue I believe. But again, it can pop it from the queue spuriously, which is why you often see these in loops with a condition

std::atomic - represents a type that multiple threads can operate on without getting undefined behavior. say you have have an operation that adds a bunch of numbers but then you split it across N threads. Without using an atomic variable, these 3 threads might read/write to old state and you get undefined behavior. Using atomic variable this doesn’t happen. [atomic operations are faster than mutex](https://stackoverflow.com/questions/15056237/which-is-more-efficient-basic-mutex-lock-or-atomic-integer)

When locking/unlocking, sometimes a separate codeblock is used `{}`

## Structs

similar to classes but everything is public by default

people use structs for POD generally

## Namespaces

you can use `namespace foo { }` (for example) in many files

## Casting (and conversions)

[this is tricky](https://stackoverflow.com/questions/332030/when-should-static-cast-dynamic-cast-const-cast-and-reinterpret-cast-be-used)

```cpp
char c = 11;       // 1 byte
int *p = (int*)&c; // 4 bytes
```

Basically this is a traditional C style cast and this is dangerous! We declare a variable `c` with value `11`. It only takes up 1 byte. On the next line, we’re getting the address of `c` and saying “nah you (and the next 3 bytes immediately after you) are going to be part of this 4-byte number. Thing is, those other 3 bytes could be other things. So it’s likely the number is no longer 11. But really there is nothing preventing this dangerous code from compiling…

also real quick, from [this video](https://www.youtube.com/watch?v=8egZ_5GA9Bc), type punning is when you have memory laid out a certain way but you use it a different way using casting to avoid copying and what not

anyways…

```cpp
double x = 5.1;
int b = x;
```

```cpp
double x = 5.1;
int b = (int)x;
```

### c++ style casts

### static cast

Google styleguide prefers these over c-style casts. They simply add more safety and searchability across a codebase

```cpp
double x = 5.1;
auto b = static_cast<int>(x);
// or better, separate conversion / casting...
auto c = int32_t{x}; // NOTE: fails because info loss using brackets
auto d = int32_t(x); // succeeds
```

### const cast

adds or removes const

### reinterpret cast

like mentioned above, changing memory to be something else directly

### dynamic cast

kinda complicated, but basically does some checks in runtime to see if a cast is possible

handling polymorphism

- [ ]  need more detail or actual examples of this

## Classes

simple class `class MyClass {`

- [ ]  but what does `class LEVELDB_EXPORT Status {` mean?
    - some sort of macro that defines how or maybe if it exports

constructor `MyClass`

destructor `~MyClass`

- can only have 1, can’t be overloaded
- auto-called when object goes out of scope…

But you don’t really need a constructor to instantiate an object if 

- class has only public members, can basically be created like a struct

default is private

`this` - very similar to js in a sense… but it’s a pointer to the object…

defining a method “inside” the function or not

- if it’s small, then it can be faster to do it inline, also I think it is implicitly `inline` if defined in class
- google style guide says inline if it is short — 10 lines or fewer. If you inline large functions, it can increase the code size which somehow means the whole thing runs slower. do not usually inline functions with loops or switches unless they are rarely executed. Don’t inline virtual or recursive functions

friend 

- functions
    - functions declared in class body that are “friends” of the class and can access private/protected members
    - apparently used a lot when overloading operators
- classes
    - basically same idea
- [G says](https://google.github.io/styleguide/cppguide.html#Friends) define friend in same file, use for builders

forward declaration

- sometimes classes are declared above something that they are later used/referenced in… This is because the compiler has to know about it because it reads top→bottom more or less. It sounds like this is done when you have just a simple class you want to use but you don’t want to use an include

const functions

```cpp
int getVal() const {
  return val;
}
```

- means that val (or any other state variables inside the class) cannot be modified in the body of the function… just a neat little constraint

virtual function

- function overridden by derived class, declared virtual in base class, runtime polymorphism
- probably should use `override` keyword in the derived class for clarity
- uses slightly more memory and compute because program must use a lookup table to figure out which fn to run

deleting constructors

- `Foo() = delete;`
    - [ ]  why would you want to do this?

copy constructor

- you may need special code to copy something otherwise you may be copying pointers if those are some of your member variables
- `class MyClass { MyClass(const MyClass& other) {} }`

if you ever see variables prefixed with `m_` it’s because it’s a ‘member’ variable — not sure how widely used though. Google styleguide does member variables like `member_var_` (i.e. snake case with underscore at end)

initialization lists

- if constructor has const or reference members that need to be set, you can’t set them in the constructor. So the way to do this is initialization lists
    
    ```cpp
    class Demo {
      Demo(int& val) : m_val(val) {} // NOTE: sets const value
    private:
      const int& m_val; // NOTE: is const
    };
    ```
    

## Smart Pointers

help automate new/delete

### unique_ptr

- use for all that don’t need sharing… it’s better because it doesn’t count references
    - [x]  but what if we want it to go out of scope?
        - it goes away
- scoped pointer, go out of scope they get deleted
- can’t be copied…

### shared_ptr

- use when you need sharing, obviously
    - usually uses reference counting

### weak_ptr

- can be copied from shared_ptr but doesn’t increase ref count… so you can have something to ask “are you alive” and get yes/no. If it’s copied to another shared_ptr, the answer would always be yes.

# Misc

- [ ]  a common pattern using c++ api is to create a pointer to something, then pass it into a fn where the fn fills it up with something. how does it know how big that is? is that stack or heap?
    - or even something as simple as `char* str;` then later `str = "hello;`
        - if you print out the address before and after, that address changes
        - so I’m willing to bet it just automatically creates a new pointer that is long enough to put it somewhere
        

converting `char[]` to `std::string`

- if the array has a \0 in it, it’ll be skipped or weird stuff will happen
- [https://stackoverflow.com/a/45129436/4918389](https://stackoverflow.com/a/45129436/4918389)

`constexpr` - value is fixed at compile/link time

# TODO

- don’t really understand cmake
    - macros…? a little
- don’t understand templating