# Unsupervised Neural Generative Semantic Hashing (2019)

[[1906.00671.pdf]]

Using Variational [[Autoencoder]] to reduce a document down to a hash, which I assume at this point is something created in the latent space.  I'm not exactly sure how we go from latent variables → hash code, but apparently once we have these codes (binary vectors), we can easily find similar documents by looking for other codes with a small Hamming distance

Related: [https://www.youtube.com/watch?v=3BDc0H9C9dw&t=1s](https://www.youtube.com/watch?v=3BDc0H9C9dw&t=1s)

Seems like there is a lot of research in this area of semantic hashing, but this paper just brings more performance, simplicity in final hash length result, and ranking, hence: Ranking Based Semantic Hashing (RBSH).

The ranking component uses "weak supervision" (labels are obtained automatically without human annotators or any external resources). In this case, those labels are "document triplets" which seems unclear to me at this point. It looks like it compares the current document to two others? Looks like they use STH (Self-Taught Hashing) and rank by similarity based on Euclidean distance between two has codes. So in other words, it just uses another algo to compute ranking distances as the "supervised part"