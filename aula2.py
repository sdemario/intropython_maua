'''

TRATAMENTO DE ERROS E EXCECOES
----------------------------

try
except
finally
'''
import sys


notas = []
try:
    n = int(raw_input("digite a nota: "))
except:
    print "Voce nao digitou um numero valido"
    sys.exit(-1)

while n >= 0:
    notas.append(n)
    n = int(raw_input("digite a nota: "))

soma = 0
for i in notas:
    soma = soma + i

print soma / len(notas)
