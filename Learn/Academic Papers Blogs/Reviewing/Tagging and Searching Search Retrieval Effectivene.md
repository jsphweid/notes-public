# Tagging and Searching: Search Retrieval Effectiveness of Folksonomies on the World Wide Web (2007)

[[tagging-and-searching.pdf]]

Taxonomy - practice and science of categorization/classification

folksonomy - end users tag stuff for themselves

- also called collaborative tagging, social classification, social indexing
- more bottom up than top down, messier but more real
- less hierarchical
- twitter hashtags

DOWNSIDES: open for abuse as you can game SEO a lot easier

study found that results of search engines with folksonomy overlap provided highest relevance

Focuses on [Delicious](https://en.wikipedia.org/wiki/Delicious_(website)) which the modern equivalent probably being [https://pinboard.in/](https://pinboard.in/) 

Reddit has some similarities — the ranking is largely determined by users

### misc other studies

old old study but still hold true probably. People generally:

- use short queries
- only look at first 10 results
- do not modify their query

A lot of these studies have humans making query, getting search results from multiple providers (without knowing which are which) and ranking results.

Apparently good search engines were significantly better than the worst

overlap in results of different systems generally means higher relevance but at least in these early studies there wasn’t a ton of overlap occurrences

talking about operators which I believe are things like “site:” or maybe “logical” operators means otherwise?

Ways to measure these things:

- precision - number of relevant results from the system divided by total number of items retrieved
    - [x]  what does this really mean
        - it’s not the whole collection, only the results returned, so when analyzing 20 results, how many were relevant out of the 20?
- recall - dividing number of relevant results retrieved by number of relevant documents in whole collection
    - hard to do without knowing how many are in the collection
    - but a relative measure could be num relevant from one IR system divided by total num relevant results from all IR systems
- relevance
- SQM - Search Quality Measure -
    - implicit
    - the order that they clicked the results
    - time spent examining the documents
    - more…

## The study

Only social bookmarking systems that allowed searches constrained their own collections were used.

results from 8 different sites were ordered randomly — ordering effect was considered minor

1. search engines (like Google)
2. directories  (like DMOZ or Yahoo Directory)
3. folksonomies (like Delicious)