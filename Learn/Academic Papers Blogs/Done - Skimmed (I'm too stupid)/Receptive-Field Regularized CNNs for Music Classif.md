# Receptive-Field Regularized CNNs for Music Classification and Tagging (2020)

[https://arxiv.org/pdf/2007.13503v1.pdf](https://arxiv.org/pdf/2007.13503v1.pdf)

CNNs don't do that great of a job in music like they do in vision, and the paper is going to describe why.

The generalization ability of CNNs is related to their RFs (Receptive Fields), whatever that means

CNNs can do a much better job (event better than more complex models) with specific tasks if they use [[Regularization]]  techniques

- Receptive Field Regularization
- Shake-Shake Regularlization

"inductive bias introduced to the architectural design of the CNN"

### Receptive Field Regularization

In biological terms, the RF is the information that a **single cell** has access to. For example, even though we perceive an entire field of view with our eyes, a single neuron in our visual system doesn't have access to the entire field of view, but only a small portion — the receptive field.

In deep learning, it's similar. In CNN layers, a neuron has only access to a limited portion of the data from the previous layer.

RF Regularization is maybe reducing the size of the RF gradually the deeper the layers progress?

### Shake-Shake Regularization

Honestly, no idea

# Applications

### Emotion and Theme Detection

multi-label auto-tagging task