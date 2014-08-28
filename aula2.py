'''

EXERCICIO FUNCAO
----------------------------

Melhore o programa de notas escrevendo uma funcao que mostre a maior nota lida

'''
import sys


notas = []
n = 0

def maior_nota(lista):
    maior = 0
    for i in notas:
        if i > maior:
            maior = i

    return i

def media_notas(lista):
    soma = 0
    for i in notas:
        soma = soma + i

    media = soma / len(lista)
    return media

while n >= 0:
    while True:
        try:
            n = int(raw_input("digite a nota: "))
            break
        except:
            print "Voce nao digitou um numero valido"
    notas.append(n)

notas.remove(-1)

media = media_notas(notas)
maior = maior_nota(notas)

print 'Media: %2.2f  Maior nota: %d ' % (media, maior)
