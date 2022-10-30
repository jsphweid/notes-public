# WaveNet

- In 2016, DeepMind developed this deep NN to produce raw audio. Was better than google TTS, but not as good as real speech. Used by Google Assistant
- Not using RNN, apparently just convolutional NN — uses "dilated convolutions".
    - animation of how this works here: [https://youtu.be/hzpxXZJQNFg?t=70](https://youtu.be/hzpxXZJQNFg?t=70)
    - dialated - "make or become wider, larger, or more open."
- generative approach to probabilistic modeling
- if you started it with a sample, then had it generate the next using the previous sample, then the next with the previous samples, etc., it would basically generate gibberish / simlish
- uses "external conditioning" so you can tell it what to say

Iteration 1 (2016)? - [https://www.youtube.com/watch?v=CqFIVCD1WWo](https://www.youtube.com/watch?v=CqFIVCD1WWo)

- apparently it generates music pretty well too
- 90 minutes to generate 1 second of audio though (2016), yikes. it's hard for it to go fast because it has to compute 1 sample at a time and all the previous ones are dependent on each other

Iteration 2 (2017)? - [https://www.youtube.com/watch?v=hzpxXZJQNFg](https://www.youtube.com/watch?v=hzpxXZJQNFg)

- 1000x times faster (apparently because of "Probability Density Distillation"?)
- has student/teacher concept which somehow solves the dependent problem?

Iteration 3(2018)? - [https://youtu.be/gIIZyYsB81M?t=1147](https://youtu.be/gIIZyYsB81M?t=1147)

- doesn't use dilation or even convolution (???) but instead a GRU cell

"wavenet" is more than just a paper evidently as it can evolve over time...