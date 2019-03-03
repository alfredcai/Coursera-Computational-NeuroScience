## 1. Likelihood ratio test with asymmetric costs
Suppose we have a stimulus defined by a single variable called s. s can take one of two values, which we will call $s_1$ and $s_2$. You could think of these as lights flashing in the eyes at one of two possible frequencies. Or perhaps listening to punk rock vs. listening to Dvorak.

Let's call the firing rate response of a neuron to this stimulus r.

Suppose that under stimulus $s_1$ the response rate of the neuron can be roughly approximated with a Gaussian distribution with the following parameters:

$\mu$ (mean): 5

$\sigma$ (standard deviation): 0.5

And likewise for $s_2$:

$\mu$: 7

$\sigma$: 1

Lets say that both stimuli are equally likely and we are given no other prior information.

Now let's throw in another twist. Let's say that we receive a measurement of the neuron's response and want to guess which stimulus was presented, but that to us, it is twice as bad to mistakenly think it is $s_2$ than to mistakenly think it is $s_1$.

Which of these firing rates would make the best decision threshold for us in determining the value of s given a neuron's firing rate?

Hint: There are several functions available to help you evaluate Gaussian distributions. In Octave and in Matlab's stats toolbox you can use the 'normpdf' function. If you know how to set the problem up, you will be able to try all the answers below to find the one that works best. If you decide to challenge yourself to solve this algebraically instead, you can use the univariate Gaussian PDF, given at the top of this [Wikipedia page](https://en.wikipedia.org/wiki/Normal_distribution).

(i) 2.69
(ii) 5.830
(iii) 5.978
(iv) 5.667

Answer:
(iii) 5.978

y_1=normdf(x_1,5,0.5)
y_2=normdf(x_2,7,1)
let 2*y_1=y_2, get x= 2.6896 or 5.9771
since we need the value in the middle of two normal distrubution, so we choose the 5.978

```matlab
% matlab code 
syms x
S = solve(2*normpdf(x,5,0.5)==normpdf(x,7,1),x)
```

## 2. Using the maximum likelihood (ML) criterion, would we diagnose them positive
Suppose we are diagnosing a very rare illness, which happens only once in 100 million people on average. Luckily, we have a test for this illness but it is not perfectly accurate. If somebody has the disease, it will report positive 99% of the time. If somebody does not have the disease, it will report positive 2% of the time.

Suppose a patient walks in and tests positive for the disease. Using the maximum likelihood (ML) criterion, would we diagnose them positive?

(i) yes
(ii) no

Answer:
P(B):prior, rare
P(A):evidence, 
P(A|B):likelihood
P(B|A):posterior

P(B|A)=99%
P(B|~A)=2%

P(A|B)=p(B|A)*p(A)/p(B)

yes

## 3. What if we used the maximum a posteriori (MAP) criterion?
Continued from Question 2:
What if we used the maximum a posteriori (MAP) criterion?

(i) yes
(ii) no

Answer:
no

## 4. Why do we see a difference between the two criteria, if there is one?
(i) Unlike MAP, ML assumes the same model for all people.
(ii) Since ML assumes a Gaussian distribution, unlike MAP, it oversimplifies the world.
(iii) The role of prior probability is different between the two.
(iv) There is no difference between the two, because in this case they are equivalent.

Answer:
iii
