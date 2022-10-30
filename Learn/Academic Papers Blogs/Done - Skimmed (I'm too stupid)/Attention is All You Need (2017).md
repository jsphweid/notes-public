# Attention is All You Need (2017)

[[1706.03762.pdf]]%202a24aa02d36b49978c41e25b2a265d0c/1706.03762.pdf)

This work introduces a Transformer model, BUT attention mechanisms have existed for a while already apparently. What this does differently: it discards other parts of the network historically used with the attention mechanism (convolution, rnn, etc.)

Attention is more or less an importance vector and it solves the problem of having a finite "memory" in a neural network. RNNs offer a fixed size memory which is restricting when the task requires long term dependencies.

Soft Attention - looking at a few specific regions, deterministic

Hard Attention - looking at 1 specific region, non-deterministic/stochastic 

- [ ]  what is the difference between these encoders and decoders used in transformers compared to the standard autoencoder network

"you have more options when you view the data as a sequence of glimpses" (as opposed to seeing it all at once)