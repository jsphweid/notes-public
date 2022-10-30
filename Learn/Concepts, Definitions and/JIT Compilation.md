# JIT Compilation

combines compiled and interpreted languages together by taking certain parts of the code and compiling those

It works even by tracing actual usage and deciding what to compile that way

Static/Dynamic, Compiled/Interpreted are not necessarily binary choices, it's a spectrum

see [here](https://youtu.be/yCd3CzGSte8?t=2842). Swift for example is pretty fluid (for example). I think it's compiled language basically but can leverage JIT to seem like an interpreted language by using parts of LLVM toolchain to compile stuff in real time