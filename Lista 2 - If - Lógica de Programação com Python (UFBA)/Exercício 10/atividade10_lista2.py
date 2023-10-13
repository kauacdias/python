z, g = input().split()
d, c = input().split()

if((z=="e" and d=="e") or (z=="d" and d=="d")):
  if((g=="e" and c=="e") or (g=="d" and c=="d")):
    print("Driblado")
    print("Gol")

if((z=="e" and d=="e") or (z=="d" and d=="d")):
  if((g=="e" and c=="d") or (g=="d" and c=="e")):
    print("Driblado")
    print("...e o goleiro pega")

if((z=="e" and d=="d") or (z=="d" and d=="e")):
    print("Bloqueado")