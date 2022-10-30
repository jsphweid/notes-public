# develop game plan

Status: Completed

### NOTE on breaking down MIDI

Need a better way of breaking apart MIDI eventually but for now we probably don't have to worry about this if we are going for MVP. As long as we have a consistent interface of what happens with the MIDI once it's broken down, it should be fine...

For now we can use the current process of breaking down MIDI and simply upload things to S3/DynamoDB under the new schema

- [ ]  need to convert back into real MIDI, it's just easier to work with than JSON midi
- [ ]  need to have metadata attached that contains start/stop/difficulty/type/etc.

## Data

- midi_segments
    - types
        - monophonic
        - polyphonic
        - drums
    - file should be stored as midi in S3
- audio_recordings
    - ideally stored in a compressed format in S3
        - option to stored as high quality...?

## High Level

- [ ]  reorganize db to work with dynamodb and think about future proofing some things
- [ ]  change midi-segmentizer to just output / upload midi and metadata to s3/dynamodb
- [ ]  change API to just deal with s3 links and such
- [ ]  change FE to just download MIDI then translate to json midi