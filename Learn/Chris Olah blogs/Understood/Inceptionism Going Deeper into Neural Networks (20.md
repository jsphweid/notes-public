# Inceptionism: Going Deeper into Neural Networks (2015)

[https://ai.googleblog.com/2015/06/inceptionism-going-deeper-into-neural.html](https://ai.googleblog.com/2015/06/inceptionism-going-deeper-into-neural.html)

similar to [[DeepDream]] it seems

I'm not immediately sure about exactly this process occurs.

"Say you want to know what sort of image would result in “Banana.” Start with an image full of random noise, then gradually tweak the image towards what the neural net considers a banana (see related work in [1], [2], [3], [4]). By itself, that doesn’t work very well, but it does if we impose a prior constraint that the image should have similar statistics to natural images, such as neighboring pixels needing to be correlated."

Not immediately sure what that means.

from this video: [https://www.youtube.com/watch?v=BsSmBPmPeYQ](https://www.youtube.com/watch?v=BsSmBPmPeYQ)

- start with a pre-trained network (some image net classifier)
- modify the network in such a way that the loss changes the image
- so passing an image of a landscape, having it go through all the layers, creating representations and finally outputing a "landscape" prediction, tell it instead that it was a cat. It will calculate an error that's pretty big at first. But then we're going to backpropagate back to the original image and *change the image* somehow so that the loss is less the next time
- MAYBE... Actually this *doesn't* seem to be what the video is doing exactly...
    - [x]  what is it doing exactly?
        - look at [[Feature Visualization [[(2017)]]]]