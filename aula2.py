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
except ValueError:
    print "Voce nao digitou um numero valido"
    sys.exit(-1)
except TypeError:
    print "Erro de tipo"
finally:
    print "Passarei por aqui em qualquer circunstancia"

while n >= 0:
    notas.append(n)
    n = int(raw_input("digite a nota: "))

soma = 0
for i in notas:
    soma = soma + i

print soma / len(notas)
