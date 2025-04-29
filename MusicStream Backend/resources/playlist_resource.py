#---External Packages import start---
from flask_restful import Resource,reqparse, fields
from flask import request, jsonify
from flask_security import auth_required, roles_accepted
#---External Packages import end---

#---Internal Packages import start---
from utilities.playlist_utilities import view_playlists
from utilities.token_expiration import check_token_expiration
#---Internal Packages import end---

#---Configure the Request Parser---
parser = reqparse.RequestParser()
parser.add_argument('name', type=str, help='Name of the playlist is required and should be a string', required=True)
parser.add_argument('description', type=str, help='Description of the playlist is required and should be a string', required=True)
parser.add_argument('date_created', type=str, help='Date of the creation of the playlist is required and should be a string', required=True)
parser.add_argument('created_by_user', type=int, help='Creator of the playlist user id is required and should be a integer', required=True)

#---Configure the album data output in a relevant manner---
playlist_data_fields = {
    "playlist_id":fields.Integer,
    "playlist_name":fields.String,
    "playlist_description":fields.String,
    "date_created":fields.List,
    "created_by_user":fields.Integer
}

#---API to perform CRUD operations using playlists---
class PlaylistApi(Resource):
    #---Get the list of all playlists present in the database---
    @auth_required("token")
    @roles_accepted("Admin","General_User")
    @check_token_expiration
    def get(self):
        playlist = view_playlists()
        if playlist is None:
            return {"message":"No playlist is present in the database"}, 400
        else:
            return {"playlists":playlist}, 201
    def post(self):
        pass
    def put(self):
        pass
    def delete(self):
        pass