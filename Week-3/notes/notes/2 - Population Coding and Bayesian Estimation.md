![](http://geekresearchlab.net/coursera/neuro/neuro-decision-21.jpg)
```
Here, we will discuss on decoding from many neurons through population coding.
```
![](http://geekresearchlab.net/coursera/neuro/neuro-decision-22.jpg)
<br<br>
![](http://geekresearchlab.net/coursera/neuro/neuro-decision-23.jpg)
```
The ath neuron has a preferred direction where the response is maximum that is denoted by the angle Sa or vector Ca.
```
![](http://geekresearchlab.net/coursera/neuro/neuro-decision-24.jpg) <br><br>
![](http://geekresearchlab.net/coursera/neuro/neuro-decision-25.jpg) <br><br>
![](http://geekresearchlab.net/coursera/neuro/neuro-decision-26.jpg)
```
Question:
In this equation, 
we normalize the contribution of each neuron to the population vector by its maximum firing rate. 
Why do we do this?
Answer:
Some neurons have an intrinsically higher firing rate and we want each neuron to contribute to the population vector in a way that is proportional to its relative activation.
Explanation:
When combining the effects of several neurons, we want to take into account that the neurons have intrinsic differences independent of the stimulus. 
For instance, if a neuron's maximum firing rate is 10Hz, and we observe an average of 9Hz in the presence of a particular stimulus, we should recognize this as a stronger response than if we had observed a 9Hz average rate for a neuron whose maximum firing rate is 100Hz.
```
![](http://geekresearchlab.net/coursera/neuro/neuro-decision-27.jpg)
```
There are also some limitations experienced in the population coding.
```
![](http://geekresearchlab.net/coursera/neuro/neuro-decision-28.jpg)
```
At first, we will focus on the posteriori distribution and likelihood function.
```
![](http://geekresearchlab.net/coursera/neuro/neuro-decision-29.jpg) <br><br>
![](http://geekresearchlab.net/coursera/neuro/neuro-decision-30.jpg) <br><br>
![](http://geekresearchlab.net/coursera/neuro/neuro-decision-31.jpg) <br><br>
![](http://geekresearchlab.net/coursera/neuro/neuro-decision-32.jpg)
```
Question:
What is the standard deviation of a poisson neuron with an average firing rate of r?
Answer:
√r
Explanation:
The variance of a poisson distribution is equal to the mean and the standard deviation is the square root of the variance. 
Therefore, if the mean firing rate is r, the variance is equal to r, and the standard deviation is equal to √r
```
![](http://geekresearchlab.net/coursera/neuro/neuro-decision-33.jpg)<br><br>
![](http://geekresearchlab.net/coursera/neuro/neuro-decision-34.jpg)<br>
![](http://geekresearchlab.net/coursera/neuro/neuro-decision-34-1.jpg)<br><br>
![](http://geekresearchlab.net/coursera/neuro/neuro-decision-35.jpg)<br>
![](http://geekresearchlab.net/coursera/neuro/neuro-decision-35-1.jpg)<br><br>
![](http://geekresearchlab.net/coursera/neuro/neuro-decision-36.jpg)<br><br>
![](http://geekresearchlab.net/coursera/neuro/neuro-decision-37.jpg)
```
Question:
If the likelihood distribution is P(A|B), 
what is the a posteriori distribution?
Answer:
P(B|A)
Explanation:
Sorry for all the Latin phrases! Mathematicians love that stuff.
Remember that with Bayesian reasoning, we start with an initial belief about a distribution of something, we call that the "prior" distribution. 
As we collect new evidence, we can adjust our belief. 
Our belief after adjusting for the new evidence is called the "a posteriori" distribution. The likelihood tells us how likely we are to observe our evidence, given the various possible values of the thing we are concerned with, which is something we taken into account while estimating the posterior distribution. 
Bayes Rule tells us precisely how we can take that likelihood into account to come up with the posterior.

In the case of this question, our prior would be P(B). Our evidence is represented by A, and the likelihood of our evidence is P(A|B). 
In the Bayes Rule formula, it is P(B|A) that plays the role of the posterior.
```
```
So, we can use Bayes Law to write the likehood, prime and sum used in the posteriori.
```
![](http://geekresearchlab.net/coursera/neuro/neuro-decision-38.jpg)<br><br>
![](http://geekresearchlab.net/coursera/neuro/neuro-decision-39.jpg)<br><br>
![](http://geekresearchlab.net/coursera/neuro/neuro-decision-40.jpg)
