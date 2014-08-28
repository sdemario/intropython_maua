'''

EXERCICIO NOTAS/MEDIA
-----------------------------

Faca um programa que leia notas de diversos alunos e calcule a media
a lista termina quando e digitado um numero negativo

'''

notas = []
n = int(raw_input("digite a nota: "))
while n >= 0:
    notas.append(n)
    n = int(raw_input("digite a nota: "))

soma = 0
for i in notas:
    soma = soma + i

print soma / len(notas)
