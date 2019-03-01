```m
>> A=[1,2,3,4,5;2,3,4,5,6;3,4,5,6,7;4,5,6,7,8;5,6,7,8,9]

A =

     1     2     3     4     5
     2     3     4     5     6
     3     4     5     6     7
     4     5     6     7     8
     5     6     7     8     9

>> A(:,1:2:5)

ans =

     1     3     5
     2     4     6
     3     5     7
     4     6     8
     5     7     9

>> [A(:,1) A(:,3) A(:,5)]

ans =

     1     3     5
     2     4     6
     3     5     7
     4     6     8
     5     7     9

>> A(:,1:3)

ans =

     1     2     3
     2     3     4
     3     4     5
     4     5     6
     5     6     7

>> [A(1,:) A(1,:) A(1,:)]

ans =

     1     2     3     4     5     1     2     3     4     5     1     2     3     4     5

>> A(1:2:5,:)

ans =

     1     2     3     4     5
     3     4     5     6     7
     5     6     7     8     9
```