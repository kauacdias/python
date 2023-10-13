S = int(30)
M = int(6)
C = int(3)

Se, Me, Ce = input().split()

S -= int(Se)
M -= int(Me)
C -= int(Ce)

if(S==0):
  print("PROXIMO MUNDO")
else:
  print(S, M, C)