a = int(input())
y=0

for i in range(a):
  x=int(input())
  if (x==1):
    y +=1

if (y/a<0.3):
  print("Regiao segura")
elif (y/a>=0.3 and y/a<=0.5):
  print("Regiao em estado de alerta")
else:
  print("Regiao com alto indice de perda de biodiversidade")