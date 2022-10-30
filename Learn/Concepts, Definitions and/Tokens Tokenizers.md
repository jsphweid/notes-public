# Tokens / Tokenizers

A tokenizer creates tokens by taking a corpus of text and splitting it into characters then grouping the characters together over and over again until the vocabulary size has been reached. Special accomodations are used for words like "it is" where they commonly appear together but are 2 distinct words — it's normally split at words.

i.e. `tokenizer.pre_tokenizer = Whitespace()`

Vocabulary is basically the set of tokens.

For semi-obvious reasons, a corpus of text that was tokenized a certain way for training a model must use the same exact tokenizing for inference on that model

An appropriate vocabulary size is necessary to limit to some degree because there is a trade off between what is possible to learn and what is possible to host in the model (input/outputs embedding matrix parts). The smallest would be to have each character be a separate token. Since no token would have str length greater than 1, there'd be a very small vocab — maybe like 100-200? (26 letters plus a bunch of special characters). Having it too big (hundreds of thousands) makes it hard to run for performance reasons.

It seems pretty common (or mandatory) for these tokenizer algorithms to be able to provide you with a specific number of vocab. It does this by incrementally building up the number of vocab based on finding things that are increasingly common.

Here are a bunch of different [text tokenizers and how they work](https://huggingface.co/transformers/tokenizer_summary.html)