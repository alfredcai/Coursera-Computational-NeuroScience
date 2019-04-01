# Networks that Learn

## 1.
(Question Variation 3: Numbers different in different variations) Suppose we have a linear feedforward network with two input nodes and one output node. Let's say that we are learning our weight vector w and that we are using the Hebb rule.

Suppose the input correlation matrix Q is:
Q=[[0.2,0.1],[0.1,0.3]]

If we allow learning to go on for a long period of time, which of these could be a final weight vector w?

(Hint: See lecture 7.1 and use Matlab's "eig" command)

w=[0.8944;1.7889]

w=[−1.5155;−1.3051]

w=[−1.5764;−1.2308]

w=[1.0515;1.7013]

Answer:
w=[1.0515;1.7013],x
w=[−1.5155;−1.3051],x
w=[−1.5764;−1.2308],x

## 2.
What does the weight vector we found in Question 1 tell us?

None of these options

That the mean of the input distributions is (0,0)

That the time constant tau, start subscript, w, end subscript $\tau_{w}$ was 2

That this Hebbian learning system is engaged in long-term depression of the outputs

Answer:
None of these options

## 3.
The "learning rate" as mentioned in lecture 7.2 is used in many different contexts to denote the sensitivity of a parameter estimate to new data during online learning. Check all of the following which are true:

[ ] A higher learning rate makes the parameter estimate more influenced by noise during online estimation.
[ ] A constant learning rate allows the parameter estimate to remain sensitive to new data.
[ ] A higher learning rate makes the parameter estimate less influenced by noise during online estimation.
[ ] The learning rate does not affect the parameter estimate's sensitivity to noise.

Answer:
A higher learning rate makes the parameter estimate more influenced by noise during online estimation.
A constant learning rate allows the parameter estimate to remain sensitive to new data.

## 4.
In the lectures, we saw multiple algorithms which use a two-step process for parameter estimation. EM is one such algorithm, consisting of the E and M steps. In each step, we iteratively update our estimates of parameters. Why do we need to alternate between the two steps? What justifies this approach?

(Hint: You may want to search "EM algorithm" on the web)

We need the alternating steps because the two sets of parameters are mutually dependent on each other, necessitating that they be optimized together. This is justified by the fact that these algorithms will always attempt to move towards a better solution with each iteration.

We don't actually need the alternating steps - we could get away with optimizing one set of values at a time, and doing it only once; we alternate because it is simple to program the alternation as a loop. This is justified by the fact that these algorithms will always arrive at the globally optimal solution.

We need the alternating steps because the two sets of parameters are mutually dependent on each other, necessitating that they be optimized together. This is justified by the fact that these algorithms will always arrive at the globally optimal solution.

We don't actually need the alternating steps - we could get away with optimizing one set of values at a time, and doing it only once; we alternate because it is simple to program the alternation as a loop. This is justified by the fact that these algorithms will always attempt to move towards a better solution with each iteration.

Answer:
We need the alternating steps because the two sets of parameters are mutually dependent on each other, necessitating that they be optimized together. This is justified by the fact that these algorithms will always attempt to move towards a better solution with each iteration.

## 5.
In the next five questions, we'll implement Oja's Hebb rule for a single neuron and explore some of its properties.

Recall that Oja's rule is:

$$
\begin{aligned}
    \tau_{w} \dfrac{d \textbf{w}}{dt} = v \textbf{u} - \alpha v^{2} \textbf{w},\\
    where  v=u⋅w.
\end{aligned}
$$

We will implement the discrete time version of Oja's rule in Matlab or Octave. To do this, first rewrite Oja's rule using discrete time rather than continuous time. Which of the following equations represents the discrete time version of Oja's rule? (Let η=1/τw).


Δw=Δtη(vu−αv2w)
Δw=Δt(vu−αv2w)
dw/dt=η(vu−αv2w)
Δw=η(vu−αv2w)

Answer:
dw/dt=η(vu−αv2w),x
Δw=η(vu−αv2w),x

## 6.
Now, in order to use Oja's rule, we need to translate the discrete time version into an update rule. Which of the following equations represents the discrete update equation for Oja's rule?


wi+1=wi+Δtη(vu−αv2w)
wi+1=wi+Δt(vu−αv2w)
wi+1=wi+η(vu−αv2w)
wi+1=wi+vu−αv2w

Answer:
wi+1=wi+η(vu−αv2w),x
wi+1=wi+Δtη(vu−αv2w)

## 7.
Continued from Question 5.

In this question, we will use the update rule we just derived to implement a neuron that will learn from two dimensional data that is given in the following Matlab file:
> c10p1.mat or c10p1.pickle

(This file is provided as part of the [exercises](http://www.gatsby.ucl.ac.uk/~dayan/book/exercises.html) from the Dayan and Abbott textbook recommended for the course).

c10p1.mat contains 100 (x, y) data points.

Assume our neuron receives as input the two dimensional data provided in c10p1.mat, but with the mean of the data subtracted from each data point (the mean of all x values should be subtracted from every x value and the mean of all y values should be subtracted from every y value). You should perform this zero-mean centering step and then display the points again to verify that the data cloud is now centered around (0, 0).

Implement the update rule derived in the previous question in Matlab or Octave. Let η=1, α=1, and  Δt=0.01. Start with a random vector as w0. In each update iteration, feed in a data point u=(x,y) from c10p1. If you've reached the last data point in c10p1, go back to the first one and repeat.

Typically, you would keep updating w until the change in w, given by norm(w(t+1) - w(t)), is negligibile (i.e., below an arbitrary small positive threshold), indicating that w has converged. However, since you are implementing this as an online learning algorithm, you may prematurely detect convergence using this method. Instead, you may just run the algorithm for 100,000 iterations.

Run your code multiple times. Which of the following describes the behavior of w and why does this happen?

Hint: Consider the eigenvectors of the correlation matrix of the mean-centered data. (The correlation matrix of a data matrix X, where rows indicate separate samples, is X.T*X/N, where N is the number of samples. You can calculate its eigenvalues using eig().) If the data is mean-centered, the correlation matrix will be the same as the covariance matrix.

Answer:
The correlation matrix has only one principal eigenvector, but there are 
two vectors of length 1/√α that are parallel to this eigenvector. 
w can converge to either of these two vectors.

## 8.
Continued from Question 5.

What happens when the data is not zero-mean centered before the learning process?

In order to more fully explore the behavior of the Oja's rule when the data isn't mean centered, you should adjust the mean of the data a few times and observe the behavior of the learning rule. You can adjust the mean of the data by adding a constant to every x component of the data and a different constant to every y component of the data.

The two vectors that w converges to in different runs of the algorithm are parallel to the vector that points roughly towards the mean of the data.

The two vectors that w converges to in different runs of the algorithm have the same direction as those found when the data is mean centered.

The two vectors that w converges to in different runs of the algorithm are exactly the same as those found when the data is mean centered.

w now converges to the same vector every time the code is run.

Answer:
The two vectors that w converges to in different runs of the algorithm are parallel to the vector that points roughly towards the mean of the data.

## 9.
Continued from Question 5.

What happens when the pure Hebb rule is used instead of Oja's rule? You can explore what happens by removing the subtractive term $- \alpha v^{2} \textbf{w}$ in your code and running the code.

The vectors found by the learning rule have the same direction as those found by Oja's rule, but the length grows without bound as a function of the number of iterations.

The vectors found by the learning rule are identical to those found by the original learning rule.

The vectors found by the learning rule are completely different from those found by the original learning rule: both the direction and length are different.

w converges to the same vector every time the algorithm is run instead of converging to two different vectors whenever the algorithm is run.

Answer:
The vectors found by the learning rule have the same direction as those found by Oja's rule, but the length grows without bound as a function of the number of iterations.
