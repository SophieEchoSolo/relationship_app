import pymysql.cursors
from flask import Flask, escape, request
import json
from flask_cors import CORS

# Connect to the database
connection = pymysql.connect(host='localhost',
							 user='root',
							 password='',
							 db='relationship_app',
							 charset='utf8mb4',
							 cursorclass=pymysql.cursors.DictCursor)

try:
	with connection.cursor() as cursor:
		sql = """SELECT * FROM people"""
		cursor.execute(sql)
		result = cursor.fetchall()
		print(result)
finally:
	pass

app = Flask(__name__)
cors = CORS(app)

@app.route('/nodes')
def getnodes():
	try:
		with connection.cursor() as cursor:
			sql = """SELECT * FROM people"""
			cursor.execute(sql)
			result = cursor.fetchall()
			return json.dumps(result)
	finally:
		pass
	return '[]'

@app.route('/links')
def getlinks():
	try:
		with connection.cursor() as cursor:
			sql = """SELECT types.name, types.line_color, types.line_style, relationships.people_a_id, relationships.people_b_id  FROM relationships JOIN types	ON relationships.type_id = types.id"""
			cursor.execute(sql)
			result = cursor.fetchall()
			return json.dumps(result)
	finally:
		pass
	return '[]'

@app.route('/types')
def gettypes():
	try:
		with connection.cursor() as cursor:
			sql = """SELECT * FROM types"""
			cursor.execute(sql)
			result = cursor.fetchall()
			return json.dumps(result)
	finally:
		pass
	return '[]'

if __name__ == "__main__":
	app.run(host='0.0.0.0',port=5000)