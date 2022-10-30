# MidiMe: Personalizing a MusicVAE model with user data

[[aaa.pdf]]

start: blog post here: [https://magenta.tensorflow.org/midi-me](https://magenta.tensorflow.org/midi-me)

They built a model that is in part pre-trained, but allows for additional training from the user to "make it their own"

Most interesting bit so far is "This allows us to generate samples from only the portions
of the latent space we are interested in"

- [ ]  so the final icing training controls very specific parts of the latent space?

[[MusicVAE]] has a latent space of 256 dimensions, what MidiMe is, is a compressed representation of MusicVAE's compressed representation!

There are apparently tradeoffs with whatever MusicVAE model you are starting with. 

- [ ]  ~~What are "free bits"?~~
    - a constraint on the minimum amount of information per group of latent variables
    - I think this means the number of neurons that the data can be compressed down to.
- Nonetheless:
    - many free bits - good at reconstructing input, generated samples will sound similar to what it was trained on
    - fewer free bits - good at generating "plausible" samples, but not good reconstructions
    

It sounds like what happens in this model is that you have a VAE with latent space, and you train another model, essentially, to manipulate that latent space in such a way that it gives you something more specific or easier to control