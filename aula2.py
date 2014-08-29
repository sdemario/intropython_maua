'''

EXERCICIO
----------------------------

1 - Data de nascimento

Faca uma alteracao no programa/clases para que ao inves da idade seja cadastrada
a data de nascimento e o metodo idade retorne a idade calculada segundo a data
de nascimento. Mostre na tela junto ao resumo de notas.

DICA: modulo datetime
     https://docs.python.org/2/library/datetime.html


2 - Melhor aluno da turma

Faca uma alteracao no programa para que todos os alunos e um professor sejam
associados a uma turma e esta tenha um metodo que retorne o aluno com a melhor
media.

DICA: classe Turma
'''

from classes import Aluno


alunos = []
a = Aluno("Aluno 1", 18)
a.add_nota("Trabalho 1", 5.0)
a.add_nota("Trabalho 2", 6.0)
a.add_nota("Prova", 4.0)
alunos.append(a)

b = Aluno("Aluno 2", 20)
b.add_nota("Trabalho 1", 8.0)
b.add_nota("Trabalho 2", 9.0)
b.add_nota("Prova", 6.5)
alunos.append(b)

c = Aluno("Aluno 3", 19)
c.add_nota("Trabalho 1", 4.0)
c.add_nota("Trabalho 2", 3.5)
c.add_nota("Prova", 2.0)
alunos.append(c)


######################################################

for i in alunos:
    resultado = "Aprovado" if i.aprovado() else "Reprovado"
    print "Media do aluno %s: %2.2f - %s " % (i.nome, i.media(), resultado)
    i.mostra_notas()
