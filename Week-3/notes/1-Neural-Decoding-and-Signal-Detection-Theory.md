```
How well can we learn what thw stimulus is by looking at the neural responses?
It is "Decoding".
```
```
Making a decision:
```
![](http://geekresearchlab.net/coursera/neuro/neuro-decision-1.jpg)
```
From the diagram,
If a monkey is looking at these dot patterns, 
then as the dot patterns move in one direction, 
then the monkey eyes too move in the same direction.

The challenging thing is predicting the direction of the dot patterns.
Sometimes, we can't say or predict which way are they going.

When the dot patterns move randomly in their chosen direction, then it's 0% coherence.
At one extreme, there is a stimulus where the dot patterns move altogether, then that's 100% coherence.
```
```
Prediciting from neural activity:
```
![](http://geekresearchlab.net/coursera/neuro/neuro-decision-2.jpg)
```
The experiment was done in monkey's brain by counting the spikes for doing prediction analysis from it's neural activity.
From the diagram,
Distribution plotting:-
The dark black colored portion is the "number of trials", where it represents the "upward choices".
Then, the checked portion is the "number of spikes" that represents the "downward choices".

#### Question:
Can you speculate what might happen to these 2 distributions as the coherence decreases?
#### Answer:
They move towards each other.
#### Explanation:
As the number of dots that move together (coherence) decreases the ability of the monkey to distinguish the direction of the group as a whole decreases as well, causing his decisions to be no better than a guess.

```
![](http://geekresearchlab.net/coursera/neuro/neuro-decision-3.jpg)
```
Now, it's changed where the visual information is less that corresponds from left to right.
The firing rates are similiar to the triggered responses.
```
![](http://geekresearchlab.net/coursera/neuro/neuro-decision-4.jpg)
```
For this diagram, where the coherence is almost 0%,
The motion appears to discriminate from left to right where the distributions over-lapses in smaller amounts.
```
```
Now the question is:
How should one decode the firing rate inorder to get the best guess about where the stimulus is moving as upward or downward?
```
```
The above can be answered from the "behavioral performance", that does the decoding.
```
![](http://geekresearchlab.net/coursera/neuro/neuro-decision-5.jpg)
```
For determining the decoding areas of the behavioral performance, we will go for "signal detection theory".
```
![](http://geekresearchlab.net/coursera/neuro/neuro-decision-6.jpg)
```
Here, r is the number of spikes in a single trial.
The probability of responses moving at "upward" is shown in the form of red curve.
The probability of responses moving at "downward" is shown in the form of blue curve.
The upward is represented as p(r|+)
The downward is represented as p(r|-)
```

#### Question:
Where would you put the threshold value?
#### Answer:
At the midpoint between the 2 curves, where their probabilities are equal.

Explanation to the Answer: 
![](http://geekresearchlab.net/coursera/neuro/neuro-decision-7.jpg) 
![](http://geekresearchlab.net/coursera/neuro/neuro-decision-8.jpg) 

#### Question:
Suppose that there is a very large penalty for false alarms, i.e., if you decide that the signal is + when it is in fact -, you pay a very high price (but not necessarily the other way around: there is no penalty for deciding - when the signal is +). Which way would you move the threshold z in order to decrease the chances of having to pay this penalty?

#### Answer:
To the right.

#### Explanation:
The farther you move the threshold to the right, the less probable it is that the negative signal will yield a measurement above threshold. Therefore, you can be almost sure that if a measurement is above threshold, it has come from the positive signal. The consequence of moving the threshold to the right would be that you would label many positive signals as negative. This scenario is discussed at the end of the lecture.

![](http://geekresearchlab.net/coursera/neuro/neuro-decision-9.jpg)
![](http://geekresearchlab.net/coursera/neuro/neuro-decision-10.jpg) 
![](http://geekresearchlab.net/coursera/neuro/neuro-decision-11.jpg)
```
where s is the likelihood.
```
#### Question:

Log(a*B/c)=?

#### Answer:

log(a)+log(b)-log(c)

#### Explainment:

Generally logarithms have a couple properties we can use here. You can use these properties to construct the correct answer.

Property 1: division inside the logarithm:

\text{log}(\frac{x}{y}) = \text{log}(x) - \text{log}(y)log(*y**x*)=log(*x*)−log(*y*)

Property 2: multiplication inside the logarithm:

\text{log}(xy) = \text{log}(x) + \text{log}(y)log(*x**y*)=log(*x*)+log(*y*)

![](http://geekresearchlab.net/coursera/neuro/neuro-decision-13.jpg) 
![](http://geekresearchlab.net/coursera/neuro/neuro-decision-14.jpg) 

```
Below diagrams are the observations from the retina cells,
```
![](http://geekresearchlab.net/coursera/neuro/neuro-decision-15.jpg)
![](http://geekresearchlab.net/coursera/neuro/neuro-decision-16.jpg)
```
Now, the distributions look more like this:
```
![](http://geekresearchlab.net/coursera/neuro/neuro-decision-17.jpg)

![](http://geekresearchlab.net/coursera/neuro/neuro-decision-18.jpg) 
```
To learn more on the retina cells, check my guest lecture notes of Dr.Fred Reike:-
https://github.com/ashumeow/Computational-NeuroScience/blob/master/Week-3/notes/notes/guest-lecture.md
```
![](http://geekresearchlab.net/coursera/neuro/neuro-decision-19.jpg)

![](http://geekresearchlab.net/coursera/neuro/neuro-decision-20.jpg)

#### Question:

True or False: Adjusting for the prior probabilities allows a downstream cell (the bipolar cell in this case) to be highly confident that any input it is receiving was the result of a stimulus rather than just noise from the upstream cell.

#### Answer:

Check if true, leave unchecked if false.

#### Explanation:

The prior probability gives us a way of quantifying the distribution of firing rates of the cell in an average case, which we can think of as simply the noisy case (the cell is receiving any random input). By adjusting for that normal firing rate, we can pick out instances when the firing rate is significantly different from what we consider normal.
