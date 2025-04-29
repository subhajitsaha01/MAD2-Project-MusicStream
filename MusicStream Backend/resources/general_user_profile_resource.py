#---External Packages import start---
from flask_restful import Resource,fields, marshal
from flask import request
from flask_security import auth_required, roles_required
#---External Packages import end---

#---Internal Packages import start---
from utilities.user_utilities import find_general_user_by_id
from utilities.token_expiration import check_token_expiration
#---Internal Packages import end---

#---Configure the user output in a relevant manner---
general_user_fields = {
    "id": fields.Integer,
    "username": fields.String,
    "email": fields.String,
    "active": fields.Boolean
}

#---API to check the user is present or not in the Database---
class GeneralUserProfileApi(Resource):
    @auth_required("token")
    @roles_required("Admin")
    @check_token_expiration
    def get(self,id):
        user = find_general_user_by_id(id)
        if user=="User not found":
            return {'message':'User not found'}, 400
        elif user==None:
            return {'message':'User is not a general user'}, 400
        else:
            return marshal(user, general_user_fields)
    def put(self):
        pass
    def post(self):
        pass
    def delete(self):
        pass