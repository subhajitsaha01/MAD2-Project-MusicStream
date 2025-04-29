#---External Packages import start---
from flask_restful import Resource,reqparse
from flask import request
from flask_security import auth_required, roles_required
#---External Packages import end---

#---Internal Packages import start---
from utilities.user_utilities import activate_user_by_id
from utilities.token_expiration import check_token_expiration
#---Internal Packages import end---

#---API to activate an user by admin---
class UserActivationApi(Resource):
    def get(self):
        pass
    def post(self):
        pass
    #---Activation of an user by id by admin after authentication---
    @roles_required("Admin")
    @auth_required("token")
    @check_token_expiration
    def put(self, id):
        activate_user_by_id(id)
        return {'message':'User is activated'}, 201
    def delete(self):
        pass