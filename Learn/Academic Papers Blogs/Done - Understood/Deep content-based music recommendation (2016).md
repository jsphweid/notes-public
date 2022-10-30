# Deep content-based music recommendation (2016)

[[44b7cf35a3b8bdc12fb1967624a38f257a42.pdf]]%20e2e58c18a7a54b71a27a578fe04658bd/44b7cf35a3b8bdc12fb1967624a38f257a42.pdf)

Using [[Latent Factors Variables]] in music audio to make recommendations.

Uses the [[Million Song Dataset]] but extended with 29-second bits of raw audio possibly (licensing most likely)

I think they use MIR techniques to gather these latent factors possibly.

Nonetheless, initially they talk about using playcount statistics

Then they talk about using CNN and traditional MIR approaches to group songs that are similar (where 'usage' data doesn't exist)

### MIR Approach

1. extract local features from audio using MFCCs
2. "vector quantize" them
3. aggregate into Bag of Words representation
    - [ ]  seems like making vectors (like word vectors) where each dimension is learned using K-means?
4. reduce size with PCA
5. use traditional regression techniques to map the feature representation to [latent] factor

### CNN Approach

1. use log-based mel-spectrogram (similar to above MFCCs)
2. train network on 3 seconds of randomly sampled audio
    - [ ]  is this raw audio or spectrogram?
3. looks like it may get several chunks and averages them together?

Once we have the latent factors, we can apparently use this to make tags or whatever, but I got lost somewhere in here...