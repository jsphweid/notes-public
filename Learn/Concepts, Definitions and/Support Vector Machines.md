# Support Vector Machines

Comes from Support Vector Classifier, which work well when data that is linearly separable

The idea of Support Vector Machines is to move data into a higher dimensional space by some transformation and then the data might be linearly separable, see [https://youtu.be/efR1C6CvhmE?t=642](https://youtu.be/efR1C6CvhmE?t=642)

see here: 

![[/Untitled.png]]

Note how the problem isn't naturally linearly separable, but after applying some function, it is (very similar to how NNs work it seems except this is more of an expert driven approach). This is called the "kernel trick" and you can use multiple kernels with various parameters (and parameters can be tuned with techniques like K-Fold Cross Validation)

"Support Vectors" are the vectors/lines that push up against the margin between data points

- see below for an easy 2d example: Notice the [[Hyperplane]]

![[/Untitled 1.png]]