'''

CLASSE DEVICE: SALVANDO DADOS NO DB
------------------------

'''

import sqlite3
from models import Device


conn = sqlite3.connect('dados.db')

dev = Device(conn)

dev.name = "Device de Testes"
dev.obs = "Teste de save"
dev.save()

raw_input("Tecle <Enter> para continuar")

dev.obs = "Teste de save: sucesso"
dev.save()

conn.close()
