#---External Packages import start---
from flask_restful import Resource,reqparse
from flask import request
from datetime import datetime
from flask_security import login_user
#---External Packages import end---

#---Internal Packages import start---
from utilities.user_utilities import user_details_by_email, check_password, set_token_and_exp_time
#---Internal Packages import end---

#---Configure the Request Parser---
parser = reqparse.RequestParser()
parser.add_argument('email', type=str, help='Email is required and should be a string', required=True)
parser.add_argument('password', type=str, help='Password is required and should be a string', required=True)

#---API to check whether the user has successfully logged in ot not---
class UserLoginApi(Resource):
    def get(self):
        pass
    def put(self):
        pass
    #---Method to be used for user login authentication---
    def post(self):
        #---parsing the request arguments---
        data = request.get_json()

        #---extracting the request parameters---
        email = data.get('email')
        password = data.get('password')

        #---passing the parameters through various checks---
        if not email:
            return {"message": "email not provided"}, 400
        if not password:
            return {"message": "password not provided"}, 400
        
        #---extract out the user object matching the email id---
        user = user_details_by_email(email)

        #---checking whether the user object exists or not---
        if not user:
            return {"message": "User not found"}, 404
        
        #---checking whether the user is active or not---
        if not user.active:
            return {"message": "User's account not activated"}, 400
        
        #---Checking the entered password with the hashed password stored in the db---
        if check_password(user, password):
            #---Get the authentication token of the user---
            token = user.get_auth_token()
            #---set the token and the expiration time in the database
            set_token_and_exp_time(user, token)
            login_user(user)
            return {"id":user.id, "username":user.username, "role":user.roles[0].name, "email":user.email, "token":token}, 201
        else:
            #---If the password does not match, return the appropriate message---
            return {"message":"Wrong password"}, 400
    def delete(self):
        pass
