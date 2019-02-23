```
Which of the following commands will NOT give an error? Select all the correct answers.
```
```m
>> A=[1,2;3,4]

A =

     1     2
     3     4

>> B=[2,2;3,3;4,4]

B =

     2     2
     3     3
     4     4

>> C=eye(3)

C =

     1     0     0
     0     1     0
     0     0     1

>> D=[1,2,3]

D =

     1     2     3

>> E=zeros(3,3)

E =

     0     0     0
     0     0     0
     0     0     0

>> A*B'

ans =

     6     9    12
    14    21    28

>> C.*E

ans =

     0     0     0
     0     0     0
     0     0     0

>> D*B

ans =

    20    20

>> C*E

ans =

     0     0     0
     0     0     0
     0     0     0

>> A-B
Error using  - 
Matrix dimensions must agree.
 
>> A*B
Error using  * 
Inner matrix dimensions must agree.
```
