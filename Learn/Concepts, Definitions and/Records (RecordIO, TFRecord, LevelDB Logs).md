# Records (RecordIO, TFRecord, LevelDB Logs)

what are these things and why are they so special?

Reading [this](https://towardsdatascience.com/a-practical-guide-to-tfrecords-584536bc786c) on TFRecords

- it sounds like it’s faster because there is overhead with switching files on disk. So if you have a dir of thousands of small files and you want to load all of them and feed them through something, the mechanism has to do a lot of work just jumping to the right place for each file. Whereas with Records you can read a bunch of data contiguously