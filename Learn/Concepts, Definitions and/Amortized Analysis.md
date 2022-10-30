# Amortized Analysis

often you see stuff like this... what does it mean?

![Untitled](Learn/Concepts,%20Definitions%20and/Amortized%20Analysis/Untitled.png)

obviously they seem to usually be the same

"amortized" - means pay off a debt over time - I don't immediately see how that relates to this though...

### reading stack overflow...

from [this](https://stackoverflow.com/a/7335098/4918389):

- "average case analysis makes assumptions about the input"
- "amortized analysis makes no such assumptions"
    - you consider the worst case and then consider the frequency? examples says appending to array can be O(n) when worst case (allocating a new array that's big enough) but since it happens not often it's O(1) overall. So it doesn't consider the inputs... or does it? (because frequency). The average case is... uhh... I need to think about this more at some point