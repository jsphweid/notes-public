# look into breaking apart MIDI

Depedency: [[]] 
Status: Completed

# TODOs:

- [ ]  look what I was doing before
    - [https://github.com/jsphweid/midi-segmentizer](https://github.com/jsphweid/midi-segmentizer)
        - honestly, I put a fair amount of work into this...
        - HOW IT WORKS BASICALLY
            - reads into absolute time MIDI, extracts bpm and midi also
            - divides into tracks
                - can you have polyphonic on one track?
            - group notes on rests
- [ ]  work out a good way going forward
    - you should be able to extract certain MIDI notes
        - take those out and make MIDI tracks then split the rest randomly?
- [ ]  write automation to make it easier in the future? (or if it's not too much work, just do it in another card?
- [ ]  optional arg to have repeated bits (same midi content) not duplicated when adding to DB
    - they may be different sections, but if they are the exact same notes with the exact same character, you should be able to sub them in. In fact, it might be preferable