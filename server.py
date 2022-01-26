#!/usr/bin/python3
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps

db_connect = create_engine('sqlite:///chinook.db')
app = Flask(__name__)
app.config["DEBUG"] = True
api = Api(app)


class Employees(Resource):
    def get(self):
        conn = db_connect.connect() # connect to database
        query = conn.execute("select * from employees") # This line performs query and returns json result
        return {'employees': [i[0] for i in query.cursor.fetchall()]} # Fetches first column that is Employee ID

    def post(self):
        conn = db_connect.connect()
        print(request.json)
        LastName = request.json['LastName']
        FirstName = request.json['FirstName']
        City = request.json['City']
        State = request.json['State']
        Country = request.json['Country']
        Email = request.json['Email']
        query = conn.execute("insert into employees values(null,'{0}','{1}','{2}','{3}', \
                             '{4}','{5}')".format(LastName, FirstName, City, State, Country, Email))
        return {'status':'success'}


class Tracks(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select trackid, name, composer, unitprice from tracks;")
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class TrackID(Resource):
        def ger(self, TrackId):
            conn = db_connect.connect()
            query = conn.execute("select * from tracks where trackid = %d "  %int(TrackId))
            result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
            return jsonify(result)

class Employees_Name(Resource):
    def get(self, employee_id):
        conn = db_connect.connect()
        query = conn.execute("select * from employees where EmployeeId =%d "  %int(employee_id))
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class Update_Info(Resource): # Update employees information
    def patch(self, employee_id):
        conn = db_connect.connect()
        print(request.json)
        LastName = request.json['LastName']
        FirstName = request.json['FirstName']
        City = request.json['City']
        State = request.json['State']
        Country = request.json['Country']
        Email = request.json['Email']
        query = conn.execute("insert into employees values(null,'{0}','{1}','{2}','{3}', \
                             '{4}','{5}')".format(LastName, FirstName, City, State, Country, Email))
#### UPDATE employees SET LastName=gosho, FirstName=gosho WHERE EmployeeId=1
        return {'status':'success'}

class clothes(Resource):
    def get(self):
        conn = db_connect.connect() # connect to database
        query = conn.execute("select * from clothes") # This line performs query and returns json result
        return {'clothes': [i[0] for i in query.cursor.fetchall()]}

    def post(self):
        conn = db_connect.connect()
        print(request.json)
        brand = request.json['brand']
        type = request.json['type']
        color = request.json['color']
        gender = request.json['gender']
        query = conn.execute("insert into clothes values(null,'{0}','{1}','{2}','{3}', \
                             )".format(brand, type, color, gender))
        return {'status':'success'}

class clothesid(Resource):
    def get(self, clothesid):
        conn = db_connect.connect()
        query = conn.clothes("select * from clothes where clothesid =%d "  %int(clothesid))
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

api.add_resource(Employees, '/employees') # Route_1
api.add_resource(Tracks, '/tracks') # Route_2
api.add_resource(Employees_Name, '/employees/<employee_id>') # Route_3
api.add_resource(TrackID, '/tracks/<trackid>')
api.add_resource(Update_Info, '/employees/<employee_id>') #
api.add_resource(clothes, '/clothes')
api.add_resource(clothesid, '/clothes/<clothesid>')

if __name__ == '__main__':
     app.run()
