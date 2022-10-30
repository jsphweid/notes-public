# Data Cleansing with Contrastive Learning for Vocal Note Event Annotations (2020)

[https://arxiv.org/pdf/2008.02069v2.pdf](https://arxiv.org/pdf/2008.02069v2.pdf)

Data Cleansing is making better labels (for supervised learning) by using a NN on that

It predicts incorrectly labeled time-frames trained using likely correct labels pairs as positive examples and local deformations of correct pairs as negative examples

- what are time-frames?

What are these datasets that it mentions??

- LakhMIDI - [[LakhMIDI Dataset]]
- DALI - [[DALI Dataset]]
- Free Music Archive - site that has been bought and sold a few times but basically curates creative commons songs

It shows that DALI is surprisingly not 100% accurate. There are a lot of little errors, some big. Overall it shows that there is a way to estimate how well the 'estimator' works.