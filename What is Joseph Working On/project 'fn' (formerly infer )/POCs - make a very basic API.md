# POCs - make a very basic API

Status: Completed
Work Type: BE

# Overview

try to keep the scope for this as small as possible — build it locally only

The big problem here is that a lot of my fns take in files and output files which is problematic to do over HTTP via rest/graphql. There are many different ways of doing this and most of the solutions are outside of what I'm used to

Uploading through S3 is a bad idea because I don't really want to have to persist all files ever processed as that would quickly get out of hand... Then I have to pay extra storage and transfer fees plus it introduces more latency.

What I don't want to do ideally is build something that's going to just be tech debt the next time I think more about this

# Ideas

1. python only approach (probably easiest) - construct a basic graphql/rest API, probably using graphene
    - I need to understand how good/bad it is to work with files in graphql before I go to far
    - [ ]  need a POC on how this feels
2. python / ts approach
    - wrap all python stuff as a grpc service and then build a ts graphql service that talks to it — obviously they'd run on the same cluster in a production setting
    - the ts service could be in charge of a lot of other things in the future, like if someone wanted to persist the inputs/outputs, auth, etc.
    - seems like a better approach than #1 long term
    - [x]  also needs a POC
        - NOTE: I'm going with this approach for now... will make the gql part in another card...

QUESTIONS to answer:

1. wasn't there some problem with uploading large files through kub that ES experienced? Ask Hunter about it