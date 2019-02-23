```
What is the vector b equal to after this block of code is executed?
```
```matlab
A = [1 0 -4 8 3; 4 -2 3 3 1];
b = zeros(1,5);
for index = 1:size(A,2)
  if A(1,index) > A(2,index)
    b(index) = A(1,index);
  else
    b(index) = A(2,index);
  end
end
```
<b>Solution:</b>
```m
>> A=[1,0,-4,8,3;4,-2,3,3,1];
>> A

A =

     1     0    -4     8     3
     4    -2     3     3     1

>> B=zeros(1,5);
>> B

B =

     0     0     0     0     0

>> for index=1:size(A,2)
if A(1,index)>A(2,index)
B(index)=A(1,index);
else
B(index)=A(2,index);
end
end
>> index

index =

     5

>> B

B =

     4     0     3     8     3
```
