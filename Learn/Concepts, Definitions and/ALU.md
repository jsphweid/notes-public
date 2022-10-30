# ALU

according to [here](http://www.peter-cockerell.net/aalp/html/ch-1.html) (ARM assembly tutorial) - "The ALU can be regarded as a black-box which takes two 32-bit numbers as input, and produces a 32-bit result."

- [ ]  what happens if the two 32 bit numbers are large such that the result can't be captured in a 32 bit result..?? (integer overflow perhaps?)

### Two's compliment

- flip bits then add 1 to get the negative equivalent
    - examples
        - 0010 (2) → 1110 (-2)
        - 0110 (6) → 1010 (-6)
        - 0111 (8) → 1000 (-8)
    - kind of disorienting at first, but it's not that bad
    - addition is exactly the same as positive numbers, but you have to throw away a bit...
        - 1110 (-2) + 1101 (-3) → 1011
    - subtraction? just turn it into an addition problem...

### half adder

adds two bits

outputs *sum* and *carry*

n2t says make LSB sum, MSB carry

- [x]  what does this mean and what ramifications does it have
    - carry is always adding to the MSB, so that kind of makes sense

### full adder

adds three bits

### adder

adds n-bits

I think using the full adder is important because you can add 3 bits. That is:

1. digit from one number
2. digit from the other number (same position)
3. carry bit

Then you should be able to just loops somehow

### ALU

can do many functions, specified by control bits