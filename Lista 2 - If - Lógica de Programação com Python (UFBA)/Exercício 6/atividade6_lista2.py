n1, n2, n3, n4, n5, n6 = input().split()
n1 = int(n1)
n2 = int(n2)
n3 = int(n3)
n4 = int(n4)
n5 = int(n5)
n6 = int(n6)

notaFinal = n1 + n2 + n3 + n4 + n5 + n6

if(notaFinal<=39):
  print("B-")
elif(notaFinal>=40 and notaFinal<=59):
  print("B")
elif(notaFinal>=60 and notaFinal<=79):
  print("B+")
elif(notaFinal>=80 and notaFinal<=99):
  print("A-")
elif(notaFinal>=100 and notaFinal<=149):
  print("A")
elif(notaFinal>=150 and notaFinal<=179):
  print("A+")
elif(notaFinal>=180 and notaFinal<=199):
  print("S-")
elif(notaFinal>=200 and notaFinal<=249):
  print("S")
elif(notaFinal>=250):
  print("S+")