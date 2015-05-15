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


@app.route('/api/aluno/new', methods=['POST'])
def aluno_new():
	if not request.json:
		return jsonify({'status': False})

	p = request.get_json()
	a = Aluno()
	a.nome = p['nome']
	a.idade = p['idade']
	db.session.add(a)
	db.session.commit()

	return jsonify({'status:': True})


if __name__ == '__main__':
	app.run(debug=True)
