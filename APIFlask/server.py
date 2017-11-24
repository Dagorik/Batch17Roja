from flask import Flask, jsonify,request
import json
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
print(db)


@app.route('/usuarios',methods = ['GET','POST'])
def users():
	if request.method == 'GET':
		sql = text('select * from user_cinta')
		result = db.engine.execute(sql)
		names = []
		for row in result:
			names.append(row[1])
		return jsonify({"nombres":names})
		
	elif request.method == 'POST':
		return "POST"


if __name__ == '__main__':
	app.run(debug = True, port = 5000)
