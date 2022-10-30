# Tensorflow serving function

`serving_input_receiver_fn` A function that takes no argument and returns a `tf.estimator.export.ServingInputReceiver` or `tf.estimator.export.TensorServingInputReceiver`

Read more [here](https://stackoverflow.com/questions/52874647/tensorflow-v1-10-why-is-an-input-serving-receiver-function-needed-when-checkpoi)

Each phase of NN (train, evaluate, inference) has a different input function. Inference only requires the serving input function.

It needs to add placeholders to the graph and do any other preprocessing.

"If you're going to pack the data in a (serialized) tf.Example (which is similar to one of the records in your TFRecord files), your serving input function will have a string placeholder (that's for the serialized bytes for the example) and will need a specification of how to interpret the example in order to extract its data."