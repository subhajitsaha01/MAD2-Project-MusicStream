#---External Packages import start---
from flask_restful import Resource,reqparse, fields, marshal
from flask import request, jsonify
from flask_security import auth_required, roles_accepted
#---External Packages import end---

#---Internal Packages import start---
from utilities.album_utilities import  get_songs_by_album
from utilities.token_expiration import check_token_expiration
#---Internal Packages import end---

#---API to perform the CRUD operations using albums---
class AlbumSongIndividualApi(Resource):
    #---Method to list all songs under album---
    @auth_required("token")
    @roles_accepted("Admin","General_User","Creator")
    @check_token_expiration
    def get(self,id):
        songs,album_name = get_songs_by_album(id)
        if songs is None:
            return {"message":"No songs present under specific album"}, 400
        else:
            return {"name":album_name,"songs":songs}, 201
    def post(self):
        pass
    def put(self,id):
        pass
    def delete(self,id):
        pass