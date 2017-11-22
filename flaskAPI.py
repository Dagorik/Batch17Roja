from flask import Flask, jsonify
from flask import request
import json

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': 'Buy groceries',
        'description': 'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': 'Learn Python',
        'description': 'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

@app.errorhandler(404)
def page_not_found(e):
	return "ESTA PAGINA NO EXISTE"

@app.route('/tareas', methods = ['GET','POST'])
def index():
	if request.method == 'GET':
		return jsonify({'tareas':tasks})
	elif request.method == 'POST':
		print(request.json)
		return jsonify({'tareas':'POST'})

#http://127.0.0.1:5000/params?params1=HOLA
#http://localhost:5000/params?params1=Param_number_one&params2=Param_number_two
@app.route('/params')
def params():
	parametro = request.args.get('params1','valor por default')
	parametro2 = request.args.get('params2','valor por default')
	return "El parametro es: {}, {}".format(parametro,parametro2)

@app.route('/user/<name>/')
def user(name):
	print(type(name))
	return "Los parametros por path son : {}".format(name)

if __name__ == '__main__':
	app.run(debug = True, port = 5000)