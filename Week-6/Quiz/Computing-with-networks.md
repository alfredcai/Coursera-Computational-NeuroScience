#Computing with Networks

## 1.
Let's design some feedforward networks that can do some basic operations on their inputs. This could mean lowering their intensity, looking for strong changes, or one of many other possibilities. One nice way to build intuition for this sort of processing is to think of these networks as operating on images. Even though our networks will operate over only 5 pixels of image data, we can still build the same basic operations that we would for a regular image.

For the next four questions, we will start with the following image as input:

![](pic/q5_pave.jpg)

Suppose we processed the image and it looked like this:

![](pic/q5_paveBlurred.jpg)

Which of the following weight matrices W would give us a feedforward network most closely approximating this image processing operation?
​	
Answers:
0.33

## 2.
Suppose we processed the image and it looked like this:

![](pic/q5_paveDarkened.jpg)

Which of the following weight matrices W would give us a feedforward network most closely approximating this image processing operation?

Answers:
0.5

## 3.
Suppose we processed the image and it looked like this:

![](pic/q5_paveEdges.jpg)

Which of the following weight matrices W would give us a feedforward network most closely approximating this image processing operation?

Answers:
0.75

## 4.
Suppose we processed the image and it looked like this:

![](pic/q5_pavePixelized.jpg)

Which of the following weight matrices WW would give us a feedforward network most closely approximating this image processing operation?

Answers:
1

## 5.
In lecture 6.2, we encountered a process of conceptual abstraction, taking us from modeling individual neurons to modeling whole networks. By the middle of the lecture, we had abstracted away many of the interesting time dynamics of feedforward neural networks and arrived at a simple equation:

${\bf v_{ss}} = F(W{\bf u})$

We have to make a number of assumptions to get to this equation. Necessarily we lose some interesting information when we make these assumptions from the beginning of lecture 6.2 to the point where we first see this equation (roughly 10 min in). Which of the following holds true? (Check all that are true)

[] This model does not allow differences in firing rates between different inputs.
[] This model shows us the outputs the system will converge to, but no longer describes the time dynamics of that convergence.
[] This model ignores the effects of synchrony and correlation between the input neurons.
[] This model ignores the firing rates of the output cells.
[] This model ignores patterns in the input and output spike timings, opting instead to simply look at firing rates.
[] This model cannot adequately represent many of the dynamics of individual cells, such as the effect of the refractory period.
[] This model assumes static, unchanging inputs, so it does not account for the dynamics resulting from constantly changing inputs.
[] This model ignores the firing rates of the input cells.
[] This model does not allow for synaptic connections where an input cell is inhibiting the firing of the output cell.
[] Since this model does not use a detailed description of individual cells, it does not account for the strength of individual synaptic connections.

Answers:

This model ignores the effects of synchrony and correlation between the input neurons.
This model cannot adequately represent many of the dynamics of individual cells, such as the effect of the refractory period.2.1/3


## 6.
The next three questions utilize the following code to model an integrate-and-fire neuron receiving input spikes through an alpha synapse:

> aplha_neuron.py or aplha_neuron.m

The parameter “$t_{peak}$” controls when the alpha function peaks after an input spike occurs (and hence how long the effects of an input spike linger on in the postsynaptic neuron). “$t_{peak}$” for excitatory synapses in the brain may vary from 0.5 ms (AMPA or non-NMDA) to 40 ms (NMDA synapse).

Vary the value of $t_{peak}$ from 0.5 ms to 10 ms in steps of 0.5 ms and observe how this influences the output of the neuron for the fixed input spike train used in this code.

Plot the output spike count as a function of $t_{peak}$ for the given input spike train.

Which of the following answers best describes the relationship between the value of $t_{peak}$ and the firing rate of the neuron?

The neuron's firing rate increases sublinearly as a function of the value of $t_{peak}$.
The neuron's firing rate increases linearly as a function of the value of $t_{peak}$.
The neuron's firing rate increases superlinearly as a function of the value of $t_{peak}$.
The neuron's firing rate decreases sublinearly as a function of the value of $t_{peak}$.
The neuron's firing rate decreases linearly as a function of the value of $t_{peak}$.
The neuron's firing rate decreases superlinearly as a function of the value of $t_{peak}$.

Answers:
The neuron's firing rate increases sublinearly as a function of the value of $t_{peak}$.

## 7.
Continued from Question 6:

Which of the following explanations best explains how the value of $t_{peak}$ influences the firing rate of the neuron?

Increasing the value of $t_{peak}$ decreases the decay rate of the synaptic conductance, allowing more charge to flow per spike and increasing the extent of the summation between input spikes.
Increasing the value of $t_{peak}$ increases the decay rate of the synaptic conductance, allowing less charge to flow per spike and decreasing the extent of the summation between input spikes.
Increasing the value of $t_{peak}$ decreases the decay rate of the neuron's voltage, increasing the extent of the summation between the neuron's voltage response to spikes.
Increasing the value of $t_{peak}$ increases the decay rate of the neuron's voltage, decreasing the extent of the summation between the neuron's voltage response to spikes.

Answers:
Increasing the value of $t_{peak}$ decreases the decay rate of the synaptic conductance, allowing more charge to flow per spike and increasing the extent of the summation between input spikes.

## 8.
Continued from Question 6:

How would you turn this synapse into an inhibitory synapse? (Check all that apply)


[] Changing the value of $E_{syn}$ to be less than that of $V_{th}$.
[] Changing the value of $E_{syn}$ to be greater than 0.
[] Changing the value of $E_{syn}$ to be less than 0.
[] Changing the value of $E_{syn}$ to be less than that of $E_{leak}$.

Answers:
Changing the value of $E_{syn}$ to be less than that of $V_{th}$.
Changing the value of $E_{syn}$ to be less than that of $E_{leak}$.

## 9.
(Question variation 2: Different variations have different numbers) Suppose that we had a linear recurrent network of 5 input nodes and 5 output nodes. Let us say that our network's weight matrix W is:


Suppose that we have a static input vector ${\bf u}$:

Which of the following is the steady state output ${\bf v_{ss}}$ of the network?

(Hint: See the lecture on recurrent networks, and consider writing some Matlab/Octave/Python code to handle the eigenvectors/values (you may use the "eig" function in Matlab/Octave or "np.linalg.eig" in Python))


Answers:
[0.57468284 0.46104003 0.5556308  0.35789389 0.33646672]
