FA, FD = input().split()
FA = int(FA)
FD = int(FD)
Resultado = FD-FA

if(Resultado%2==0 and FD>FA):
  print("vendido")
else:  
  print("sinto muito")