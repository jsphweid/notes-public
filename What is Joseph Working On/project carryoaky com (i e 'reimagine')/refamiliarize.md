# refamiliarize

Status: Completed

reimagine-app

- FE app obviously

reimagine-api

- Query
    - getUserSettings
    - getSegment
- Mutation
    - createUserSettings
    - updateUserSettings
    - postRecording
    - postMidi
    - createMixFromRecordingFragments
- has a synth lambda but isn't this what reimagine-mixer-go does?
    
    

reimagine-mixer-go

- honestly should probably just rewrite this in python, if at all. I think there is value in this app in just being able to download the raw files and just mix them together in cubase... would need timings though

reimagine-graphql-lambda

- NOTE: I'm guessing this is just an old artifact and can be deleted
- Query
    - segment
- Mutation
    - postRecording
    - postMidi

probably should just monorepo this up