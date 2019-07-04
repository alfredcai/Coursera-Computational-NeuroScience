![](http://geekresearchlab.net/coursera/neuro/n-1.jpg)
```
Each bit of information specifies location by additional factor of 2.
```
```
Entropy is the average information of a random variable.
It measures variability.
It computes a number of yes/no questions.
```
![](http://geekresearchlab.net/coursera/neuro/n-2.jpg)
```
Question:
Can you speculate how many bits of information are required to locate your car (the old-fashioned bug) either by calculating or by intuition?
Answer:
3
```
Explanation: <br>
![](http://geekresearchlab.net/coursera/neuro/n-3.jpg)
<br>
<code>In the above diagram, there was a minus missing in the 4th line before 1/8.</code>
<br>
<br>
![](http://geekresearchlab.net/coursera/neuro/n-4.jpg)<br><br>
![](http://geekresearchlab.net/coursera/neuro/n-5.jpg)<br><br>
![](http://geekresearchlab.net/coursera/neuro/n-6.jpg) 
```
Back to spike code: Stimulus??
From the below diagram,
Entropy tells us about the intrinsic variability of outputs.
But, we need to consider the stimulus and how it's driving the responses.
The stimulus can one in perfect direction where each of them is perfectly encoded.
Let r be spiking response and s be the stimulus.
Everytime, there is a stimulus, we will get a spike.
```
![](http://geekresearchlab.net/coursera/neuro/n-7.jpg)<br><br>
```
let q be the error probabilty.
```
![](http://geekresearchlab.net/coursera/neuro/n-8.jpg)
<br><br>
![](http://geekresearchlab.net/coursera/neuro/n-9.jpg)
```
On below diagram,
Now, going back to binomial calculations,
And see how the mutual information depends upon the noise.
p => maximizes the entropy
Let's assume that noise is as same as for the spike and silence keeping the value to be q.

So, this should be intuitive.

As error grows larger, the spiking is less likely to appear 
where the mutual information decreases.

When q = 0.5, then there is no mutual information between r and s.
```
![](http://geekresearchlab.net/coursera/neuro/n-10.jpg)
```
Question:
If the stimulus and response are independent events with their own probabilities, p(s) & p(r), 
what is p(r|s)?
```
![](http://geekresearchlab.net/coursera/neuro/n-11.jpg)
```
Answer:
p(r)

Explanation:
Because there is no relationship between response and stimulus.
```
```
From the above same diagram,
Question:
If p(r|s) = p(r), 
what is the mutual information (MI) of r and s?
Answer:
0
Explanation:
Recall that when p(r|s) = p(r), 
r and s are independent because the statement tells us that knowing s does not help us narrow down what r could be. 
Because s does not reduce the level of uncertainty about r, it is said that s gives us no information about r. 
Thus, the mutual information of r and s is 0. 

Note that the word "mutual" refers to the fact that the relationship between two variables can be viewed both ways: 
if knowing r reduces uncertainty about s, then knowing s necessarily reduces uncertainty about r by the same amount. 
Thus, when we quantify this reduction in uncertainty we call it "mutual information."
```
```
The 2 questions refers to Part 1 in that diagram...
Summarizing Part 1,
Noise entropy is equal to the total entropy.
The MI is zero.
Coming to Part 2,
At the opposite extreme,
The response is perfectly predicted by the stimulus.

In this case, the noise entropy is 0,
So, the MI will be given by the total entropy of the response.
All the responses coding capacity is used in encoding the stimulus.
```
![](http://geekresearchlab.net/coursera/neuro/n-12.jpg)
<br><br>
![](http://geekresearchlab.net/coursera/neuro/n-13.jpg)
```
Below diagram,
P(r,s) = joint distribution
P(r)P(s) = marginal distribution
It can be rewritten using conditional distribution
Hence, totally computed.
Thereby, the information is completely symmetric.
```
![](http://geekresearchlab.net/coursera/neuro/n-14.jpg)
```
A small recipe for calculating...
```
![](http://geekresearchlab.net/coursera/neuro/n-15.jpg)
```
In the next part, we will discuss on calculating information in spike trains...
Two methods were being used...
--- Information in spike patterns
--- Information in single spikes
```
