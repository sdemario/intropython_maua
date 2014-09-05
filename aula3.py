'''

CLASSE DEVICE: CARREGANDO DADOS DO DB
------------------------

'''

import sqlite3
from models import Device


conn = sqlite3.connect('dados.db')

dev = Device(conn)

dev.load(3)

dev.name = "Device update"

dev._update()

conn.close()
