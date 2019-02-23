```
Suppose x=[1 1 2 2 1 3 2 2 3 1]. Which expression returns the "index of the first element of x equal to 3"?
(read this question carefully)
```
```m
>> x=[1 1 2 2 1 3 2 2 3 1]

x =

     1     1     2     2     1     3     2     2     3     1

>> x==3

ans =

     0     0     0     0     0     1     0     0     1     0

>> find(x==3)

ans =

     6     9

>> find(x==3,1)

ans =

     6

>> x=3

x =

     3
```
