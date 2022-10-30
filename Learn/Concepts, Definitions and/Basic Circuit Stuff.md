# Basic Circuit Stuff

### Playing around with an arduino...

### Other stuff

[https://en.wikipedia.org/wiki/Kirchhoff's_circuit_laws](https://en.wikipedia.org/wiki/Kirchhoff's_circuit_laws)

Basically in a closed circuit, the nodes voltages must drop so there is 0 left. see [here also](https://www.youtube.com/watch?v=CdqvY_vY1XA&list=PLowKtXNTBypETld5oX1ZMI-LYoA2LWi8D&index=2) 

voltages drop

You may have a constant voltage but lower current

You can't talk about voltage at a point, but a voltage between two points

## flip flops vs. registers

flip flop - store 1 bit, takes in a clock

- how long does it remember? (until you flip it again... or for 1 clock pulse?... or??)

register - like a flip flop but can store stuff for an arbitrary amount of time

flip flop can only "output its previous input"

### feedback

feedback is okay for sequential chips because there is a time delay

# clock thoughts

we allow sequential chips to be in unstable states during clock cycles, but they should stabilize before the next tick

![[/Untitled.png]]