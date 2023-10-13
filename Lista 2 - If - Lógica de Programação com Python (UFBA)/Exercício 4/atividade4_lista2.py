L, P = input().split()
L2, P2 = input().split()
L3, P3 = input().split()
L = int(L)
P = int(P)
L2 = int(L2)
P2 = int(P2)
L3 = int(L3)
P3 = int(P3)

L += L2 + L3
P += P2 + P3

if(L==P):
  print("Empate")
elif(L>P):
  print("Lucas")
else:
  print("Pedro")