# Audio Set; An Ontology and Human-Labeled Dataset for Audio Events (2017)

[[audioset.pdf]]

A paper that introduces a dataset, compiled from sounds on youtube - 10 second clips across 632 "classes" "guided by literature and manual curation"

Ontology - a graph of concepts/categories of a subject area and relationships between them

They found their classes by looking at web-text, crawling and discovering large amounts of words that have "sound" as their primary ancestor (or something like that)

![[/Untitled.png]]

But they can go 6 layers deep

## Conclusion

looks like they provided VGGish (like VGG-ish - [[VGG]] ), which is a bunch of 128-dimensional vectors/embeddings of each AudioSet category

- "produced from a VGG-like audio classification model"