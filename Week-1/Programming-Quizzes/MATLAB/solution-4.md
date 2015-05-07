```
Which of the following commands will NOT give an error? Select all the correct answers.
```
```m
>> B=[2,2;3,3;4,4]

B =

     2     2
     3     3
     4     4

>> d=[1,2,3]

d =

     1     2     3

>> f=[8;9]

f =

     8
     9

>> B-[d' d'*2]

ans =

     1     0
     1    -1
     1    -2

>> B+repmat(f',3,1)

ans =

    10    11
    11    12
    12    13

>> B-repmat(f,1,3)
Error using  - 
Matrix dimensions must agree.
 
>> B+[f;f;f]
Error using  + 
Matrix dimensions must agree.
```
