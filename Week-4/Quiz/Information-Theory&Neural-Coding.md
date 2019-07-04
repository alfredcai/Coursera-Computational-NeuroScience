# Information Theory & Neural Coding

## 1. entropy H(F) of this distribution

Suppose that we have a neuron which, in a given time period, will fire with probability 0.1, yielding a Bernoulli distribution for the neuron's firing (denoted by the random variable F = 0 or 1) with P(F = 1) = 0.1.

Which of these is closest to the entropy H(F) of this distribution (calculated in bits, i.e., using the base 2 logarithm)?

(i) 0.4690
(ii) -0.1954
(iii) 1.999
(iv) 0.1954

Answer:
(i) 0.4690

H(f)=-$\sum_i{p_i \log{p_i}}$
h(f)=-0.1*$\log_2(0.1)$-0.9*$log_2(0.9)$=0.4689955935892812

```python3
from math import log2
-0.1*log2(0.1)-0.9*log2(0.9)
```

## 2. the mutual information $MI(S,F)$

Continued from Question 1:

Now lets add a stimulus to the picture. Suppose that we think this neuron's activity is related to a light flashing in the eye. Let us say that the light is flashing in a given time period with probability 0.10. Call this stimulus random variable $S$.

If there is a flash, the neuron will fire with probability 1/2. If there is not a flash, the neuron will fire with probability 1/18. Call this random variable $F​$ (whether the neuron fires or not).

Which of these is closest, in bits (log base 2 units), to the mutual information $MI(S,F)$?

(i) 0.0904
(ii) 0.8476
(iii) 0.3786
(iv) -0.3786

Answer:
(i) 0.0904

MI(S,F)=total entropy - average noise entropy
total entropy: H(R)=
noise entropy: H(R|+)=-0.5*log2(0.5)-0.5*log2(0.5)=1.0


MI(S,F)=H[F]-$\sum_S{P(S)H(F|S)}$
H[F]=-0.1*$\log_2(0.1)$-0.9*$log_2(0.9)$=0.4689955935892812
$\sum_S{P(S)H(F|S)}$=0.1*0.5+0.9/18=0.1

MI(S,F)=0.36899559358928125

## 3. What do the $\phi_i s$, called the "basis functions," represent in our metaphor?

$$
\begin{aligned}
    I(x) &=\sum_i{a_i \phi_i(x)} + \epsilon(x) \\
    E &=\sum_x{[I(x)-\sum_i{a_i \phi_i(x)}]^2}+\lambda\sum_i{C(a_i)}
\end{aligned}
$$


This math from lecture 4.3 could potentially be intimidating, but in fact the concept is really simple. Getting an intuition for it will help with many types of problems. Let's work out a metaphor to understand it.

Suppose we want to build a complex image. We could do that by layering a whole bunch of pieces together (mathematically - summing). This is like drawing on transparencies with various levels of opacity and putting them on top of each other. Those familiar with Photoshop or Gimp will recognize that concept. If we had to build an image in Photoshop with a bicycle on a road, for instance, perhaps we could have an image of a sky, and one of the road, and one of the bike. We could "add" these pieces together to make our target image.

Of course, if our neural system was trying to make visual fields that worked for any sort of input, we would want more than just roads, skies, and bikes to work with! One possibility is to have a bunch of generic shapes of various sizes, orientations, and locations within the image. If we chose the right variety, we could blend/sum these primitive pieces together to make just about any image! One way to blend them is to let them have varying transparencies/opacities, and to set them on top of each other. That is what we would call a weighted sum, where the weights are how transparent each piece is.

Of course, we may not want to have too many possible shapes to use. As mentioned in the video, the organism likely wants to conserve energy. That means having as few neurons firing as possible at once. If we conceptually make a correlation between these shapes and the neurons, then we can point out we would want to use as few shapes as we could while maintaining an accurate image.

This math gives us a way of summing a bunch of pieces together to represent an image, to attempt to make that representation look as much like the image as possible, and to make that representation efficient - using as few pieces as possible. That is a lot of work for two lines of math!

Now let's put this metaphor into action to understand what all these symbols mean. I'll give you one to start with. The vector x in the equation above represents the coordinates of a point in the image. Now you fill in the rest:

What do the $\phi_i s$, called the "basis functions," represent in our metaphor?

(i) The level of transparency vs. opacity/influence of each piece.
(ii) The importance of coding efficiency.
(iii) The pieces that make up the image.
(iv) The difference between the actual image and the representation.

Answer:
The pieces that make up the image.

## 4. What does $\epsilon$ represent?

Continued from Question 3:

What does $\epsilon$ represent?

(i) The difference between the actual image and the representation.
(ii) The importance of coding efficiency.
(iii) The level of transparency vs. opacity/influence of each piece.
(iv) The pieces that make up the image.

Answer:
The difference between the actual image and the representation.

