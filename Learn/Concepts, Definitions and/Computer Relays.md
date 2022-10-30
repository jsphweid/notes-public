# Computer Relays

see [https://www.youtube.com/watch?v=n594CkrP6xE](https://www.youtube.com/watch?v=n594CkrP6xE)

started as signal repeaters in telegraphs

early versions used an electromagnet which mechanically operated the switch but never versions use solid state

ensure electrical isolation between control and controlled circuits

### early electromagnetic versions

electricity changes the field around the wire it's passing through, see 

![[/Untitled.png]]

you can make this field even stronger when you wind the wire in a **coil**. With a strong field, you can actually affect decent physical change (activating a switch) - this is a solenoid

See image below, but basically when the left circuit is lit up, the coil produces magnetism which makes the armature move away from where the spring on the right is keeping it and pushes the circuit on the right to be completed. When magnetism is lost because the left circuit is turned off, the spring on the right side draws the armature back to its natural position.

![[/Untitled 1.png]]

This is also interesting because you could replace the right circuit in the image above with a pipe on a pipe organ. I think this is how modern pipe organs operate actually.

I'm thinking about how I could build a python version of this... it's difficult to imagine because programming is generally a "write then execute" sort of environment whereas electricity is more of a persistent environment with continuous information and state reveals itself and transitions through time. 

### solid state relays

no moving parts (obviously)

uses a photo-sensitive transistor. not going to go into too much detail about it here, but basically there is light and receptor inside these things that replaces the coil/switch

I'm sure there are legit uses for these but on the surface, my confusion is: if these use a transistor inside, and transistors can just be used as switches too, why not use those instead of relays. Also, I am dumb.