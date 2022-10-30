# Learning Features from Music Audio with Deep Belief Networks (2010)

[[paper.pdf]]

Abstract -  use Deep Belief Network on fourier transform, then use the "activations" from the trained network as inputs in Support Vector Machines. Performance is better than MFCCs in — for example — genre recognition.

So obviously raw audio data needs some work to derive any information from it. That's where feature extraction comes in. We need to transform that raw data into something usable. Fourier transforms, filters, etc. are all tools that can chip away at raw audio — creating features that can then be used as inputs to some other system that does things like genre detection. This paper seems to be about making learned system that just creates features from raw audio. It says "for a given task" however. IE it's probably not going to make an NN that can create features for general music purposes.

In this paper, the Deep Belief Network performs unsupervised learning which more or less sets the weights up for success so the supervised training on a specific task goes more successfully.

Honestly it doesn't seem like much insight has come from this paper. This research happen too long ago and it seems like many more advancements have been made sense.