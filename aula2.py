'''

EXERCICIO FUNCAO
----------------------------

Melhore o programa de notas escrevendo uma funcao que mostre a maior nota lida

'''
import sys


notas = []
n = 0

while n >= 0:
    while True:
        try:
            n = int(raw_input("digite a nota: "))
            break
        except:
            print "Voce nao digitou um numero valido"
    notas.append(n)

notas.remove(-1)
soma = 0
for i in notas:
    soma = soma + i

print soma / len(notas)
