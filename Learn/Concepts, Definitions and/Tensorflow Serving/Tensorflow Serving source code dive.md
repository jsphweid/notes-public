# Tensorflow Serving source code dive

It's a c++ project. I know a bit of C. Very little c++. Doesn't seem like an insane number of lines of code though. It downloaded relatively quickly. Let's see how this goes.

### general file structure

- no make/cmake... hmmm
    - looks like it uses bazel, which is a google thing... it's kind of like make, gradle, ant, etc.
    - cmake is actually a meta-build tool
    - bazel is less manual

### compiling