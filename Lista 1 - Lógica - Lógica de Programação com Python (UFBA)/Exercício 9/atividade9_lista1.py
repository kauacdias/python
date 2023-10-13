tamanho, distancia = input().split()
tamanho = int(tamanho)
distancia = int(distancia)

valor, pedagio = input().split()
valor = int(valor)
pedagio = int(pedagio)

valorTamanho = tamanho * valor

distancia = tamanho//distancia
distancia *= pedagio

vf = distancia + valorTamanho

print(vf)