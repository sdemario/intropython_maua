'''

CLASSE DEVICE: CARREGANDO DADOS DO DB
------------------------

'''

import sqlite3
from models import Device


conn = sqlite3.connect('dados.db')

dev = Device(conn)
dev.name = 'Device Insert'

dev._insert()

conn.close()
