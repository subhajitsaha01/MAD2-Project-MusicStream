#---External Packages import start---
from flask_restful import Resource,reqparse, fields
from flask import request, jsonify
from flask_security import auth_required, roles_accepted, current_user
from datetime import date
#---External Packages import end---

#---Internal Packages import start---
from utilities.user_utilities import update_user_data, delete_user_by_id, view_user_by_id
from utilities.token_expiration import check_token_expiration
#---Internal Packages import end---

#---Configure the Request Parser---
parser = reqparse.RequestParser()
parser.add_argument('username', type=str, help='Username of the user is required and should be a string')
parser.add_argument('email', type=str, help='Email of the user is required and should be a string')
parser.add_argument('password', type=str, help='Password of the user is required and should be a string')


#---API to perform the CRUD operations using Users data individually, mainly updation and deletion of details---
class UsersIndividualApi(Resource):
    @auth_required("token")
    @roles_accepted("Admin","Creator","General_User")
    @check_token_expiration
    def get(self, id):
        user = view_user_by_id(id)
        user_current = current_user
        if user_current.id==id or user_current.roles[0]=="Admin":
            if user is None:
                return {"message":"No user with specific id present"}, 400
            else:
                return {'user':user}, 201
        else:
            return {"message":"User not authenticated to view the profile"}, 400
    def post(self):
        pass
    #---Method to perform updation of users data---
    @auth_required("token")
    @roles_accepted("Admin","Creator","General_User")
    @check_token_expiration
    def put(self, id):
        user = current_user
        if ((user.roles[0]=="General_User" or user.roles[0]=="Creator") and user.id==id) or user.roles[0]=="Admin":    
            #---Parsing the request arguments---
            args = parser.parse_args()
            data = request.get_json()

            #---Extracting the request parameters---
            username = data.get("username")
            email = data.get("email")
            password = data.get("password")
            
            #---Matching it with relevant conditions---
            if username and email and password:
                update_user_data(id,username=username,email=email,password=password)
            if username:
                update_user_data(id,username=username)
            if email:
                update_user_data(id,email=email)
            if password:
                update_user_data(id,password=password)
            return {"message":"User details are updated"}, 201
        else:
            return {"message":"User not entitled to update the details"}, 400
    #---Method to perform deletion of users data---
    @auth_required("token")
    @roles_accepted("Admin")
    @check_token_expiration
    def delete(self,id):
        delete_user_by_id(id)
        return {"message":"User data is deleted"}, 201