```
What does the keyboard command do when placed inside a MATLAB script 
```
```
(for example:
```
```matlab
x = 5;
y = [3 5 7];
z = x * y;
keyboard;
w = z .^ 2;
```
<b>Solution:</b>
```m
>> x=5;
>> y=[3 5 7];
>> z=x*y;
>> keyboard;
K>> w=z.^2;
K>> dbquit

Stops execution of program and gives control to the keyboard.
```
