X, Y, Z = input().split()
X = int(X)
Y = int(Y)
Z = int(Z)

if(X>=Y and X>=Z):
  print(X)
elif(Y>=X and Y>=Z):
  print(Y)
else:
  print(Z)