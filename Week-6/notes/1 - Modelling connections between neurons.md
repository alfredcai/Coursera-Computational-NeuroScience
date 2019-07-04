![](http://geekresearchlab.net/coursera/neuro/net-1.jpg)
```
How do neurons connect to form networks?

Neurons use synapses
```
```
What do these chemical "synapses" do?

-- Increase or Decrease postsynaptic membrane potential.
```
```
In an excitatory synapse,
(Steps)
[1] Input spike
[2] Neurotransmitter release (Eg.Glutamate)
[3] Binds to receptors
[4] Ion channels open
[5] Positive ions (Eg.Na+) enter cell
[6] Depolarization (increase local membrane potential)
```
```
In an inhibitory synapse,
(Steps)
[1] Input spike
[2] Neurotransmitter release (Eg.GABA)
[3] Binds to receptors
[4] Ion channels open
[5] Positive ions (Eg.K+) leave the cell
[6] Hyperpolarization (dencrease local membrane potential)
```
```
What we want to do is...
a computational model of the effects of a synapse on the membrane potential V.

So.. how do we do this?
```
![](http://geekresearchlab.net/coursera/neuro/net-2.jpg)<br><br>
![](http://geekresearchlab.net/coursera/neuro/net-3.jpg)
```
Question:
What is the effect of τm, the "membrane time constant", on how fast the cell's voltage changes in response to an input?

Answer:
As τm increases, it takes longer for the cell to reach steady state when an input is turned on, and longer to decrease to equilibrium when it is turned off.

Explanation:
If you divide both sides of the membrane potential equation by τm, 
you can see that if the time constant increases, 
the terms on the right hand side governing the rate of change of voltage decrease.
```
```
One more question before we proceed...

Going back to the mathematical definition of τm, what then can we say is the relationship between the cell's surface area and how fast the cell reacts to an input?

Answer:
The cell's surface area does not affect how fast it reacts.

Explanation:
τm=Rm*Cm=rm/A∗cmA=rm*cm
So the surface area does not affect the time constant (which determines how fast the cell reacts)!

```
```
What is the value of P_s at equilibrium? That is, what is the value of P_s such that dP_s/dt is 0?

\frac{dP_s}{dt} = \alpha_s(1-P_s) - \beta_sP_s
dt
dP 
s
​	 
​	 =α 
s
​	 (1−P 
s
​	 )−β 
s
​	 P 
s

Answer:
α 
s
​	 /(α 
s
​	 +β 
s
​	 )

Explanation:
To solve this, we set \frac{dP_s}{dt} = 0 
dt
dP 
s
​	 
​	 =0. This yields 0 = \alpha_s(1-P_s) - \beta_sP_s0=α 
s
​	 (1−P 
s
​	 )−β 
s
​	 P 
s
​	 . Thus, 0 = \alpha_s - P_s(\alpha_s + \beta_s)0=α 
s
​	 −P 
s
​	 (α 
s
​	 +β 
s
​	 ), so P_s = \alpha_s/(\alpha_s + \beta_s)P 
s
​	 =α 
s
​	 /(α 
s
​	 +β 
s
​	 ).
​	
```
```
How do we model the effects of a synapse on the membrane potential V?
```
![](http://geekresearchlab.net/coursera/neuro/net-4.jpg)<br><br>
![](http://geekresearchlab.net/coursera/neuro/net-5.jpg)<br><br>
![](http://geekresearchlab.net/coursera/neuro/net-6.jpg)
```
Question:
What is the value of Ps at equilibrium? 
That is, what is the value of Ps such that dPs/dt is 0? 
Answer:
```
![](http://geekresearchlab.net/coursera/neuro/net-7.jpg)<br><br>
![](http://geekresearchlab.net/coursera/neuro/net-8.jpg)
```
How do we model the effects of multiple spikes in synaptic conductance?
```
![](http://geekresearchlab.net/coursera/neuro/net-9.jpg)<br><br>
![](http://geekresearchlab.net/coursera/neuro/net-10.jpg)<br>
