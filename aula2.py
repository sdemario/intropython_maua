'''

MOSTRAR DADOS
----------------------------

Queremos mostrar todas as notas dos alunos logo apos o seu resumo
'''

from classes import Aluno


alunos = []
a = Aluno("Aluno 1", 18)
a.add_nota(5.0)
a.add_nota(6.0)
a.add_nota(4.0)
alunos.append(a)

b = Aluno("Aluno 2", 20)
b.add_nota(8.0)
b.add_nota(9.0)
b.add_nota(6.5)
alunos.append(b)

c = Aluno("Aluno 3", 19)
c.add_nota(4.0)
c.add_nota(3.5)
c.add_nota(2.0)
alunos.append(c)


######################################################

for i in alunos:
    resultado = "Aprovado" if i.aprovado() else "Reprovado"
    print "Media do aluno %s: %2.2f - %s " % (i.nome, i.media(), resultado)
    i.mostra_notas()
