'''

CONEXAO COM O BANCO DE DADOS (SQLITE)
------------------------

'''

import sqlite3


conn = sqlite3.connect('dados.db')
db = conn.cursor()


for row in db.execute("select * from device"):
    print row



conn.close()
