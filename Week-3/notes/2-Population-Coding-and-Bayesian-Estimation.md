## Decoding from many neurons

### methods for decoding from populations

- population vector
- Bayesian inference
- maximum likelihood
- maximum a posteriori

**population vector**: In neuroscience, a population vector is the sum of the preferred directions of a population of neurons, weighted by the respective spike counts.


### population vector

#### Criket cercal system(蟋蟀结节系统)

**cercai**: transduce wind velocity into an electrical singal by the movement of the hairs on cercai.

The i(th) neuron has a preferred direction where the response is maximum that is denoted by the angle S(i) or vector C(i).

```
Question:
Which of these options presents a plausible explanation for the presence of neurons that encode for motion in 4 different directions in a 2-dimensional plane?

1. Having neurons that select for 4 different directions allows the cricket to have a higher density of motion sensitive neurons.
2. Negative firing rates cannot be achieved by a neuron.
3. The cricket collects more information about its environment if the basis vectors are not independent.
4. A sensory neuron can respond to motion in a direction along its primary motion-sensitive axis but not to motion in a direction against it.

Answer:
2. Negative firing rates cannot be achieved by a neuron.
4. A sensory neuron can respond to motion in a direction along its primary motion-sensitive axis but not to motion in a direction against it.

Explanation:
This has to do with negation and how it relates to the physical world. On the real number line, we of course have negative numbers. But in physical terms, we cannot, for instance, have a negative firing rate. Also, sensory neurons are meant to respond to positive stimuli. As a result, we need pairs of vectors that face in opposite directions so that motion in either direction can be encoded.
```

The cosine-like response functions of the cells have been shifted and scaled so that the normalized firing rate is always between 0 and 1.

```
Question:
In this equation, we normalize the contribution of each neuron to the population vector by its maximum firing rate. Why do we do this?

Answer:
Some neurons have an intrinsically higher firing rate and we want each neuron to contribute to the population vector in a way that is proportional to its relative activation.

Explanation:
When combining the effects of several neurons, we want to take into account that the neurons have intrinsic differences independent of the stimulus. 
For instance, if a neuron's maximum firing rate is 10Hz, and we observe an average of 9Hz in the presence of a particular stimulus, we should recognize this as a stronger response than if we had observed a 9Hz average rate for a neuron whose maximum firing rate is 100Hz.
```

The eight different clumps of vectors represent eight different neurons, each of whom has a preferred direction indicated by its position among the other seven neurons.

The population vecator is neither general or optimal(which make use of all information in the stimualus/response distribution)

There are also some limitations experienced in the population coding.

### Bayesian inference

a posteriori distribution = (conditional distribution(also called likelihood function) * prior distribution) / marginal distribution

focus on the posteriori distribution and likelihood function.

### Decoding an aribitray continuous stimulus
assumption:
- assume independence
- assume Possion firing
- assume good coverage: $\sum_{i=1}^{N}f_i(s)$

$f_i(s)$ is a Gaussian distribution of s.

> The Gaussians here are not probability distributions. “Gaussian” just refers to the mathematical form of the tuning curve.

spikes are produced randomly and indepandently in each time bin. 
assume as Poisson distrubition.

```
Question:
What is the standard deviation of a poisson neuron with an average firing rate of r?

Answer:
√r

Explanation:
The variance of a poisson distribution is equal to the mean and the standard deviation is the square root of the variance. 
Therefore, if the mean firing rate is r, the variance is equal to r, and the standard deviation is equal to √r
```

### Maximum likelihood

From Gaussianity of tunning curves,
$$
\begin{aligned}
    s^*=\frac{\sum{r_a s_a}/\sigma_a^2}{\sum r_a/\sigma_a^2}
\end{aligned}
$$

if all $\sigma$ are the same,
$$
\begin{aligned}
    s^*=\frac{\sum{r_a s_a}}{\sum r_a}
\end{aligned}
$$


### maximum posterior distribution

```
Question:
If the likelihood distribution is P(A|B), what is the a posteriori distribution?

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

Maximum $\ln{p[r|s]}$ with respect to s
$$
\begin{aligned}
\ln{p[r|s]} = \ln{P[r|s]} +\ln{p[s]}-\ln{P[r]}
\end{aligned}
$$

#### limitations of these approaches

- tunning curve/mean firing rate
- correlations in the population

```
So, we can use Bayes Law to write the likehood, prime and sum used in the posteriori.
```
![](http://geekresearchlab.net/coursera/neuro/neuro-decision-38.jpg)

