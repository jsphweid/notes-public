# Mel Scale

comes from "melody" - because the scale is based on pitch comparisons

seems similar to "decibel" (of which each unit is 1/10 of a "bel")

Basically we humans apparently don't perceive pitch in line with frequency: 200hz → 400hz *sounds like* a much bigger interval than 12000hz → 12200hz. So the Mel Scale provides a mapping that is much more in line with how humans perceive.

When it comes to music, humans manipulate frequencies/hz in ways that sound meaningful to them. In order to convey this importance to an algorithm (I'm guessing), a mel scale/spectrogram is often used in some fashion with learning algorithms (for example, transforming the input).

I'm guessing that theoretically, it should be possible for a computer to do tasks (transcription, genre recognition, etc) with a plain spectrogram, but I'm guessing this makes it faster to obtain convergence.