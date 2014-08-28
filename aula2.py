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


p = Professor("Sheldon", 29)
print p.salario

p.set_salario(1000)
print p.salario

## Pessoa nao tem salario
