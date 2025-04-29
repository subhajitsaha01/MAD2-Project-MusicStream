#---External Packages import start---
from flask_security import hash_password, verify_password
from datetime import datetime, timedelta
#---External Packages import end---

#---Internal Packages import start---
from db.database import db
from models.models import datastore, Users
#---Internal Packages import end---

#---Utility function to get user from token---
def get_user_from_token(token):
    user = datastore.find_user(remember_token=token)
    if user is None:
        return None
    else:
        return user.remember_token_expires

#---Utility function to set the expiration time---
def invalid_toke_exp_time(user):
    user.remember_token_expires = datetime.utcnow() - timedelta(seconds=1)
    db.session.commit()

#---Utility function to add token and set the expiration time---
def set_token_and_exp_time(user, token):
    user.remember_token_expires = datetime.utcnow() + timedelta(hours=1)
    user.remember_token = token
    db.session.commit()

#---Utility function to check email pre-exists or not---
def email_exists(email):
    return datastore.find_user(email=email)

#---Utility function to check username pre-exists or not---
def username_exists(username):
    return datastore.find_user(username=username)

#---Utility function to create an user and insert it into the datastore---
def insert_general_user(username, email, password):
    datastore.create_user(username=username,email=email,password=hash_password(password),active=False,roles=["General_User"])
    db.session.commit()

#---Utility function to create an user and make a creator and insert it into the datastore---
def insert_creator(username, email, password):
    datastore.create_user(username=username, email=email, password=hash_password(password),active=False,roles=["Creator"])
    db.session.commit()

#---Utility function to extract the details of the matched user object---
def user_details_by_email(email):
    user = datastore.find_user(email=email)
    return user

#---Utility function to activate an user object matching by id---
def activate_user_by_id(id):
    Users.query.filter_by(id=id).update({'active':True})
    db.session.commit()

#---Utility function to deactivate an user object matching by id---
def deactivate_user_by_id(id):
    Users.query.filter_by(id=id).update({'active':False})
    db.session.commit()

#---Utility function to check the password and stored password in db---
def check_password(user, password):
    return verify_password(password, user.password)

#---Utility function extract out an user filtered by id and extracting the first object matching the condition---
def find_general_user_by_id(id):
    user = Users.query.filter_by(id=id).first()
    if user!=None:
        if user.roles[0].name=="General_User":
            return user
        else:
            return None
    else:
        return "User not found"

#---Utility function to filter a creator by id and returning the object---
def find_creator_by_id(id):
    creator = Users.query.filter_by(id=id).first()
    if creator!=None:
        if creator.roles[0].name=="Creator":
            return creator
        else:
            return None
    else:
        return "User not found"

#---Utility function to get users---
def get_users():
    data = []
    users = Users.query.all()
    if users is None:
        return None
    else:
        for user in users:
            data_user = {'id':user.id,'username':user.username, 'email':user.email, 'role':user.roles[0].name,'active':user.active}
            data.append(data_user)
        return data

#---Utility function to update the data of users by id---
def update_user_data(id,username=None,email=None,password=None):
    if username is not None:
        Users.query.filter_by(id=id).update({'username':username})
    if email is not None:
        Users.query.filter_by(id=id).update({'email':email})
    if password is not None:
        Users.query.filter_by(id=id).update({'password':hash_password(password)})
    db.session.commit()
    
#---Utility function to delete the data of user by id---
def delete_user_by_id(id):
    user = Users.query.filter_by(id=id).first()
    user.roles = []
    db.session.commit()
    playlists = user.playlists
    for playlist in playlists:
        db.session.delete(playlist)
    user.playlists = []
    db.session.commit()
    db.session.delete(user)
    db.session.commit()
    
#---Utility function to view the profile of the user---
def view_user_by_id(id):
    user = Users.query.filter_by(id=id).first()
    if user is None:
        return None
    else:
        data = {'id':user.id, 'username':user.username, 'email':user.email}
        return data