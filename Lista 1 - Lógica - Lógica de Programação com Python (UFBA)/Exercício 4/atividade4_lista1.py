prova, segundaProva, trabalho = input().split()
prova = float(prova)
segundaProva = float(segundaProva) 
trabalho = float(trabalho)
mediaPonderada = ((prova*4)+(segundaProva*4)+(trabalho*2))/10
print(format(mediaPonderada, ".2f"))