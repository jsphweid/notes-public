# ponder these issues

Status: Completed

# Misc thoughts

way to validate types
everything should be single arg js object
convert types
validate types and convertible
talks about loss between types (float to integer)
- float to int -> potentially lossy
- int to float -> never lossy

focused on providing a definitive API that is well documented and strict and

capture usage

should abstract from the details of the function/library

converts and adapters to go between types

compiler that compiles the graph/pipeline, validates, verifies

function dns

- have a server that resolves function queries and determines where to execute them, this can later be cached for a time, like DNS

this is becoming too complicated, what's the MVP

maybe we should start with the frontend first

# Attempting to simplify

Functions should be cataloged

- what it accepts as input
    - easy
    - defined as ts type, proto, or graphql schema
- what it returns as output
    - easy
    - defined as ts type, proto, or graphql schema
- description
    - easy
- place to run it
    - hard
- how to run it
    - hard

hard

Adapters → connect inputs

where do adapters run though?

# Terminology

pipeline == graph

function == node

# Questions

design is not complete

- [ ]  how can we start with something simpler
- [ ]  does the whole graph execute client or server side
    1. managed client-side
        - pipeline gets compiled and client *manages* the pipeline execution by sending/receiving requests/responses for each fn as it executes
        - pros
            - could be more flexible by allowing certain things to execute locally and others to execute remotely
        - cons
            - can get into situations where some things fail and others don't and the user is aware of that
            - lots of network IO sending stuff back and forth, and it would be lots of complexity to minimize that
    2. managed server-side
        - pipeline gets compiled and sent to server along with all the inputs to the pipeline and simply get results back
        - pros
            - would be more efficient usually (unless everything could run locally, without network IO) because there are no requests being sent to a server
            - would be simpler to design possibly
        - cons
            - if we wanted to run it locally, pretty much every function would have to run locally, functions would have to be "local-compatible"
- [ ]  how could we build this so most of it's open source?
    - limit to only doing everything client-side, every part of graph returns promise still though, and you can make your own remote calls somehow
    

### IT HAS TO START SMALLER THAN THIS

taking a break to learn networking