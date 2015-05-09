```
Continuation from previous chapter...
Question:
How are these oriented receptive fields obtained from center-surround receptive fields?
Answer:
(Primary Visual Cortex, V1 model)
Using Mechanistic Models,
Arrange the (center surround) inputs (LGN cells) in 45 degree vertical manner (preferred orientation),
then make a feed-forward connection convering inputs to a particular cell (V1).
-- Proposed in 1960 by Hubel & Wiesel.
-- Controversial model (It does not talk other recurrence inputs, though those input contribute to V1 cell).
-- Two kinds of inputs:- Feed-forward and recurrent networks.
```
![](http://geekresearchlab.net/coursera/neuro/receptive-mech.jpg)
<br>
```
Interpretive Models:
RF1, RF2, RF3 and RF4 --> neurons
```
![](http://geekresearchlab.net/coursera/neuro/receptive-inter.jpg) <br><br>
![](http://geekresearchlab.net/coursera/neuro/receptive-inter-2.jpg)<br>
```
Question:
When we say "linear combination" we are talking about a specific mathematical way of combining several things together. 
Which of the following looks most like an example of a linear combination of receptive fields to form an image reconstruction, 
assuming I is the image, and the RFs are the receptive fields we are combining?
Answer:
I = 3*RF1 + 2*RF2 + 5*RF3
Explanation:
Put simply, a linear combination involves adding multiples of many things together. 
For example, 
if we linearly combine X1, X2, X3, ... together, with multipliers equal to a, b, c, ..., we get: a*X1 + b*X2 + c*X3 + ...
Likewise, 
we can linearly combine receptive fields where the multipliers are the strength of the response of a neuron (with a particular receptive field) to the visual stimulus.
```
```
(contd..) Interpretive models of receptive field:
-- When it comes to reconstruction of images and errors...
Start out with random RF running an efficient coding algorithm over natural image patches.
-- Types of efficient coding algorithms:
(i) Sparse coding [Olshausen & Field, 1996]
(ii) Independent Component Analysis (ICA) [Bell & Sejnowski, 1997]
(iii) Predictive coding
```
![](http://geekresearchlab.net/coursera/neuro/receptive-inter-3.jpg)
```
Question:
With this interpretive model of V1 receptive fields, our purpose is to:
Answers:
(1) Give an explanation why V1 receptive fields are formed the way we observe them to be...
(2) Demonstrate that the perceptual processes in the brain may be formed in a way that allows for a faithful and efficient encoding of the natural environment.
(3)Provide a computational model of one aspect of the brain's organization, which gives us insights that may be difficult to derive from strict empirical measurements alone.
```
