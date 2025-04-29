#---External Packages import start---
from flask_restful import Resource
from flask import request
from datetime import datetime
from flask_security import logout_user, current_user, auth_required
#---External Packages import end---

#---Internal Packages import start---
from utilities.user_utilities import invalid_toke_exp_time
from utilities.token_expiration import check_token_expiration
#---Internal Packages import end---

#---API to check whether the user has successfully logged in ot not---
class UserLogoutApi(Resource):
    def get(self):
        pass
    def put(self):
        pass
    #---Method to be used for user logout token authentication---
    @auth_required("token")
    @check_token_expiration
    def post(self):
        invalid_toke_exp_time(current_user)
        logout_user()   
        return {"message":"Token has been invalidated"}, 201
    def delete(self):
        pass
