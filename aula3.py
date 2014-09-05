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

mea = Measure(conn, dev)
mea.temperature = 20
mea.humidity = 79
mea.date = datetime.datetime.now().isoformat()
mea.latitude = -46.6941627
mea.longitude = -23.6086852
mea.save()

mea = Measure(conn)
mea.load(3)

print mea.device.id, mea.temperature, mea.humidity

conn.close()


'''
EXERCICIO:

Implemente a classe Measure que contenha todos os seus atributos necessarios e
persista seus dados no Banco de Dados
'''
