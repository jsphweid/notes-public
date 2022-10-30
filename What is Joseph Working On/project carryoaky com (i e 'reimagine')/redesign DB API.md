# redesign DB/API

Status: Completed

# Overview

make it use DynamoDB somehow instead of SQL. NOTE: only do this in workbench!

# TODOs

- [ ]  look at all the functionality that already exists
- [ ]  design a dynamodb around it with Nosql Workbench
    - access patterns
        - [ ]  add new piece
            - piece has bits/parts, which are MIDI (maybe they can be stored in the database as blobs?)
            - must store some information that says where each bit should go, some sort of master list
            - NOTE: be aware of the size limit of 4KB I think... do small MIDI bits ever get that high?
        - [ ]  randomly select bit
        - [ ]  upload new performance
        - [ ]  compile random performance (has this been done before)
    - [ ]  
    
    [[re imagine access patterns]]
    
    - [ ]  investigate very lightly - all performances could be reduced down to a hash and could be reused across pieces.. except that could be added later as a secondary index...?