# Visualizing Representations: Deep Learning and Human Beings (2015)

[https://colah.github.io/posts/2015-01-Visualizing-Representations/](https://colah.github.io/posts/2015-01-Visualizing-Representations/)

we look at word vectors, paragraph vectors (wikipedia), and then translation model (representations of LSTM translation task)

Some of these dimensionality reduction techniques are deterministic and some are stochastic. PCA for example is deterministic and t-SNE is stochastic.

### comparing

At least two problems regarding visualizations and their relationship to other visualizations when it's close (reword?)

1. every time a model is trained, it's weights are likely initialized randomly and they gradually become optimized in different directions. A model that is retrained many times from scratch will likely arrive at a similar degree performance, but the individual neurons will look quite different. This makes visualizations appear different although the network has likely learned the same thing.
2. some dimensionality reduction techniques involve stochastic processes

to compensate for this, you can essentially apply a dimensionality reduction technique to each of these similar visualizations and see that they group together actually

### thinking the unthinkable

humans' eyes are extended to see cells and stars with microscopes and telescopes... similarly we can think in ways that were previously unthinkable because we build tools to adapt the thought to our brain's wiring

TLDR: it's better when you can visualize the representations