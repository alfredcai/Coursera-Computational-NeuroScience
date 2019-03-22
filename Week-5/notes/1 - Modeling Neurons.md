![](http://geekresearchlab.net/coursera/neuro/model-1.jpg)<br><br>
![](http://geekresearchlab.net/coursera/neuro/model-2.jpg)<br><br>
![](http://geekresearchlab.net/coursera/neuro/model-3.jpg)<br><br>
![](http://geekresearchlab.net/coursera/neuro/model-4.jpg)<br><br>
![](http://geekresearchlab.net/coursera/neuro/model-5.jpg)<br><br>
![](http://geekresearchlab.net/coursera/neuro/model-6.jpg)<br><br>
![](http://geekresearchlab.net/coursera/neuro/model-7.jpg)<br><br>
![](http://geekresearchlab.net/coursera/neuro/model-8.jpg)<br><br>
![](http://geekresearchlab.net/coursera/neuro/model-9.jpg)<br><br>
![](http://geekresearchlab.net/coursera/neuro/model-10.jpg)<br><br>
![](http://geekresearchlab.net/coursera/neuro/model-11.jpg)<br><br>
![](http://geekresearchlab.net/coursera/neuro/model-12.jpg)<br><br>
![](http://geekresearchlab.net/coursera/neuro/model-13.jpg)<br><br>
![](http://geekresearchlab.net/coursera/neuro/model-14.jpg)<br>

# Modeling Neurons

## Kirchhoff Circuit Laws

The algebraic sum of currents in a network of conductors meeting at a point is zero.

## model
- lipid bilayer: behave like a capacitor
- give a voltage V across the membrance
- Kirchhoff Law: $I_R$ + $I_C$ + $I_ext$ = 0
- $I_ext$ is what we can observe

$I_R$ = V/R

Q=CV (capacitance * voltage) also Q=It (electric current * time)
$I_C$ = C $\dfrac{dV}{dt}$

so we get $C \dfrac{dV}{dt} = -\dfrac{V}{R} + I_ext$ 

> the differential equation is linear and it's first order in V, dependence on V, is simply linear on V

## the cell's battery: the equilibrium potential
cell outside: higher ion concentration, [Na+] [Cl+] [Ca2+]
cell inside: higher, [K+]


t=0, steady state. V=$V_{\inf}$
=$V_{rest} + I_{ext}R$

## each ion type is independent and has its own battery
E_Na ~ 50mV
E_Ca ~ 150mV
E_K  ~ -80mV
E_Cl ~ -60mV

```
What is V_{\infty}?

$I_{ext}R$

$V_{rest}$

$V_{rest} + I_{ext}R$

$\dfrac{V_{rest}}{R}$

Answer:
$V_{rest} + I_{ext}R$
```

```
Recall from week 1 that many types of ion channels can be opened and closed to allow more or less of a particular ion to flow across the cell membrane. In addition, channels can be "gated," meaning the probability the channel will open depends on some variable (such as those listed in the previous slide). So when we say, for instance, that an ion channel type is voltage-dependent or voltage-gated, we mean:

When these channels open, the membrane voltage changes.
These channels exist in electrical synapses, not chemical synapses.
These channels are more likely to be open when membrane voltage reaches a certain range
All of these

Answer:
These channels are more likely to be open when membrane voltage reaches a certain range

Explanation:
Voltage-gated channels sense the voltage across the cell membrane and are more likely to be open if the voltage gets high enough or low enough (depending on the particular channel type).

```
```
Let's review our circuit diagram from earlier in the lecture. The resistor, capacitor, and battery are roughly analogous to the ______, ______, and ______, respectively.
ion gradient, lipid bilayer, ion channels
ion channels, lipid bilayer, ion gradient
lipid bilayer, ion channels, ion gradient
lipid bilayer, ion gradient, ion channels

Answer:
ion channels, lipid bilayer, ion gradient

```