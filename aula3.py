'''

CLASSE DEVICE: DELETANDO REGISTROS DO DB
------------------------

'''

import sqlite3
from models import Device


conn = sqlite3.connect('dados.db')

dev = Device(conn)
dev.load(3)
dev.delete()

conn.close()


'''
EXERCICIO:

Implemente a classe Measure que contenha todos os seus atributos necessarios e
persista seus dados no Banco de Dados
'''
