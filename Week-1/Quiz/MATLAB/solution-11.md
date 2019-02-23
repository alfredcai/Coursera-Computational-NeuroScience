```
Which of the following expressions could be used "to set all of the negative entries in A to zero"?
(read this question carefully)
```
```m
>> A=[5,-2,3;2,-3,4;3,4,-8]

A =

     5    -2     3
     2    -3     4
     3     4    -8

>> A<0=0
 A<0=0
    |
Error: The expression to the left of the equals sign is not a valid target for an assignment.
 
>> (A<0)=0
 (A<0)=0
      |
Error: The expression to the left of the equals sign is not a valid target for an assignment.
 
>> A(A<0)=0

A =

     5     0     3
     2     0     4
     3     4     0

>> A(:)=0

A =

     0     0     0
     0     0     0
     0     0     0
```
