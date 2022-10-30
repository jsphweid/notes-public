|access patterns|table/GSI|key conditions|example|notes|
|---|---|---|---|---|
|get all MidiSegments for a piece|table|PK=piece where SK begins_with MidiSegment|,|
|get all AudioRecordings for a piece|table|PK=piece where SK begins_with AudioRecording|,|
|get all AudioRecordings for a MidiSegment|GSI1|MidiSegment=midisegment|,|
|get random MidiSegment|,,|"get random piece, then get random segment"|
|get random MidiSegment for a piece|,,|"get all "|
|get user settings by id|table|PK=user ID where SK=user ID|,|
|get mixes by piece id|table|PK=piece ID where SK begins_with Mix|,|
|get mixes by user id|,,|"should be batch processed, cache on table if necessary"|
|get all AudioRecordings for a user|GSI2|PK=user ID where SK begins_with AudioRecording|,|
|get all Mixes for a user|GSI2|PK=user ID where SK begins_with Mix|,|
|get all Pieces for a user|GSI2|PK=user ID where SK begins_with Piece|,|
|,|,,|