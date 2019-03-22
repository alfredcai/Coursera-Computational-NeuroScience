![](http://geekresearchlab.net/coursera/neuro/spi-1.jpg)<br><br>
![](http://geekresearchlab.net/coursera/neuro/spi-2.jpg)<br><br>
![](http://geekresearchlab.net/coursera/neuro/spi-3.jpg)<br><br>
![](http://geekresearchlab.net/coursera/neuro/spi-4.jpg)<br><br>
![](http://geekresearchlab.net/coursera/neuro/spi-5.jpg)<br><br>
![](http://geekresearchlab.net/coursera/neuro/spi-6.jpg)<br><br>
![](http://geekresearchlab.net/coursera/neuro/spi-7.jpg)<br><br>
![](http://geekresearchlab.net/coursera/neuro/spi-8.jpg)<br><br>
![](http://geekresearchlab.net/coursera/neuro/spi-9.jpg)<br><br>
![](http://geekresearchlab.net/coursera/neuro/spi-10.jpg)<br><br>
![](http://geekresearchlab.net/coursera/neuro/spi-11.jpg)<br><br>
![](http://geekresearchlab.net/coursera/neuro/spi-12.jpg)<br><br>
![](http://geekresearchlab.net/coursera/neuro/spi-13.jpg)<br><br>
![](http://geekresearchlab.net/coursera/neuro/spi-14.jpg)<br><br>
![](http://geekresearchlab.net/coursera/neuro/spi-15.jpg)<br><br>
![](http://geekresearchlab.net/coursera/neuro/spi-16.jpg)<br>

# Spikes
## the ion channel is a cool molecular machine
n describes a subunit:
n is open probability
1-n is close probability

channel open probability is n^4

only when four subunit happen to be open together, the ion channel allows a current to flow

## Dynamic of activitation
$\dfrac{dn}{dt} = \alpha(V)(1-n) - \beta(V)n$

we cam rewrite it:
$$
\begin{aligned}
    & \tau_n(V) \dfrac{dn}{dt} &= n_\infty(V) - n \\
where:&\\
    & \tau_n(V)   &= \dfrac{1}{\alpha(V)+\beta(V)}\\
    & n_\infty(V) &= \dfrac{\alpha(V)}{\alpha(V)+\beta(V)}
\end{aligned}
$$

```
The open probability of the potassium channel is the product of open probabilities of its subunits. What is an assumption we make here?

The probability of each subunit being in the open configuration is independent of the other subunits' configuration
The probability of the channel being open is larger when a channel has more subunits and we correspondingly raise n to higher powers
At any given time, we only need to know if a single subunit is open to determine if the channel will be open.
All of the above.

Answer:
The probability of each subunit being in the open configuration is independent of the other subunits' configuration

Explanation:
The probability of both of two independent events happening is the product of the probabilities of each event happening separately. If we assume the 4 subunits open and close independent of one another, then the probability that all of them will be open at the same time is the probability that one of them is open at any given time (n), raised to the 4th power, so that the probability the channel is open (all subunits are in the open configuration) is n*n*n*n. A similar concept would apply if we flipped 4 coins at the same time; the probability of getting 4 heads would be (1/2)^4, since the probability of getting heads on each individual quarter does not depend on whether or not any of the other quarters land on heads.
```
```
Based on the graph on the right, which variable is the fastest to react?

n
h
m
They are all roughly the same.

Answer:
m

Explanation:
The graph shows that mm has the smallest time constant. This means that when voltage (on the x axis) changes, mm is the first to reach its steady state ($m_{\infty}$) for that voltage.
```