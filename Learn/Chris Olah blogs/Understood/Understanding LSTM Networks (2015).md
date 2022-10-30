# Understanding LSTM Networks (2015)

RNNs have a problem because they can't look back *that* far. In theory they can, but in practice they don't. 

Enter LSTMs...

The key to LSTMs is the cell state. Regular RNNs don't have that. They only have the previous input combined with the current (?)

1. Forget gate - determines how much of the previous state to keep or throw away... this is the value of the previous hidden layer (?) multiplied by what's coming in plus a bias then sigmoided for a 0-1 value to multiple that A. by
2. New information - 2 different layers that decide what new information goes in