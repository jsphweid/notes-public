# Transformer Model

A NN model that uses [[Attention]]  (and self-Attention). It's good for parallelization. Good for long-range dependencies. 

[https://ai.googleblog.com/2017/08/transformer-novel-neural-network.html](https://ai.googleblog.com/2017/08/transformer-novel-neural-network.html)

Here is a typical high level drawing:

![[/Untitled.png]]

Each encoder looks like this:

![[/Untitled 1.png]]

The Self-Attention step looks like this:

![[/Untitled 2.png]]

The things I don't initially understand here are the Queries, Keys, and Values

Successful examples:

- [[BERT]]
- GPT-3 - OpenAI

Helpful links:

[https://jalammar.github.io/illustrated-transformer/](https://jalammar.github.io/illustrated-transformer/)