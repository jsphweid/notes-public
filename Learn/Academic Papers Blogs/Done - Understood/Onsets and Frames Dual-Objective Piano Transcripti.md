# Onsets and Frames: Dual-Objective Piano Transcription (2018)

[[1710.11153.pdf]]

# starting with blog post: [https://magenta.tensorflow.org/onsets-frames](https://magenta.tensorflow.org/onsets-frames)

onset detector output

1. feeds into frame detector
2. restricts final output from saying that there is a note occuring

# [https://magenta.tensorflow.org/oaf-drums](https://magenta.tensorflow.org/oaf-drums)

New dataset that allows for lots of drum training...

# actual paper

from summary: the restriction of only predicting a note if an onset exists for it appears to be a feature of inference only which is interesting.

They start with the biggest benefits as being MIR / Musicology tasks

Earlier techniques used Nonnegative Matrix Factorization (NMF)

It appears that the transcriptions are done in 2d space?

translates piano sustain into notes with longer values, simplifies things, but of course loses that extra dimensionality of having a sustain pedal (which colors notes of course)

uses python mir eval library to evaluate

1. note-based precision
2. recall
3. F1 scores

- [x]  summarize and talk about velocities?
    - the velocity study is different because there was no established way measuring velocities in transcriptions before this paper, in fact other papers didn't really consider it apparently
    - velocities are somewhat relative and that means finding the loss is a bit tricky
- [x]  start with 4. EXPERIMENTS

Apparently they tried to add reverb and use other synths but the score was the same :thonk

It says that it is more desirable to *not* have randomly generated samples... but why?