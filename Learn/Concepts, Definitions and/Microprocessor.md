# Microprocessor

a "complex chip", 

- [x]  is a microprocessor a CPU?
    - no, but most CPUs are microprocessors
        - a roomful of vacuum tubes is a CPU but not a microprocessor
    - think

requirements of being a microprocessor:

- multipurpose
    - [ ]  how is this a requirement... what does it mean...?
- clock-driven - see [[Clocks in digital circuits]]
- register-based
    - [ ]  ???
- digital integrated circuit that accepts binary as input, processes it according to instructions stored in memory and provides binary results

They process machine code, which has likely been assembled via an assembler. An assembler assembles assembly code into machine code. The assembly code (and consequently machine code) is specific to the machine/microprocessor family. Compilers from higher level languages change a 'high level language' into assembly which gets assembled into machine code for a particular architecture.

### comparison with microcontrollers

not a microcontroller (which has more devices included). An arduino is a microcontroller

microprocessors rely on external RAM and peripherals. They may or may not have integrated registers though (which is a form of memory). microcontrollers on the other hand have all of that stuff integrated in System on a Chip fashion

### 6502

a classic microprocessor

watch this: [https://www.youtube.com/watch?v=LnzuMJLZRdU](https://www.youtube.com/watch?v=LnzuMJLZRdU)

it has a small reset sequence and then just starts reading address for instructions???. And it takes two clock cycles to reach each... No it's reading a no-op because he "hard-coded" it to look there in the data register?

you need a ROM chip with some more interesting instructions