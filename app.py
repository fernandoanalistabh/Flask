from flask import Flask, jsonify, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Student_Controller(Resource):
    def get(self):
        return {"about":"hello world"}

    def post(self):
        student = request.get_json()
        return {'you sent': student}, 200

api.add_resource(Student_Controller, '/students')

if __name__ =="__main__":
    app.run(debug=True)