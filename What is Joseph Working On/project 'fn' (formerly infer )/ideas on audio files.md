# ideas on audio files

The question is, what do we ship back and forth over http?

- raw audio data, the most universal and portable, but can't benefit from compression
- bytes, probably the most compact depending on file type format
    - complication - what do we give back if it's a send/receive audio operation?
- base64, not as good as bytes, but simple as it can be represented as string