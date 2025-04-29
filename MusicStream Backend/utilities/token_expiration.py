#---External Packages import start---
from flask import request
from functools import wraps
from datetime import datetime
#---External Packages import end---

#---Internal Packages import start---
from utilities.user_utilities import get_user_from_token
#---Internal Packages import end---

def check_token_expiration(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = request.args["auth_token"]
        if not token:
            return {"message":"Token is not provided"}, 401
        else:
            expiration_time = get_user_from_token(token)
            if expiration_time is None:
                return {"message":"Token is invalid"}, 401
            if datetime.utcnow() > expiration_time:
                return {"message":"Token has expired"}, 401
        return func(*args, **kwargs)
    return wrapper