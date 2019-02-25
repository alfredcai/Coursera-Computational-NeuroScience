## 1. What is the definition of a spike triggered average for a neuron?


(i) The set of stimuli preceding a spike, each averaged over time.
(ii) The stimuli preceding a spike, averaged over all stimuli that elicited a spike.
(iii) None of these.
(iv) The average time between spikes in a recording.
(v) The set of all stimuli that elicit a spike.

```
The STA is computed as an average over the spike-triggered ensemble. 

For example, if each stimulus in the spike-triggered ensemble is a 100 ms time-series, 
then the STA will also be a 100 ms time-series.

so, (ii) The stimuli preceding a spike, averaged over all stimuli that elicited a spike.
```

## 2. What is the nature of this neuron? That is, what mathematical operation of the stimulus does it compute?

(i) Differentiation.
(ii) Running average/sum.
(iii) No response.
(iv) Leaky integration.

```
(iv) leaky integration
```
## 3. Which of the following stimuli would you expect this neuron to respond most strongly to? You may assume that all non-zero values of the stimulus have the same magnitude. That is, assume that all positive stimuli have a value of c and all negative stimuli have a value of −c where c>0.

(i) No difference.
(ii) A constant positive value.
(iii) A positive value followed by a negative value.
(iv) A constant negative value.
(v) A negative value followed by a positive value.

```
(ii) A constant positive value.
```

## 4. Suppose we had reason to suspect that this neuron responded to two modes (features) of the stimulus. Which of the following methods is most likely to help us determine those two modes?

(i) Principal component analysis/covariance analysis
(ii) Dividing the spikes into two disjoint sets and computing the spike-triggered average for each of those sets independently.
(iii) Computing the spike-triggered average to get the first mode and then subtracting it from the stimulus in each time window before a spike and then computing the spike-triggered average for the resulting signal to get the second mode.
(iv) Computing the spike-triggered average normally.

```
not (iii)
```

## 5.Which of the following is not an example of a linear filtering system? 
Let x(t) denote the input signal and y(t) denote the output signal.

(i) y(t)=3x(t)−5x(t−τ), where τ is positive.			
(ii) y(t)=cos[x(t−θ)]
(iii) y(t)=∫∞0e−τx(t−τ)dτ			
(iv) y(t)=∑∞n=0anx(t−nτ), where a is between 0 and 1, and τ is positive.

```
(ii) y(t)=cos[x(t-\theta)]
```