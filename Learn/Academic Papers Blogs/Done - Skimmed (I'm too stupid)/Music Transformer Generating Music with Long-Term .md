# Music Transformer: Generating Music with Long-Term Structure (2018)

[[1809.04281.pdf]]

### [https://magenta.tensorflow.org/music-transformer](https://magenta.tensorflow.org/music-transformer)

This generates MIDI like [[Learning to Create Piano Performances [[(2017)]]]] BUT instead of using some RNN/LSTM which has access to only a fixed-size hidden state, it uses a tranformer model where it has direct access to *all* earlier events

- [ ]  what is the "original transformer model" that it keeps talking about?
- [ ]  on multiple occasions, it's referring to other papers and I don't immediately understand the specifics of what it's referring to

Can be used with a primer (like a set of input notes that the model then uses as a motif) or without a primer.

Score Conditioning - kind of like a primer but instead it's more of a play along (for example, you give it twinkle twinkle little star and ask it to harmonize it with ad libbed textures and harmonies)

### actual paper

- [x]  why is "relative timing" more meaningful here?
    - after reading a few paragraphs, it seems that the importance for relative timing is to satisfy the common qualities of music, periodicity, groove, pattern, i.e. some regularly repeating quality which pervades much of music. Building things in an absolute way apparently does not promote this. When using relative timings, periodicity is a first class citizen
        - [ ]  but does this capture the periodicity between larger sections of music or just the note-to-note?

"self-attention" as it relates to a generative model, is the basic ability of the NN to look at its self. The kicker here is that it can access any part of its self. This is in contrast to RNN, where only a limited amount of past information is allowed to be stored, which means the NN has to carry the burden of preemptively learning what is important so it can be kept somehow. The argument here is that this restriction is unnecessary in some contexts such as a task like music composition. And so it can simply be swapped out for this self-attention mechanism.

uses a more sparse MIDI-like representation where position in sequence no longer corresponds to time

- [ ]  I don't really understand this section

- [ ]  how is independence achieved in voices? and how is it represented towards the end of the model?
- [ ]  what are "per-position representations"?

### Attention with Chris Olah first

[https://distill.pub/2016/augmented-rnns/](https://distill.pub/2016/augmented-rnns/)