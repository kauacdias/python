A, M, C = input().split()
A = int(A)
M = int(M)
C = int(C)

A /= 2
M /= 3
C /= 5

A = int(A)
M = int(M)
C = int(C)

if(A<M and A<C):
  print(A)
elif(M<A and M<C):
  print(M)
else:
  print(C)