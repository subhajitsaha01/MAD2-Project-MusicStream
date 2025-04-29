#---External Packages import start---
from flask_restful import Resource,reqparse, fields
from flask import request, jsonify, send_file
from flask_security import auth_required, roles_accepted
from datetime import date
#---External Packages import end---

#---Internal Packages import start---
from utilities.song_utilities import view_song_by_its_id,update_song_by_its_id, delete_song_by_its_id
from utilities.token_expiration import check_token_expiration
#---Internal Packages import end---

#---API to perform the Listen operations on Individual Song data---
class SongsListenApi(Resource):
    #---To get the data about an individual song using the song id---
    @auth_required("token")
    @roles_accepted("Admin","General_User","Creator")
    @check_token_expiration
    def get(self,filename):
        return send_file("songs/"+filename, mimetype='audio/mpeg')
    def post(self):
        pass
    def put(self,id):
        pass
    def delete(self,id):
        pass