from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from data import students, error

app = Flask(__name__)
api = Api(app)

@app.route('/students', methods = ['GET'])
def get():
    return jsonify(students)

@app.route('/students/<int:id>', methods = ['GET'])
def get_by_id(id):
    for student in students:
        if student['id']==id:
            return jsonify(student), 200
    return jsonify(error), 400

@app.route('/students', methods = ['POST'])
def post():
    std = request.get_json()
    for student in students:
        if student['id']==std['id']:
            return "Estudante já adicionado.", 400
    students.append(std)
    return jsonify(std), 201

@app.route('/students', methods = ['PUT'])
def put():
    std = request.get_json()
    for student in students:
        if student['id']==std['id']:
            student['name'] = std['name']
            student['passport_number'] = std['passport_number']
            return jsonify(student), 200
    return jsonify(error), 400

@app.route('/students/<int:id>', methods = ['DELETE'])
def delete(id):
    for student in students:
        if student['id']==id:
            students.remove(student)
            return jsonify(student), 200
    return jsonify(error), 400


if __name__ =="__main__":
    app.run(debug=True)