'''

CLASSES - CLASSE x INSTANCIA
----------------------------

- Classe
  Em orientacao a objetos, uma classe e uma estrutura que abstrai um conjunto de
  objetos com caracteristicas similares. [wikipedia]

  - Estrutura da classe
       - Construtores
       - Destrutor
       - Propriedades/Atributos
       - Eventos/Metodos
'''

class Pessoa:
    nome = "Nome da Pessoa"
    idade = 100
    profissao = None

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def set_profissao(self, profissao):
        self.profissao = profissao


class Professor(Pessoa):
    profissao = "Professor"
    salario = 0

    def set_salario(self, valor):
        self.salario = valor


class Aluno(Pessoa):

    def __init__(self, nome, idade):
        Pessoa.__init__(self, nome, idade)
        self.notas = []

    def add_nota(self, valor):
        self.notas.append(valor)

    def media(self):
        soma = 0
        for i in self.notas:
            soma = soma + i

        media = soma / len(self.notas)
        return media


a = Aluno("Aluno 1", 18)
a.add_nota(5.0)
a.add_nota(6.0)
a.add_nota(6.0)

print "Media do aluno %s: %2.2f: " % (a.nome, a.media())

'''
EXERCICIO:

Escreva um metodo que retorne Verdadeiro se o aluno foi aprovado (media >= 5.0)
ou Falso se o aluno foi reprovado (media < 5.0). Depois, no programa principal,
imprima um status "Aprovado" ou "Reprovado".
'''