## 5. What do the $a_i$ 's represent?

Continued from Question 7:

What do the $a_i$ 's represent?

(i) The importance of coding efficiency.
(ii) The difference between the actual image and the representation.
(iii) The pieces that make up the image.
(iv) The level of transparency vs. opacity/influence of each piece

Answer:
The level of transparency vs. opacity/influence of each piece

## 6. What does $\lambda$ represent?

Continued from Question 3:

What does $\lambda$ represent?

(i) The pieces that make up the image.
(ii) The difference between the actual image and the representation.
(iii) The level of transparency vs. opacity/influence of each piece.
(iv) The importance of coding efficiency.

Answer:
The importance of coding efficiency.

## 7. best describes the tuning curve

In the following three questions, we will explore Poisson neuron models and population coding.

This exercise is based on a set of artificial "experiments" that we've run on four simulated neurons that emulate the behavior found in the cercal organs of a cricket. Please note that all the supplied data is synthetic. Any resemblance to a real cricket is purely coincidental.

In the first set of experiments, we probed each neuron with a range of air velocity stimuli of uniform intensity and differing direction. We recorded the firing rate of each of the neurons in response to each of the stimulus values. Each of these recordings lasted 10 seconds and we repeated this process 100 times for each neuron-stimulus combination.

We've supplied you with a .mat file for each of the neurons that contains the recorded firing rates (in Hz). These are named neuron1, neuron2, neuron3, and neuron4. The stimulus, that is, the direction of the air velocity, is in the vector named stimstim.

The matrices contain the results of running a set of experiments in which we probed the synthetic neuron with the stimuli in stim. Each column of a neuron matrix contains the firing rate of that neuron (in Hz) in response to the corresponding stimulus value in stimstim. That is, nth column of neuron1 contains the 100 trials in which we applied the stimulus of value stim(n) to neuron1.

Plot the tuning curve-- the mean firing rate of the neuron as a function of the stimulus-- for each of the neurons.

Which of the following functions best describes the tuning curve?

(i) Gaussian.
(ii) Unrectified cosine.
(iii) Half-wave rectified cosine.
(iv) Linear function.

Answer：
Half-wave rectified cosine.

## 8. Which of the neurons (if any) is NOT Poisson?

Continued from Question 7:

We have reason to suspect that one of the neurons is not like the others. Three of the neurons are Poisson neurons (they are accurately modeling using a Poisson process), but we believe that the remaining one might not be.

Which of the neurons (if any) is NOT Poisson?

Hint: Think carefully about what it means for a neuron to be Poisson. You may find it useful to review the last lecture of week 2. Note that we give you the firing rate of each of the neurons, not the spike count. You may find it useful to convert the firing rates to spike counts in order to test for "Poisson-ness", however this is not necessary.

In order to realize why this might be helpful, consider the fact that, for a constant aa and a random variable $X$, $\mathbb{E}[aX] = a\mathbb{E}[X]$ but $Var(aX)=a^2 Var(X)$. What might this imply about the Poisson statistics (like the Fano factor) when we convert the spike counts (the raw output of the Poisson spike generator) into a firing rate (what we gave you)?

(i) None.
(ii) Neuron 1.
(iii) Neuron 2.
(iv) Neuron 3.
(v) Neuron 4.

Ansewer:
Neuron 3.

## 9. What is the direction, in degrees, of the population vector?

Continued from Question 7:

Finally, we ran an additional set of experiments in which we exposed each of the neurons to a single stimulus of unknown direction for 10 trials of 10 seconds each. We have placed the results of this experiment in the following file:

pop_coding contains four vectors named $r1$, $r2$, $r3$, and $r4$ that contain the responses (firing rate in Hz) of the four neurons to this mystery stimulus. It also contains four vectors named $c1$, $c2$, $c3$, and $c4$. These are the basis vectors corresponding to neuron 1, neuron 2, neuron 3, and neuron 4.

Decode the neural responses and recover the mystery stimulus vector by computing the population vector for these neurons. You should use the maximum average firing rate (over any of the stimulus values in 'tuning.mat') for a neuron as the value of $r_{max}$ for that neuron. That is, $r_{max}$ should be the maximum value in the tuning curve for that neuron.

What is the direction, in degrees, of the population vector? You should round your answer to the nearest degree. Your answer should contain the value only (no units!) and should be between $0^{\circ}$ and $360^{\circ}$. If your calculations give a negative number or a number greater than or equal to 360, convert it to a number in the proper range (you may use the mod function to do this).

You may need to convert your resulting vector from Cartesian coordinates to polar coordinates to find the angle. You may use the atan() function in MATLAB to do this. Note that the the convention we're using defines $0^{\circ}$ to point in the direction of the positive y-axis and $90^{\circ}$ to point in the direction of the positive x-axis (i.e., 0 degrees is north, 90 degrees is east).

Answer:
112