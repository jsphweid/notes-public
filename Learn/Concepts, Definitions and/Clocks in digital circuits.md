# Clocks in digital circuits

allows different blocks to sync with each other

frequency, which determines:

- clock period - time taken to complete one clock cycle (should be completely derived from the freq)
- duty cycle - what percentage of the time the clock is "high" (is this at all derived from the freq though...?)
    
    ![[/Untitled.png]]
    
- clock phase (in relation to other clocks)

At this point, I'm still really confused...

Watching [https://www.youtube.com/watch?v=wx0NyUfpm48](https://www.youtube.com/watch?v=wx0NyUfpm48)

clocks "decide the time of the input"

a clock is nothing but "a signal"

- [x]  does that mean for each signal there is a different clock? like two inputs to a NAND function require 2 different clocks? That seems like a ridiculous thought. Maybe it is that the clock signal is a third-party signal that lines things up somehow?
    - you can use a clock however you wish, it seems like it is more in the vein of "3rd party signal" that I used above. A common pattern seems to be that a clock only makes other devices/switches/gates "on" when the clock is in the 1 position. But things can be designed around only being "on" when the clock is in the 0 position just as easily.
    - from [this video](https://www.youtube.com/watch?v=cXmomjBScGI), the clock dictates when the input will affect the output
    - it's like a metronome

at this point I like the metronome analogy. Another analogy is [runescape ticks](https://runescape.fandom.com/wiki/Game_tick). It's this fundamental lower limit of when actions can be performed in the game. It's like the entire game state changes slightly every 0.6 seconds. That's more of a discrete signal though.

It's still not 100% clear to me. I may come back to this.

Things that confuse me still (somehow):

- [ ]  **why** does there have to be a tick? it's almost like web land where you poll the BE for some new data vs. just letting the BE tell you when there is new stuff via websockets
    - maybe it has something to do with async vs. sync data signals (not really sure what data signals are but it seems like another input to a module)
- [ ]  if things take longer than one cycle to complete, how is the state stored? (if that even makes sense to ask)
- [ ]  from [here](https://www.intel.com/content/www/us/en/gaming/resources/cpu-clock-speed.html), "Sometimes, multiple instructions are completed in a single clock cycle; in other cases, one instruction might be handled over multiple clock cycles" if this is the case, what exactly then is the clock actually doing.!>?!?! (runescape analogy breaks down)

### gear analogy

from [here](https://www.nandland.com/articles/flip-flop-register-component-in-fpga.html), it's like a bunch of gears... you need a master gear turning it 

- honestly, this gear analogy just makes me more confused

from the same site, it shows this D [[Flip Flop]] example:

![[/Untitled 1.png]]

what it basically does it quantize the D into the Q — lines it up with the clock

### networking analogy

[https://www.youtube.com/watch?v=8BhjXqw9MqI](https://www.youtube.com/watch?v=8BhjXqw9MqI)

don't know if this analogy holds up but basically the alternating low-high of data transfer on a line must be chunked up somehow in parts, and two clocks in sync can do that (don't want clock skips)... but that's not really how an IC clock works most likely...? not really sure if this video deals with typical networking (how do packets fit in, for example)