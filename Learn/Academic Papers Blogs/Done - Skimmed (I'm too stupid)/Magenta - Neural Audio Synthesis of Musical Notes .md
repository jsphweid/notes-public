# Magenta - Neural Audio Synthesis of Musical Notes with WaveNet Autoencoders (2017)

[[1704.01279.pdf]]

[[nsynth_audio_examples.zip]]

1. Instead of relying on various types of traditional synthesis (arrangement of oscillators, or FM Synthesis, Granular Synthesis, etc.), you can generate raw samples using only Neural Nets
2. "Further, we show that this model can learn a semantically meaningful hidden representation that can be used as a high-level control signal for manipulating tone, timbre, and dynamics during playback."

Introduces [[NSynth Dataset]] and a new [[WaveNet ]] -style autoencoder that learns [[Temporal (Hidden) [[Codes]] Codes]] which "capture[s] longer term structure without external conditioning"

This is different from WaveNet and other [[Autoregressive Model]] because this new thing "doesn't rely on external dependencies"

- [x]  what are external dependencies here (later "external conditioning")?
    - in the context of speech that long-range structure can
    be enforced by *conditioning on temporally aligned linguistic features*
- [x]  still vague, more..>?
    - what I think they mean is that they don't want "babbling" — they don't want to cues to get sensible output

Says it has WaveNet-like Encoder and a WaveNet Decoder

- [ ]  what is an encoder/decoder here?
- [ ]  are they collectively known as an autoencoder?

The encoder "infers hidden embeddings distributed in time"

- [ ]  what does this mean?

The decoder apparently uses the embeddings to reconstruct the "original audio"

- [ ]  how does it do that?
- [x]  why is it reconstructing "original audio"? isn't it supposed to make something new?
    - I think this is part of the training → the purpose is to find something that encodes and decodes to the original

# Autoencoder

### motivations for a custom one

- primary - "consistent long-term structure without external conditioning"
- secondary - "use learned encodings for applications such as meaningful audio interpolation"
    - encodings are like NN-trained layers information but have utility elsewhere
        - they have a form understandable to humans? or designed by humans
        

### how the original [[WaveNet ]]  autoencoder worked

- having a stack of [[Dilated Convolution]] s predicting the next sample results in babbling (?) because there is a lack of longer term structure, but somehow that paper, it showed that speech "long-range structure can be enforced by conditioning on temporally aligned linguistic features"
    - [x]  what in the hell does this mean?
        - temporal - ~~worldly as opposed to spiritual affairs, secular,~~ but most likely, **related to time**
        - temporal alignment - seems to mean aligning things together in time
        - temporal sequence - such as speech and music — at this point I think it is synonymous with digital audio sequence — i.e., digital time-based sonic/pressure variations captured
        - linguistic feature - assuming this is more related to phonetics, it probably means something about articulation
            - from a video, it means "phoenemes, intonation, punctuation"
            
            ![[/Untitled.png]]
            
        - "We call it a ‘temporal encoding’ because the result is a
        *sequence* of hidden codes with separate dimensions for
        time and channel."
            - Not completely sure what this means, but maybe it's placing importance on the time being separate?
    - [x]  if it means something to the effect that long-range structure can be enforced when you train on articulations that are aligned correctly, I still don't quite know what that means...
        - [x]  somehow this means external conditioning...?!?!
    - [https://vimeo.com/240608327](https://vimeo.com/240608327)
        - "with external conditioning, produces coherent sound"
            - [x]  maybe it takes it the pronunciation tool in a dictionary (for example)?
                - it probably takes in a sentence or whatever expressed as a sequence of pronunciations
        - for music it could be "midi or sheet music" but what if the model could produce its own conditioning - this is what fueled [[NSynth Dataset]]?
            - [ ]  how did it "fuel" NSynth? (did they use "fueled"?)
            - On the subject of the dataset, I don't immediately know how even having a dataset like this enables notes to connect together well... Even though it only has those few one-shot recordings, it's able to make notes longer or shorter than that — probably because the NN captures the timbre and inference just keeps making samples (doesn't pay attention to the notes duration?)
            
        
    
    ### more...
    
    autoencoder
    
    - raw audio → embedding
    - raw audio → causal shift → decoding
    - [ ]  what exactly does this mean or do?
    
    something about latent variables that I did not understand
    
    ### more info
    
    [https://magenta.tensorflow.org/nsynth](https://magenta.tensorflow.org/nsynth)
    
    from [https://www.youtube.com/watch?v=y8mOZSJA7Bc](https://www.youtube.com/watch?v=y8mOZSJA7Bc):
    
    more or less a quote: conditional wavenet that's also an auto-encoder to do timbre modeling. we feed in the model both through the wavenet to do next step prediction but also to an encoder that maps it to a lower dimensional representation and conditioned the wavenet on that encoder so it can decode better. then we have a latent representation of our audio that we can start manipulating, creating our own sounds or "jiggle" the various latent factors and see what happens