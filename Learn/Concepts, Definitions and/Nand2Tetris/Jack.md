# Jack

very simple version of Java

no inheritance

1 class per file and can be compiled separately

function local vars must be defined at the top?

"Following its header specification, the subroutine declaration contains a sequence of zero or more local variable declarations, then a sequence of zero or more statements."

- [ ]  not sure exactly what this means

primitives are allocated to memory when they are declared, 16 bit int, boolean, char

a declared class only consumes a pointer

standard lib comes with Array, String

- declaration of

types - weak typing

- "The language specification does not define the results of attempted assignment or conversion from one type to another, and different Jack compilers may allow or forbid them. (This underspecification is intentional, allowing the construction of minimal Jack compilers that ignore typing issues.)"
    - [ ]  not really sure what this means yet

object var can be converted to array, which allows object fields to be accessed like an array

variables - static, field, parameter/arg, local - pretty self explanatory

interesting statements

- let - assignment, single valued or array
- do - essentially "call"

expressions

- constant
- variable name in scope
- `this` keyword - denotes current object
- array element expression
- non-void subroutine call
    - [ ]  why non-void
    - [ ]  how do this mix with "do"
- various unary and binary operators

order of evaluation - for the simplicity of the complier, you need parens if you want any sort of ordering

manual garbage collection

calling new makes an OS call to get enough memory space for the object

convention is to have a dispose method on the class to inform it how to dispose

- [ ]  the example of dispose list they have isn't 100% clear

standard lib has lots of things and "can be viewed as a basic operating system"