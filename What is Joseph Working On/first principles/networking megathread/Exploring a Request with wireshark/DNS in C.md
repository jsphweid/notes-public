# DNS in C

see [here](https://stackoverflow.com/questions/47258547/why-is-the-hex-value-of-a-period-in-a-dns-request-not-0x2e-and-why-does-it-chan) but basically you don't encode addresses quite the same as you do in text

- "laughtears.com" is encoded like "10 laughtears 3 com" using those lengths indicating how long the next segment is...