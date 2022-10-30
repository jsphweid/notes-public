# Improving Perceptual Quality of Drum Transcription with the Expanded Groove MIDI Dataset (2020)

[[2004.00188.pdf]]

E-GMD seems like a combination of other public datasets

It randomly played the data in various batches, combinations, permutations, normalizations, etc.

Basically most of this paper was focused on how they gathered the data and what the results from the model were. They also talked about limitations. But the long and short of it is that the model ranked more superior compared to other state of the art models.

The model used is close to [[Onsets and Frames  Dual-Objective Piano Transcription (2018)]] but there were some slight differences — like a dedicated velocity prediction module, as well as putting more emphasis on higher frequencies by using 44.1khz sampling rate instead of 16khz.

They also seemed to train this model for much longer than the piano one... which is interesting for some reason