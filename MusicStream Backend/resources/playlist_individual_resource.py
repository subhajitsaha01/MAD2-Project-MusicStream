#---External Packages import start---
from flask_restful import Resource,reqparse, fields
from flask import request, jsonify
from flask_security import auth_required, roles_accepted, current_user
#---External Packages import end---

#---Internal Packages import start---
from utilities.playlist_utilities import view_playlist_by_id, update_playlist_by_id, delete_playlist_by_id
from utilities.token_expiration import check_token_expiration
#---Internal Packages import end---

#---Configure the Request Parser---
parser = reqparse.RequestParser()
parser.add_argument('name', type=str, help='Name of the playlist is required and should be a string', required=True)
parser.add_argument('description', type=str, help='Description of the playlist is required and should be a string', required=True)

#---Configure the album data output in a relevant manner---
playlist_data_fields = {
    "playlist_id":fields.Integer,
    "playlist_name":fields.String,
    "playlist_description":fields.String,
    "date_created":fields.List,
    "created_by_user":fields.Integer
}

#---API to perform CRUD operations on the Playlist Table---
class PlaylistIndividualApi(Resource):
    #---Operation to get the playlist by id and inspect the data inside---
    @auth_required("token")
    @roles_accepted("Admin","General_User")
    @check_token_expiration
    def get(self, id):
        user = current_user
        playlist = view_playlist_by_id(id)
        if playlist is None:
                return {"message":"No playlist is present with that id"}, 400
        if (user.roles[0]=="General_User" and user.username==playlist["created_by_user"]["name"]) or user.roles[0]=="Admin":
                return playlist, 201
        else:
            return {"message":"User not authorized to access this playlist details"}, 400
    #---Operation to update the details of a playlist by id---
    @auth_required("token")
    @roles_accepted("Admin","General_User")
    @check_token_expiration
    def put(self,id):
        #---Parsing the request arguments---
        args = parser.parse_args()
        data = request.get_json()
        user = current_user
        
        #---Extracting the request parameters---
        playlist_name = data.get("name")
        playlist_description = data.get("description")
        playlist = view_playlist_by_id(id)
        
        #---matching it with the relevant conditions---
        if (user.roles[0]=="General_User" and user.username==playlist["created_by_user"]["name"]) or user.roles[0]=="Admin":
            if playlist_name and playlist_description:
                update_playlist_by_id(id,playlist_name=playlist_name,playlist_description=playlist_description)
                return {"message":"Playlist name and description have been updated"}, 201
            elif playlist_name:
                update_playlist_by_id(id,playlist_name=playlist_name)
                return {"message":"Playlist name have been updated"}, 201
            elif playlist_description:
                update_playlist_by_id(id,playlist_description=playlist_description)
                return {"message":"Playlist description have been updated"}, 201
        else:
            return {"message":"User not authorized to update this playlist details"}, 400
    def post(self):
        pass
    #---Operation to delete the playlist with specific playlist id---
    @auth_required("token")
    @roles_accepted("Admin","General_User")
    @check_token_expiration
    def delete(self, id):
        user = current_user
        playlist = view_playlist_by_id(id)
        if playlist is None:
            return {"message":"Playlist with given id does not exist"}, 201        
        if (user.roles[0]=="General_User" and user.username==playlist["created_by_user"]["name"]) or user.roles[0]=="Admin":
            delete_playlist_by_id(id)
            return {"message":"Playlist data is deleted"}, 201
        else:
            return {"message":"User not authorized to access this playlist details"}, 400