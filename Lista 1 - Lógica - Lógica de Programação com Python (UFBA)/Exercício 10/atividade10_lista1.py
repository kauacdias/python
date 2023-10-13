s = int(input())

h = s//3600
m = (s-(h*3600))//60
mr = m*60 
sr = (s-(h*3600))-mr

print(f'{h}h {m}m {sr}s')