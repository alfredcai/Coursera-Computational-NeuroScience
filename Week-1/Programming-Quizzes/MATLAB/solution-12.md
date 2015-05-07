```m
>> A=[1;2;3]

A =

     1
     2
     3

>> B=[-1,-2,-3]

B =

    -1    -2    -3

>> B=[-1;-2;-3]

B =

    -1
    -2
    -3

>> C=[-1;-4;-9]

C =

    -1
    -4
    -9

>> whos
  Name      Size            Bytes  Class     Attributes

  A         3x1                24  double              
  B         3x1                24  double              
  C         3x1                24  double              

>> C=A.*B

C =

    -1
    -4
    -9

>> C=A*B
Error using  * 
Inner matrix dimensions must agree.
 
>> C=A'*B

C =

   -14
```
