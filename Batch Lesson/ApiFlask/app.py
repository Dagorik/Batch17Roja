from flask import Flask, jsonify
from flask import request
import json
from firebaseuser import FirebaseUser

app = Flask(__name__)
database = FirebaseUser()

@app.route('/user', methods = ['GET','POST'])
def index():
	if request.method == 'GET':
		data = database.getallusers()
		lista = []
		lista.append(data)			
		return jsonify({'users':lista})
	elif request.method == 'POST':
		data = request.json
		user = database.createUser(data)
		lista = []
		lista.append(user)
		return jsonify({'tareas':lista})

if __name__ == '__main__':
	app.run(debug = True, port = 5000)