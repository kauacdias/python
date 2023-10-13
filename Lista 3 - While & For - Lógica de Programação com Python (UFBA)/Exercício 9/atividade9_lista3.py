a, b = map(int, input().split())
c = 0
r = False

for i in range(a):
  x, y  = map(int, input().split())
  b +=y
  c +=x
  if (c>b):
    r=True

if(r==True):
  print("Madara venceu")
else:
  print("Naruto defendeu a Vila")