#---External Packages import start---
from flask_restful import Resource,reqparse, fields
from flask import request, jsonify
from flask_security import auth_required, roles_accepted, current_user
#---External Packages import end---

#---Internal Packages import start---
from utilities.playlist_utilities import add_song_to_playlist, delete_song_from_playlist, view_playlist_by_id
from utilities.token_expiration import check_token_expiration
#---Internal Packages import end---

#---API to implement the add/delete songs from a playlist---
class PlaylistSongIndividualApi(Resource):
    def get(self):
        pass
    #---Adding songs with the help of id's to the playlist with respect to the id---
    @auth_required("token")
    @roles_accepted("Admin","General_User")
    @check_token_expiration
    def post(self,playlist_id,song_id):
        user = current_user
        playlist = view_playlist_by_id(playlist_id)
        if playlist is None:
            return {"message":"Playlist id is invalid"}, 400
        if (user.roles[0]=="General_User" and user.username==playlist["created_by_user"]["name"]) or user.roles[0]=="Admin":
            check = add_song_to_playlist(playlist_id=playlist_id,song_id=song_id)
            if check==None:
                return {"message":"Song is not present"}, 400
            elif check==False:
                return {"message":"Song already present in playlist"}, 400
            else:
                return {"message":"Song has been added to the designated playlist"}, 201
        else:
            return {"message":"User not entitled to add songs in this playlist"}, 400
    def put(self):
        pass
    #---Deleting songs from a playlist w.r.t. the id from the designated playlist---
    @auth_required("token")
    @roles_accepted("Admin","General_User")
    @check_token_expiration
    def delete(self,playlist_id,song_id):
        user = current_user
        check = delete_song_from_playlist(playlist_id=playlist_id, song_id=song_id)
        playlist = view_playlist_by_id(playlist_id)
        if playlist is None:
            return {"message":"Playlist id is invalid"}, 400
        if (user.roles[0]=="General_User" and user.username==playlist["created_by_user"]["name"]) or user.roles[0]=="Admin":
            if check==None:
                return {"message":"Song id is invalid"}, 400
            elif check==False:
                return {"message":"Song is not present under designated playlist"}, 400
            else:
                return {"message":"Song is deleted from playlist"}, 201
        else:
            return {"message":"User not entitled to delete songs from this playlist"}