# A Dataset and Taxonomy for Urban Sound Research (2014)

presents UrbanSound database - "One of the main challenges and hindrances to urban sound
research is the lack of labeled audio data"

presents rigorous taxonomy

![[/Untitled.png]]

I don't like this as much because it imposes too much supervision on the processes. 

Apparently you can just take shit from freesound.org, nice.

Apparently the best performing algorithm was SVM but not sure how it was implemented...

It confused things with obvious frequency space overlap (air conditioners and idling engines, for example), which is expected for such a simple classification algorithm using simple spectrograms (by way of MFCCs)