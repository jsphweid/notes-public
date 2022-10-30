# MMM : Exploring Conditional Multi-Track Music Generation with the Transformer (2020)

[https://arxiv.org/pdf/2008.06048.pdf](https://arxiv.org/pdf/2008.06048.pdf)

Previous token based systems have a limited way of dealing with tracks because the number of tracks directly increases the token vocabulary. The way they deal this paper deals with it is to keep them separate somehow, allowing the number of token vocab to stay the same

In this paper/model, simultaneous sounding notes from different tracks are spread far apart. Attention allows for **non-time-ordered sequences**

They use conditional, unconditional, and in-painting it seems. In painting seems to work by using a special token (FILL_PLACEHOLDER) to represent the gap and then asking it at the end to come up with something. This is a very low-effort understanding. How can I explore this further

Explore the suggested uses:

1. track inpainting
2. bar inpainting