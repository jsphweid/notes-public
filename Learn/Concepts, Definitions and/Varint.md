# Varint

Google uses this a lot (for example in LevelDB)

integer with variable number of bytes

from left to right, every MSB of each byte is 1 except last

bytes are little endian

![Untitled](Learn/Concepts,%20Definitions%20and/Varint/Untitled.png)

if statements processed in specific order, smaller to larger cases

`>>7` is used because we only use 7 bits to represent the number

the `*(ptr++)` is interesting because I’m not really sure why the parens are needed

this code could be simplified. In fact it is even in the same leveldb codebase… hmm