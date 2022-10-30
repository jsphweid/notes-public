# 3b. processors (cpu)

Status: geohot stuff not sure I'm gonna do

- [ ]  Building a ARM7 CPU
    - simple pipeline to start, decode, fetch, execute
    - How much BRAM do we have?
    - We need at least 1MB, DDR would be hard I think, maybe an SRAM. Simulatable and synthesizable.
- [ ]  Coding a bootrom(Assembler, 40) -- This allows code download into RAM over the serial port, and is baked into the FPGA image. Cute test programs run on this.