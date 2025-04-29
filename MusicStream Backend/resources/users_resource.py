#---External Packages import start---
from flask_restful import Resource,reqparse, fields
from flask import request, jsonify
from flask_security import auth_required, roles_accepted
from datetime import date
#---External Packages import end---

#---Internal Packages import start---
from utilities.user_utilities import get_users
from utilities.token_expiration import check_token_expiration
#---Internal Packages import end---

#---Configure the album data output in a relevant manner---
user_data_fields = {
    "id":fields.Integer,
    "username":fields.String,
    "email":fields.String,
    "active":fields.Integer,
}

#---API to perform the CRUD operations using songs---
class UsersApi(Resource):
    #---Get the list of songs currently present for a database---
    @auth_required("token")
    @roles_accepted("Admin")
    @check_token_expiration
    def get(self):
        users = get_users()
        if users is None:
            return {"message":"No users present in the database"}, 201
        else:
            return {'users':users}, 201
    def post(self):
        pass
    def put(self):
        pass
    def delete(self):
        pass