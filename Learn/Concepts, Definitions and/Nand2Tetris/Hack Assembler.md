# Hack Assembler

Assembler is probably going to be easy to write. The only non-trivial thing is dealing with certain symbols that point to *some* memory address (variables/labels)

- [ ]  So these symbols are resolved by specific addresses that exist in ROM, not RAM? (in the same space as the instructions themselves...?)
    - is it possible this was just a dumb example?
    - I thought all symbols are simply erased and replaced with either ROM jump addresses (for goto symbols) or dedicated RAM addresses (for variables)

Some commands may take up multiple machine instructions

variables (particularly in high level languages such as C) will often be larger than 1 memory address

assembler must take into account

1. word size
2. data type

Rules:

- *.asm assembly files → *.hack machine code files
- .hack file is actually a text file where each line is a 16 bit instruction containing just 1s and 0s
- .asm file is a text file where each line is one of these:
    - instruction - A or C instruction
    - symbol - in parens () - generates no machine code but lets the assembler know how to resolve other lines
- constants - non-negative, decimal
- symbols - letters, digits, underscore, dot, dollar sign, colon that doesn't begin with a digit
- comments - text after // should be ignored
- white space - is ignored
- empty lines - ignored also
- casing - mnemonics must be uppercase, everything else can be either, but it's case sensitive (typically uppercase for labels and lowercase for variable names)
- instructions
    
    ![[/Untitled.png]]
    
    ![[/Untitled 1.png]]
    
    - symbols
        - pre-defined
        
        ![[/Untitled 2.png]]
        
        - labels - CAN ONLY BE DEFINED ONCE, refer to instruction memory location
        - variables - non-pre-defined, non-label symbol, mapped to next RAM address starting with 16
        

### Writing the Assembler

they propose 4 parts:

1. parser module - parses the input
    - breaks into fields and symbols
        - A instruction
        - C instruction
            - fields → *comp, dest, jump*
2. code module - provides binary codes for mnemonics
3. symbol table module - handles symbols
4. main - drives translation

this/that/pointer