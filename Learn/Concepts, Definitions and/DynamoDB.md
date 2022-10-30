# DynamoDB

primary key ⇒ partition key + sort key (composite). Don't need a sort key if the partition key is unique. If it's not unique, then the combination of partition key + sort key must be unique. Every ITEM must have a unique primary key. If you need to get everything in a partition, you just give it the partition key. GSIs aren't unique though.

sharding with random / hash keys at end

- when writing, put a random number on end (say 0-200)
    - then when you retrieve everything, you just go in order 0-200 at end to evenly distribute reads
- if you need to obtain specific values, then make the 0-200 computed
    - for example an ID rental_id/order_id/etc. use mod 200 + 1 to get something predictably down to 0-200
    

projection

- attributes copied from a table into a secondary index — more storage / write costs