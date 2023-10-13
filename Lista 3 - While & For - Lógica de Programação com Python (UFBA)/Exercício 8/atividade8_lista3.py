a, b = map(int, input().split())
d = 1

for i in range(a):
  c = int(input())
  b -= c

  if(b>0):
    d+=1

if(b>0):
  print("Resistiu")
else:
  print(d)