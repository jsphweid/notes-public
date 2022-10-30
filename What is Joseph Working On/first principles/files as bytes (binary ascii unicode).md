# files as bytes (binary/ascii/unicode)

Status: Completed

There are two types of file

- text files
- non-text files (binary)
    - just a sequence of bytes
    - "binaries" are usually meant to be executable, but a wav/img/etc file are binary files too

[https://www.youtube.com/watch?v=MijmeoH9LT4](https://www.youtube.com/watch?v=MijmeoH9LT4)

Character Codes

- ASCII - represented as 8 bits / 1 byte (256 possibilities, but actually 1 is used for error checking so it's really half..>?)
    - 7 bit - original
    - 8 bit - extended ASCII
    - that's why it conveniently prints out stuff in a hexdump
- Unicode - system designed to represent all the world's characters (like 100k+)
    - basically just assigning all characters to a particular number like ASCII but instead of going to 128/256, it goes up to 100k+
- UTF-8 - it's like an implementation of unicode?!?!
    - uses 7 bits to represent ASCII (so that stays the same) with the first bit a 0
    - above that the first bit is a 1 and starts behaving like a header. subsequent bytes also have "headers" to indicate they are a continuation (although the first header specifies how many there will be)
        - the trick here is to avoid 8 0's which signals to many machines end of file