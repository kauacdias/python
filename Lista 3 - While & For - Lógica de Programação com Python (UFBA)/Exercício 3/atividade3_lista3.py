a = int(input())
x = int(input())
limite = a

while x!=0:
  x = int(input())
  if (x>a):
    limite=x

if (limite>a):
  print("ALARME")
else:
  print("O Havai pode dormir tranquilo")