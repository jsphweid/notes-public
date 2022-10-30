# Short-Time Forier Transform

Like DFT, but it segments/windows as to see the evolution of a signals frequencies

window size - number of samples we apply windowing to

frame size - number of samples that we consider in each chunk of the signal

hop size - how many samples the window slides

usually the same 

sometimes the frame size is bigger

bin is sometimes referred to as frame??? although frame is confusing because it means something different in the time domain. frame can also mean window though.

The DFT gives us coefficients for the whole input, but STFT gives us those for each frame, so it has an extra dimension.

windowing function - hann window used often... but why...?

- supposed to avoid spectral leakage??

So you can simply ignore everything else outside the window by using a rectangular window function (setting everything outside to 0) but these better windowing functions attenuate boundary effects.