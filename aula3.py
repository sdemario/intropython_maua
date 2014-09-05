'''

CLASSE DEVICE: DELETANDO REGISTROS DO DB
------------------------

'''

import sqlite3
import datetime
from models import Device, Measure


conn = sqlite3.connect('dados.db')

dev = Device(conn)
dev.load(1)

print "As medidas aferidas para o Device %s sao: " % dev.name
for mea in dev.measures():
    print dev.name, mea.device.id, mea.temperature, mea.humidity

conn.close()


'''
EXERCICIO:

Implemente a classe Measure que contenha todos os seus atributos necessarios e
persista seus dados no Banco de Dados
'''
