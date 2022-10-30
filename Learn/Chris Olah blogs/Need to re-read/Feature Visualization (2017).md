# Feature Visualization (2017)

[https://distill.pub/2017/feature-visualization/](https://distill.pub/2017/feature-visualization/)

This seems to be the process by which you generate "images for neurons" 

1. feature visualization - what is a network looking for
    - seen by *generating* examples
2. attribution - studies what part of an example is responsible for the network activating a particular way

neurons are possibly misleading — it's not always clear why they are the way they are

![[/Untitled.png]]%200ea809b656b448ac958a421aa87fafbb/Untitled.png)

this detects animal faces, but also cars...

You can add neurons together and it's similar to adding word vectors together:

![[/Untitled 1.png]]%200ea809b656b448ac958a421aa87fafbb/Untitled%201.png)

- [ ]  what are *directions?*

"If you want to visualize features, you might just optimize an image to make neurons fire."

- this seems to be what is sometimes done from primitive times
- "Unfortunately, this doesn’t really work. Instead, you end up with a kind of neural network optical illusion — an image full of noise and nonsensical high-frequency patterns that the network responds strongly to."
    - high frequency patterns I assume means the eyes everywhere in a picture that is activating a particular neuron in imagenet classifier
- [ ]  is this deepdream?
- they do seem interesting but not productive is the impression I get