# Autoencoder

"An autoencoder is a type of artificial neural network used to learn efficient [[data codings]] in an unsupervised manner"

I believe a key part to the success of an autoencoder is its ability to learn a representation/encoding for a set of data AND to simultaneously learn how to use that encoding to reconstruct the original. I think "auto" (i.e. "self", "same") as the prefix here indicates this ability to deconstruct and reconstruct.

![[/Untitled.png]]

Basically, they learn to make some representation and also learn how to translate it back into its original space. Then the end and beginning are compared for loss. That's how you do it without labels.

## Variational Autoencoder

autoencoder with a little stochastic process thrown in the middle

- loss function has to be a little different (reparameterizing)

### Overview according to Two Minute Papers

[https://www.youtube.com/watch?v=Rdpbnd0pCiI](https://www.youtube.com/watch?v=Rdpbnd0pCiI)

Input and output shape are the same dimension

- initially seems pointless because nothing is "being done" from the outside — just have the start and end be the same... But! you have a bottleneck layer, where the network in the middle where the NN is forced to represent the input in *much* smaller dimensionality — because it's going to have to decode to the output (which is the same as input) somehow from that small dimensionality
    - even though this low dimensionality seems appealing for compression, there is apparently no advantage to using classical compression techniques (like jpeg)... but the things they distill in the process can be used for other very interesting purposes