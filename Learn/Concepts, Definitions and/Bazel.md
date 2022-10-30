# Bazel

google's open source version of its internal build system (called blaze)

watching [https://www.youtube.com/watch?v=6GCDfoAOKIY](https://www.youtube.com/watch?v=6GCDfoAOKIY)

- seems to support any language in theory
- only builds the things that it needs to when things change

workspaces - directory that houses:

1. all of a project's source files
2. Bazel's build outputs
- contains a `WORKSPACE` file - seems to mostly identify the project as a "workspace"
- 1+ `BUILD` file(s) - tells Bazel how to build *different parts* of the project
    - directories *within* a workspace that have `BUILD` files are "packages"
- all inputs and dependencies must be in the same workspace... *unless* linked...()
    - [ ]  what is an input?
    - [ ]  what is a dependency?
    - [ ]  what is linking?
    

`BUILD` file

- contains several different types of instructions
    1. build rule - most important, tells Bazel how to build desired outputs (executable binaries or libraries)
        - each instance is called a *target*, which points to a specific set of source files and dependencies... also possibly other targets
        - examples of build rules
            - cc_binary
            
            ```
            # the `name` attribute is mandatory, but many are optional
            # the `sources` attribute is optional (somehow)
            cc_binary(
                name = "hello-world",
                srcs = ["hello-world.cc"],
            )
            ```
            
            - cc_library

To build:

- example: `bazel build //main:hello-world`
    - `//main:` is the location to `BUILD` file relative to the root of the workspace
        - [x]  what does the double `/` indicate?
            - dunno but here is a better formula: `//path/to/package:target-name`
- more complex examples use a visibility attribute because by default targets are only visible to other targets in the `BUILD` file... I assume this is so you can control who gets access to what very explicitly?