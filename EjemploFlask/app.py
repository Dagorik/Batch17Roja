from flask import Flask, jsonify, render_template
from flask import request
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import text
import json

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

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

@app.route('/usuarios',methods = ['GET','POST'])
def users():
    if request.method == 'GET':
        sql = text('select * from user_prueba')
        result = db.engine.execute(sql)
        names = []
        for row in result:
            print(row)
            names.append(row[1])
        return jsonify({'nombres':names})

    elif request.method == 'POST':
        if not request.json:
            return "No es un json"
        id_user = request.json['id']
        name = request.json['nombre']
        last_name = request.json['last_name']
        age = request.json['age']
        sql = "insert into user_prueba(id_user,nombre,apellido,edad) values ({},'{}','{}',{});".format(id_user,name,last_name,age)
        result = db.engine.execute(sql)
        #json.dumps(request.json),201
        return jsonify(request.json),201



@app.errorhandler(404)
def page_not_found(e):
	return render_template('untitled.html')

@app.route('/tareas', methods = ['GET','POST'])
def index():
	if request.method == 'GET':
		return jsonify({'tareas':tasks})
	elif request.method == 'POST':
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