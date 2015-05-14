#!/usr/bin/python

from flask import Flask, request, jsonify
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/')
def index():
	return "Hello, Maua!"



if __name__ == '__main__':
	app.run(debug=True)
