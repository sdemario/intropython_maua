'''

TRATAMENTO DE ERROS E EXCECOES
----------------------------

try
except
finally
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
