#---External Packages import start---
from flask_restful import Resource,reqparse, fields
from flask import request, jsonify
from flask_security import auth_required, roles_accepted, current_user
from datetime import date
#---External Packages import end---

#---Internal Packages import start---
from utilities.song_utilities import add_rating_song_by_user, get_rating_song_by_user, update_rating_song_by_user, delete_rating_song_by_user
from utilities.token_expiration import check_token_expiration
#---Internal Packages import end---

#---Configure the Request Parser---
parser = reqparse.RequestParser()
parser.add_argument('rating', type=float, help='Rating of the song is required', required=True)

#---Configure the album data output in a relevant manner---
song_rating_data_fields = {
    "rating_id":fields.Integer,
    "song_id":fields.Integer,
    "user_id":fields.Integer,
    "rating":fields.Float
}

#---API to perform CRUD operations on album rating by user---
class SongRating(Resource):
    #---Get the rating of the album by the respective user
    @auth_required("token")
    @roles_accepted("Admin","General_User","Creator")
    @check_token_expiration
    def get(self, id, song_id):
        user = current_user
        if user.id==id:
            song_rating = get_rating_song_by_user(id=id, song_id=song_id)
            if song_rating is None:
                return {"message":"Rating not present for this song by user"}, 400
            else:
                return song_rating, 201
        else:
            return {"message":"User not entitled to get the rating of the song"}, 400
    #---Update the rating of the album by the respective user---
    @auth_required("token")
    @roles_accepted("Admin","General_User","Creator")
    @check_token_expiration
    def put(self,id, song_id):
        #---Parsing the request arguments---
        args = parser.parse_args()
        data = request.get_json()
        user = current_user

        if user.id==id:
            #---Extracting the request parameters---
            rating = data.get("rating")
            
            #---Matching it with the relevant conditions---
            if not rating:
                return {"message":"Rating is not provided"}, 400
            else:
                status = update_rating_song_by_user(id=id,song_id=song_id,rating=rating)
                if status==True:
                    return {"message":"Rating is updated"}, 201
                else:
                    return {"message":"Rating not provided"}, 400
        else:
            return {"message":"User is not entitled to update the rating of the song"}, 400
    #---Add the rating of the album by the respective user---
    @auth_required("token")
    @roles_accepted("Admin","General_User","Creator")
    @check_token_expiration
    def post(self,id,song_id):
        #---Parsing the request arguments---
        args = parser.parse_args()
        data = request.get_json()
        user = current_user

        if user.id==id:
            #---Extracting the request parameters---
            rating = data.get("rating")
            
            #---Matching it with the relevant conditions---
            if not rating:
                return {"message":"Rating is not provided"}, 400
            else:
                status = add_rating_song_by_user(id=id,song_id=song_id,rating=rating)
                if status==True:
                    return {"message":"Rating is added to the song"}, 200
                else:
                    return {"message":"Rating is already present for the song by the user"}, 400
        else:
            return {"message":"User is not entitled to rate the song"}, 400
    #---Delete the rating of the album by the respective user---
    @auth_required("token")
    @roles_accepted("Admin","General_User","Creator")
    @check_token_expiration
    def delete(self,id,song_id):
        user = current_user
        if user.id==id:
            status = delete_rating_song_by_user(id=id,song_id=song_id)
            if status is True:
                return {"message":"Rating is deleted"}, 201
            else:
                return {"message":"Rating not provided for song by user"}, 400
        else:
            return {"message":"User is not entitled to delete the rating of the song"}, 400