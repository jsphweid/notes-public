# Deep Learning for Audio Signal Processing (2019)

[https://arxiv.org/pdf/1905.00078v2.pdf](https://arxiv.org/pdf/1905.00078v2.pdf)

Basically an overview of the whole current state... hope it's good.

Note: I didn't talk about everything here... mostly just stuff related to things I'm interested in...

### Audio Features

MFCCs

log-mel spectrum

constant-q spectrum

spectrogram - temporal

...but these are all designed

### Models

CNNs

RNNs

Seq2Seq

- often not pure seq2seq, but componentized, trained separately
    - conversely, maybe 42-47 offers more hope for that approach though?
        - the "components" are trained jointly in this approach

GANs

Loss Functions?

Phase Modeling

### Data

expanding datasets

- data generation
    - generating from scratch, apparently has difficult with real data
- data augmentation
    - transposition raw audio for example

### Applications

traditionally solved with hand-written algorithms

- transcription - onset/offset detection, fundamental freq estimation
- rhythm analysis
    - beat tracking
    - meter identification
    - downbeat tracking
    - tempo estimation
- harmonic analysis
    - key detection
    - melody extraction
    - chord estimation
- high level analysis
    - instrument detection
    - instrument separation
    - transcription
    - structural segmentation
    - artist recognition
    - genre classification
    - mood classification
- high level *comparison*
    - discovery of repeated themes
    - cover song identification
    - music similarity estimation
    - score alignment

*Which of these have truths that can be scored and evolve using the same system of comparison? For example, with transcription, the notes have a corresponding truth (midi for example). Regardless of whether or not it's a hand-crafted algorithm, ML'ed, etc., we can score it the same and keep results and gradually improvement them using the same result contract.* 

Look at [https://github.com/ybayle/awesome-deep-learning-music](https://github.com/ybayle/awesome-deep-learning-music) for more...

- source separation
    - single channel -
    - multi channel - obviously easier as the spatial element is a very helpful contributor
- enhancement
    - noise reduction
    - speech quality improvement
- generative models

"all tasks in all audio domains face relatively small datasets, posing a limit on the size and complexity of deep learning models trained on them." BINGO BANGO

Read "Data Requirements" more........