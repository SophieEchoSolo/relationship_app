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
		# print(result)
finally:
	pass

app = Flask(__name__)
cors = CORS(app)

# How do I get the data from /newtypes to be inserted into the types table?
@app.route('/newtype', methods=['POST'])
def posttypes():
	data = request.form.to_dict(flat=True)
	print(data)
	# try:
	with connection.cursor() as cursor:
		sql = """INSERT INTO types (name, line_color, line_style) VALUES (%s, %s, %s)"""
		val = (data["r_type"], data["line_color"][-6:], data["line_style"])
		cursor.execute(sql, val)
		connection.commit()
		cursor.close()
	with connection.cursor() as cursor:
		sql = """SELECT * FROM types"""
		cursor.execute(sql)
		result = cursor.fetchall()
		return json.dumps(result)
	# except Exception as e: print(e)
	
@app.route('/newpeople', methods=['POST'])
def postpeople():
	data = request.form.to_dict(flat=True)
	print(data)
	with connection.cursor() as cursor:
		sql = """INSERT INTO people (name) VALUES (%s)"""
		val = (data["new_name"],)
		cursor.execute(sql, val)
		connection.commit()
		cursor.close()
	with connection.cursor() as cursor:
		sql = """SELECT * FROM people"""
		cursor.execute(sql)
		result = cursor.fetchall()
		return json.dumps(result)


@app.route('/newrelationship', methods=['POST'])
def postrelationship():
	data = request.form.to_dict(flat=True)
	print(data)
	with connection.cursor() as cursor:
		sql = """INSERT INTO relationships (type_id, people_a_id, people_b_id) VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE type_id=%s"""
		val = (data["type_id"], data["people_a_id"], data["people_b_id"], data["type_id"])
		cursor.execute(sql, val)
		connection.commit()
		cursor.close()
	with connection.cursor() as cursor:
		sql = """SELECT * FROM relationships"""
		cursor.execute(sql)
		result = cursor.fetchall()
		return json.dumps(result)
	
@app.route('/deleterelationship', methods=['POST'])
def deleterelationship():
	data = request.form.to_dict(flat=True)
	print(data)
	with connection.cursor() as cursor:
		sql = """DELETE FROM relationships WHERE people_a_id = %s && people_b_id = %s"""
		val = (data["people_a_id"], data["people_b_id"])
		cursor.execute(sql, val)
		connection.commit()
		cursor.close()
	with connection.cursor() as cursor:
		sql = """SELECT * FROM relationships"""
		cursor.execute(sql)
		result = cursor.fetchall()
		return json.dumps(result)
	
@app.route('/deleteperson', methods=['POST'])
def deleteperson():
	data = request.form.to_dict(flat=True)
	print(data)
	with connection.cursor() as cursor:
		sql = """DELETE FROM people WHERE id = %s"""
		val = (data["id"])
		cursor.execute(sql, val)
		connection.commit()
		cursor.close()
	with connection.cursor() as cursor:
		sql = """SELECT * FROM people"""
		cursor.execute(sql)
		result = cursor.fetchall()
		return json.dumps(result)

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