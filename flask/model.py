from mauaserver import db

class Aluno(db.Model):
	id		= db.Column(db.Integer, primary_key=True)
	nome	= db.Column(db.String(100))
	idade	= db.Column(db.Integer)
