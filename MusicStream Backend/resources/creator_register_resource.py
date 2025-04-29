#---External Packages import start---
from flask_restful import Resource,reqparse
from flask import request
#---External Packages import end---

#---Internal Packages import start---
from utilities.user_utilities import email_exists, username_exists, insert_creator
#---Internal Packages import end---

#---Configure the Request Parser---
parser = reqparse.RequestParser()
parser.add_argument('username', type=str, help='Username is required and should be a string', required=True)
parser.add_argument('email', type=str, help='Email is required and should be a string', required=True)
parser.add_argument('password', type=str, help='Password is required and should be a string', required=True)

#---API to check the user is present or not in the Database---
class CreatorRegistrationApi(Resource):
    def get(self):
        pass
    def put(self):
        pass
    #---Method for User Registration---
    def post(self):
        #---parsing the request arguments---
        args = parser.parse_args()
        data = request.get_json()
        
        #---extracting the request parameters---
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        #---matching it with the relevant conditions---
        if not email:
            return {"message":"Email not provided"}, 400
        if not username:
            return {"message":"Username not provided"}, 400
        if not password:
            return {"message":"Password not provided"}, 400
        if email_exists(email) or username_exists(username):
            return {"message":"Email or username prexists in the backend"}, 400
        else:
            insert_creator(username=username,email=email,password=password)
            return {"message":"Creator is created"}, 201
    def delete(self):
        pass