# Reference Counting vs. Garbage Collection

For managing the lifecycle of objects

Reference counting is a technique for knowing when a variable can be released from memory. It does this by incrementing a number for a variable by 1 each time something refers to it is added. When it is removed or goes out of scope it is decreased. When it reaches 0, the memory can be freed

Garbage collection - periodically examine all objects and see which ones can be removed

- [ ]  but how do you know
    - something about being "reachable" though I don't immediately know what that means