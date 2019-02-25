## 2.4 Neural Encoding: Variability
![](http://geekresearchlab.net/coursera/neuro/v-1.jpg)
```
When have you found a good feature?
(i) When the input/output curve over your variable is interesting.
(ii) Hoe to quantify interesting?
```
![](http://geekresearchlab.net/coursera/neuro/v-2-1.jpg)

### Kullback- Leibler divergence(relative entropy)

the Kullback–Leibler divergence (also called relative entropy) is a measure of how one probability distribution is different from a second, reference probability distribution.


![](http://geekresearchlab.net/coursera/neuro/v-2-2.jpg)
![](http://geekresearchlab.net/coursera/neuro/v-3.jpg)
![](http://geekresearchlab.net/coursera/neuro/v-4.jpg)

#### Question:
In summary, some advantages of maximally-informative dimensions are (check all that apply):
#### Answers:
(i) It gives us a way of seeking filters that maximize the discriminability of the spike-conditioned distribution and the prior.
(ii) It does not require a specific structure for the distributions, such as Gaussians.
(iii) You sound super-smart when you mention it at a party.


![](http://geekresearchlab.net/coursera/neuro/v-5.jpg)
![](http://geekresearchlab.net/coursera/neuro/v-6.jpg)
```
Example 1: Bernoulli trials
```
```
Example 2: Binomial spiking
```
![](http://geekresearchlab.net/coursera/neuro/v-7.jpg)
```
Example 3: Poisson spiking
```
![](http://geekresearchlab.net/coursera/neuro/v-8.jpg)

#### Question:
Suppose that while a stimulus is present, a neuron's mean firing rate is r=4 spikes/second. 
If this neuron's spiking is characterized by Poisson spiking, then the probability that the neuron fires k spikes in T seconds is given by: p(k)=((rT)^k e^−rT)/k!
What is the probability that when this stimulus is shown for one second the neuron does not fire any spikes?
Answer:
e^-4
#### Explanation:
The probability that the neuron fires no spikes in one second is given by p(0), 
where we set T=1 second. 
Thus, rT=4 and 
p(0)=(4)^0 e^−4/0!=e^−4


![](http://geekresearchlab.net/coursera/neuro/v-9.jpg) 
![](http://geekresearchlab.net/coursera/neuro/v-10.jpg)

#### Question:
Poisson models are accurate descriptions of some neurons but poor descriptions of others. 
Which of the following neurons is least likely to be characterized by Poisson spiking?
Answer:
A neuron that fires many hundreds of times per second.
#### Explanation:
Poisson spiking assumes that each spike time is independent of all the others. 
However, in real neurons there exists a refractory period (usually on the order of a millisecond or so) that prevents the cell from spiking immediately after a previous spike has just occurred. 
The more times a cell spikes per second, the larger the role of this effect. 
There can also be more complex effects that render a neuron's spiking non-Poisson.

![](http://geekresearchlab.net/coursera/neuro/v-11.jpg)

#### Question:
Which of the following additions to our spike-generation model would improve its accuracy?
#### Answers:
(i) Taking into account the history of the cell's own firing.
(ii) Taking into account the cell's interaction with other cells.
#### Explanation:
In the real world, the activity of a neuron is often affected by its own spiking history as well as the activity of the neurons that it is connected to. 
We will now examine models that try account for these effects.

![](http://geekresearchlab.net/coursera/neuro/v-12.jpg)
![](http://geekresearchlab.net/coursera/neuro/v-13.jpg)
![](http://geekresearchlab.net/coursera/neuro/v-14.jpg)

```
The sweet lecturer says that i deserve a puppy for watching this week videos... =P
She is right... the theory was too deep and the math problems related to it were challenging..
Next week is on decoding...
```
