# TorchScript

serializable model that can be loaded in a process where **there is no python dependency**

captures the structure of a pytorch program

subset of python

statically typed

[https://pytorch.org/tutorials/beginner/Intro_to_TorchScript_tutorial.html](https://pytorch.org/tutorials/beginner/Intro_to_TorchScript_tutorial.html)

## Transitioning

for transitioning to "script (graph?) mode" (TorchScript)

tools:

- tracer (`torch.jit.trace`) - a function that takes an eager model and inputs you provide and record all the tensor operations that get done. this recording gets turned into a torchscript module
    - cons: doesn't preserve control flow or other language features like data structures
- script compiler (`torch.jit.script`) - literally parses python code
    - cons: only supports a subset of the python language (but it's growing...)

The central question I have... are all MAR files equal? whether they were compiled from torchscript or eager code?