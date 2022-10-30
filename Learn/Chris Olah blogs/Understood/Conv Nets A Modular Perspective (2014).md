# Conv Nets: A Modular Perspective (2014)

What is slightly confusing to me about conv nets, is that in some ways they appear similar to how I think of convolution: a special kind of mathematical operation used to for example filter sound waves or images. Convolution of signals is combining signals: combine a signal with a kernal. That's the heart of DSP.

There are times when reading about CNNs where I feel like this is the case. For example, in an image, it seems like a filter is applied using convolution for the inner layers, but the filter's structure/properties *are learned* by the neural network...

This is what confuses me... What is this:

![[/Untitled.png]]%201f33b66281b346ee81e6934ce729cc86/Untitled.png)

They seem to be a little different when I hear NN people talking about it

- [x]  what is the difference or misunderstanding?
    - Possibly, the drawing above is just unrealistic because usually the kernel length is longer than that
    - when I think of convolution, I think a stride, but his drawings are probably "all strided out" (yes I just made that up)

CNNs seem to be a way to reduce the complexity of the problem: distilling what would be many neurons into a condensed set of neurons that are dense with useful information

Often followed by a max-pooling later to downscale — gets rid of some variation in the image anyways