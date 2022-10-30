# Collaborative Filtering

technique used by recommender systems...

- [ ]  how is it different from any other prediction algorithm
    - perhaps it's because there is some degree of indirection(?) involved i.e. instead of looking at your own purchases and predicting the next purchase, it compares you to other people — finding people with similar habits and using that data for you
    - you need a lot of data to make a prediction, but when there is sparse data, you can "collaborate" with other people's data and effectively get the benefit of big data
        - maybe like how a NN-based speech-to-text translator can be more effective when you prime it with some data from your voice (in addition to the actual training data). **CF seems to be strictly non-NN based, however**
    - varies from Content-Based filtering: [https://medium.com/@medfordxie/neighborhood-vs-latent-factors-methods-in-collaborative-filter-recommender-systems-part-1-9f969c4990b0](https://medium.com/@medfordxie/neighborhood-vs-latent-factors-methods-in-collaborative-filter-recommender-systems-part-1-9f969c4990b0)
        
        
        ![[/Untitled.png]]
        
- [ ]  how does it do it?
    - I don't know

challenges

![[/Untitled 1.png]]

another explanation here: [https://youtu.be/4-f77HjB_CI?t=510](https://youtu.be/4-f77HjB_CI?t=510)

# Types

![[/Untitled 2.png]]

### Neighborhood

Seems to be more focused on just comparing users against users or items against items

### Latent Factor Model

In LF, you compare the features that the users have an affinity against features that *items* have an affinity for. 

- [ ]  what? lol
- I don't really know what this means other than it seems to be focused on comparing specific *features* (i.e. probably [[Latent Factors Variables]])
- and it involves putting users and items in the same space somehow