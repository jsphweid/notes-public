# MusicVAE

[https://magenta.tensorflow.org/music-vae](https://magenta.tensorflow.org/music-vae)

Basically it's like what NSynth is for timbre but to notes.

Generates melodies, or combines two melodies together using special sauce in latent space of a variational audoencoder

![[/Untitled.png]]

Uses several RNNs in a hierarchical structure, namely a Conductor RNN that itself generates embeddings, which are used by the decode instead of the latent space directly.

- [ ]  practically, what does this look like?

"We found this conditional independence to be an important feature of our architecture. Since the model could not simply fall back on autoregression in the note decoder to optimize the loss during training, it gained a stronger reliance on the latent code to reconstruct the sequences."

- [ ]  what does this mean...? to "fall back on autoregression"