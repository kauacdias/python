a = int(input())
b = int(input())
resultado = []
y = 0
x = 0

for i in range(a):
  for i in range(b):
    c, d = map(int, input().split())
    y += c
    x += d

  resultado.append((y,x))
  y=0
  x=0

for y, x in resultado:
  print(y, x)