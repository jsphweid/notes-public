# audio engine revamp

Priority: Priority Medium
Size: Size Long
Status: Not started

This code is messy, uses deprecated APIs, only supports mono signals, and is imprecise 

A refactor would be mostly FE:

- [ ]  support stereo audio
    - probably should support mono/stereo
    - if recorded in stereo but is really mono (both channels have same data), it should be converted to mono
- [ ]  don’t use script processor node because it’s deprecated
    - there may be a better way to save buffers while recording, if that’s even still necessary
- [ ]  it’s imprecise... buffers start coming in and startTime is recorded *around the same time* — this probably makes mixes using recordings from the same device relatively correct sounding, but the differences between devices could be fairly large
    - ideally recording starts and the exact second this happens is known
    - *then* everything else begins with *that* start time in mind (or another time can be used as long as we can use the difference later to adjust)
    - also baseLatency is used to adjust the final signal as well
        - I’m not 100% sure what gets factored into this baseLatency or not, however