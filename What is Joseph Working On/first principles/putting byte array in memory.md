# putting byte array in memory

Status: random thoughts

I had a buffer that was a string of bytes in memory. When I printed them out, I noticed:

![[/Untitled.png]]

Apparently it has something to do with signs

- [ ]  what does that mean? maybe [here](https://stackoverflow.com/questions/3512749/memcpy-adds-ff-ff-ff-to-the-beginning-of-a-byte) or [here](https://stackoverflow.com/questions/31090616/printf-adds-extra-ffffff-to-hex-print-from-a-char-array)

But, basically my thought was... the width of the memory is 4 bytes (32-bit) yet we are only using up 1/4 of that to do our stuff with chars. Is that really what's going on here?