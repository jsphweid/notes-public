# The Bach Doodle: Approachable music composition with machine learning at scale (2019)

[[000097.pdf]]

[https://magenta.tensorflow.org/coconet](https://magenta.tensorflow.org/coconet)

CoCoNet is introduced in [[Counterpoint by Convolution [[(2017)]]]], which was a paper way to hard for me to understand. 

### training

1. start with a score 
    - 3 dimensions, Voice x Note x Time
        - [ ]  although isn't time more nuanced? like start, stop, etc.
2. combining that with a "mask" that covers up parts
3. model makes predictions
4. something about probability distributions and guessing which ones were missing?
    - [ ]  but how is that different from previous step?
    

### inference

so from the probability distribution step, it could either do one at a time and re-run

- says "This strong assumption often leads these processes off the rails when the model gets increasingly confused by its own creation."
    - [ ]  why though?

but what it actually does is fill the whole thing in, then refine it again by taking stuff out and in-painting more notes 

- [ ]  how does it decide which ones to take out? is it random? or does it take out ones with lower probability? i.e. how does it know that it is refining something as opposed to corrupting it?

============

left off at Why does it work? here: [https://magenta.tensorflow.org/coconet](https://magenta.tensorflow.org/coconet)

Honestly, this blog post ain't much better than the paper. Holy Jesus.