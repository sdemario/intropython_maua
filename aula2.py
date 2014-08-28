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

p = Pessoa("Sheldon", 29)

print p.nome
print p.idade
p.set_profissao("Programador")

print p.profissao
