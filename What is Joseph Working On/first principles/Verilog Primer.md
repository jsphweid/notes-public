# Verilog Primer

Status: Completed

everything is a module, even tests... can make functions, for statements, if statements

but it's not a language in the traditional sense... It's kind of like a DSL or Hashicorp Configuration Language

there are blocks that have a begin/end, which can be either sequential or parallel

time is relative and the units are arbitrary I think. From what I can tell, the execution doesn't actually  'wait' around for the time to pass...

clocks - 

initial block - block often used in tests that sets the initial state

- can only be ran once... not repeatable
- may not be able to be used in hardware
- should only be used for simulation really
- starts at simulation time 0
- 

always block - it's a block that only gets executed when one of the inputs change... (reminds me of some react hooks)

- the list of inputs is called a sensitivity change
- often used as `posedge clk` which means it only happens on the rising edge of the clock, but really it can be used with any variable (I'd think); it's more of the 0→1 transition (NOTE: , not 0→1)
    - posedge ⇒ positive edge (going from 0 → 1)
    - negedge ⇒ negative edge (going from 1 → 0)
- you often see `<=` in assignments
    - this means the assignment is non-blocking
        - if there are multiple assignments using the same vars, it will use an older assignment (?) (unless blocking assignment is used..?)
        

reg = register, holds data (/state?)

wire = some ref to a variable that can't be changed but observed

assign - basically like hooking wires up straight-up... I suppose you could build a pass-through module... but you'd have to use assign in that...? (or two `not`s)

- it may be a little more complicated than this actually... it [happens async](https://numato.com/kb/learning-fpga-verilog-beginners-guide-part-2-modules/) but honestly I don't really know what this means...

builtin verilog gates... see here: [https://www.asic-world.com/verilog/gate1.html](https://www.asic-world.com/verilog/gate1.html)

model interface - basically the arguments

- kind of like a pin map for an IC