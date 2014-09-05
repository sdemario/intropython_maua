'''

SQL
------------------------

Structured Query Language, ou Linguagem de Consulta Estruturada ou SQL, é a
linguagem de pesquisa declarativa padrão para banco de dados relacional (base de
dados relacional). [wikipedia]


SUBCONJUNTOS:
    - INSERT
    - SELECT
    - UPDATE
    - DELETE

CLAUSULAS:
    - FROM
    - WHERE
    - GROUP BY
    - ORDER BY

ESTRUTURA:
     - INSERT
         Inserir registros

         INSERT INTO tabela (campo1, campo2) VALUES (1, "teste")


    - SELECT
        Consultar registros

        SELECT [campos] FROM tabela;


    - UPDATE
        Alterar registros

        UPDATE tabela SET campo = valor


    - DELETE
        Remover registros

        DELETE FROM tabela


EXEMPLOS:

     insert into device(name, obs) values ("Exemplo Sensor", "Sensor da Maua")
     select name, obs from device
     select * from device
     select name from device where id = 3
     update device set name = "sensor a" where id = 3
     delete from device where id = 2 where id = 3

'''
