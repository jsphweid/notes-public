# Jack Compiler

compilation = syntax analysis + code generation

# Syntax Analysis

syntax analyzer

- tokenizing
- parsing
- OR could also be divided like
    - lexical analysis
    - context-free grammars
    - parse trees
    - recursive descent algorithms
    

syntax analyzer can output XML to make sure we're building things correctly

computer (formal) languages are different from natural languages. formal languages have simplicity and consistency. Their structure is allegiant to a set of strict rules ("context-free grammar"). Parsing is determining the exact correspondence between what is written and grammar rules. The first step to this is breaking it into tokens.

- [ ]  not 100% following this

syntax - rules that govern structure of a language

### Characters

A text file is really just a sequence of characters.

### Tokens

But we only care about certain ones. For example, we don't care about white space, comments, or individual characters necessarily. So we  group things into tokens, groups that we care about and are meaningful. This stream of tokens is the meaningful input with which we make decisions by. Each language defines which tokens are valid and how they ought to be used.

### Grammar

The next step is assembling tokens into a grammar that represents various tasks like variable assignment, statements, expressions, etc.

### Context-free Grammar

In layman's terms, I think it means that the context doesn't matter. A sequence of tokens means the same no matter where it is placed.

- [ ]  Gotta be honest... I didn't really fully grasp the rest of this little discussion

## Parsing

determines if input is valid by (again) determining correspondence between what is written and grammar rules

parser output → parse tree (or derivation tree). The rules are hierarchical. In other words (and is perhaps [more obvious here](https://stackoverflow.com/a/57913354/4918389)), parsing is taking linear stream of tokens and transforming it into a hierarchical structure

### parse trees

Some compilers hold the whole tree in memory while others approach it more incrementally

### recursive descent parsing

basically, you start with the tree from the top. you go down until you hit terminal atoms where things can be directly translated — if not you recursively parse the non-terminal atoms until you get to the bottom

more about parsing...

![[/Untitled.png]]

could have 5 different parsing routines (left side). the implementation of the statement parser (first one) need to determine which of those (while/if/etc.) it is and then call the associated subroutine for that. Sometimes this is obvious because of that first token (for example, if the first token *while* is used, then we probably need to follow with a whileStatementParser, since the grammar doesn't allow it to mean anything else — when it is this obvious, it's call LL(1) — Leftmost, left-to-right). If that's not the case, then look-ahead is necessary. In Jack, only expressions are the only item in the grammar where look-ahead is necessary.

![[/Untitled 1.png]]

## Analyzer

I assume this is a tool we need to build. Similar to the translator we built, it accepts an argument of a file or group of files in a dir.

### terminals

things that are bolded above

should generate <xxx> terminal </xxx>, where xxx is

- keyword
- symbol
- integerConstant
- stringConstant
- identifier

### non-terminals

<xxx> recursive code for body </xxx>, where xxx is

- class, classVarDec, subroutineDec, parameterList, subroutineBody, varDec
- statements, whileStatement, ifStatement, returnStatement, letStatement, doStatement
- expression, term, expressionList

## Output

tokenizer ⇒ XxxT.xml

parser ⇒ Xxx.xml

## Compilation Engine

tokenizer is easy. This is a bit tougher

advances tokenizer exactly beyond the *end tag (?)*

`class` keyword hints `class` start

`function` keyword hints `subroutineDec` start

`let` keyword hints `letStatement` start

`while` keyword hints `whileStatement` start

`do` keyword hints `doStatement` start

`{` symbol (after function?) hints `subroutineBody` start

`var` keyword hints hints `varDec` start

what kicks off `statements`, `parameterList`? (plural)

what ends something? maybe `;`? maybe only statements

`=` anticipates an `expression`?

`(` anticipates an `expressionList`? which has multiple `expression`'s

each expression has a `term` inside it?

### Recursive Descent Algorithm

need a recursive routine that can parse non-terminals

If the non-terminal consists of only terminal atoms, the routine can output them in a structured way. Else recursively call

### Expression List

are arguments when calling a function, separated by the `,` symbol

### Terms

Originally I think I was overthinking what *term* could mean, but now it seems more clear. An expression is composed of one or more terms separated by symbols

# Code Generation

Two main issues:

1. Data Translation
    - variables!
        - life cycle / scope - local/global/argument/field/etc. - maintain
        - type - must accomodate in the target platform
        - symbol table - a look up cache (?) of sorts that describes each variable when it is encountered, keeps track of scope so that it manipulates the correct variable if multiple exists at multiple levels. must encode scope. IE sounds like more than just local/global. Obviously if it's local, which local? idk yet
            - suggested as a list of dictionaries
        - different types require different sizes of memory chunks
        - different kinds have different lifecycles
            - example: static variable should be available for entire program lifecycle
            - example: field in class is available for each instance of object and until the object is cleaned up
        - but we already did a lot of this in the VM layer, now we just need to manipulate them
        - objects - everything gets stored as an index to the base address, objects, arrays, etc.
            - object has a base address and variables on the object are stored at numbered locations away from base address?
2. Command Translation
    - expression evaluation
        - postfix notation, x+y → x,y,+ or *push x*, *push y*, *add*
            - 
    - flow control
        - must translate if/while/for/etc. to lower level goto / unconditional-goto
        

### Observations from translated programs

- constructor new calls `Memory.alloc` - this returns a pointer to the base address... to store this, it's always popped to pointer 0 `pop pointer 0`
- `this` used to refer to fields on instance in their correct order but sometimes `pointer` is used
    - [x]  when and why is `pointer` used?
        - seems like every time `this` is referred to by name, you see `push pointer 0` maybe because that refers to the base address of the object whereas `push this 0` refers to the first argument on the object
- object functions seem to pass in that fantom this/self argument via
    
    ```wasm
    push argument 0
    pop pointer 0
    ```
    
    the "self"/"this" is argument 0, which is an address presumably. It's pushed to the stack and then popped into `pointer 0` (THIS) so that shifts the base address for THIS
    
- `var` vs. `let`
    - `var` is a variable declaration, like `static` or `field`
    - `let` is a statement, you always see assignments with `let`
        - you assign variables with `let` BUT THEY ALREADY HAVE TO BE DECLARED IN SOME SCOPE
        
    

# Go back and check out

- [ ]  pointer 1, i.e. that - I didn't really have a clear understanding of what or why I was doing that