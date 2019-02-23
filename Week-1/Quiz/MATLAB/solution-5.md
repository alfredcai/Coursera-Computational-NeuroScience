```
Suppose we wish to generate a 4x1 vector that contains the number 5 in every position. 
Which of the following expressions will accomplish this task? Select all the correct answers.
```
```m
>> a=[5;5;5;5]

a =

     5
     5
     5
     5

>> a=fives(4,1)
Undefined function or variable 'fives'.
 
>> a=ones(4,1)

a =

     1
     1
     1
     1

>> a=ones(4)*5

a =

     5     5     5     5
     5     5     5     5
     5     5     5     5
     5     5     5     5

>> a=eye(4)*5

a =

     5     0     0     0
     0     5     0     0
     0     0     5     0
     0     0     0     5

>> a=ones(4,1)*5

a =

     5
     5
     5
     5
```
