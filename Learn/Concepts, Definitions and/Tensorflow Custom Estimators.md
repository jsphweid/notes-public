# Tensorflow Custom Estimators

deprecated but still useful to understand if you need to make a SavedModel

input fn - depends on what it is for (serving, training, etc.) but generally takes in features and maybe labels/batch-size depending on the task.

- returns as Dataset stream of sorts for train/eval