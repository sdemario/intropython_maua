#!/usr/bin/python

from flask import Flask, request, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///maua.db'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

from model import *

@app.route('/')
def index():
	return "Hello, Maua!"


@app.route('/api/v1.0/alunos', methods=['GET'])
def aluno_list():
	alunos = []
	for i in Aluno.query.all():
		print i.nome, i.idade
		alunos.append({'id': i.id, 'nome': i.nome, 'idade': i.idade})

	return json.dumps(alunos)


if __name__ == '__main__':
	app.run(debug=True)
