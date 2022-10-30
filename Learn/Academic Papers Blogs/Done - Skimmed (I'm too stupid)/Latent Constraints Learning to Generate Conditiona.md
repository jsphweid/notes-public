# Latent Constraints: Learning to Generate Conditionally from Unconditional Generative Models (2018)

[[1711.05772.pdf]]

Post-hoc learning latent constraints - is this something like NN fine-tuning?

latent constraints - value functions that identify regions in latent space that generates outputs with desired attributes

- [ ]  ????

In regards to having control over the creative output of a NN, there are several techniques available:

GANs: Generative Adversarial Network

VAE: *Variational* AutoEncoder

They both learn to *unconditionally* generate realistic and varied outputs by sampling from a semantically structured latent space. But they each have strengths and weaknesses

The paper is making it seem like this is the alternative to using custom large datasets to train for something specific *or* tolerating non-specific creations (having no control over parameters at inference time) from a NN.

IE, we can have our cake and eat it.

It does this by somehow separating training steps from the application of user constraints for custom behavior.

1. create unsupervised model that learns how to construct data from latent embeddings
2. leveraging latent structures exposed in those embedding spaces as a source of prior knowledge, upon which we can enforce behavioral constraints

## a new day

This papers is about training a model in such a way that you can apply the constraints *afterwards*

1. create unsupervised model that learns how to reconstruct data from latent embeddings
2. leverage the latent structure as a source of prior knowledge, upon which we can enforce behavioral constraints