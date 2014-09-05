'''

CLASSE DEVICE: CARREGANDO DADOS DO DB
------------------------

'''

import sqlite3
from models import Device


conn = sqlite3.connect('dados.db')

dev = Device(conn)
print dev.name

dev.load(1)
print dev.name


conn.close()
