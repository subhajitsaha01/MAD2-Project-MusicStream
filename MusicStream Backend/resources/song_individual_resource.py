#---External Packages import start---
from flask_restful import Resource,reqparse, fields
from flask import request, jsonify
from flask_security import auth_required, roles_accepted
from datetime import date
#---External Packages import end---

#---Internal Packages import start---
from utilities.song_utilities import view_song_by_its_id,update_song_by_its_id, delete_song_by_its_id
from utilities.token_expiration import check_token_expiration
#---Internal Packages import end---

#---Configure the Request Parser---
parser = reqparse.RequestParser()
parser.add_argument('name', type=str, help='Name of the song is required and should be a string')
parser.add_argument('lyrics', type=str, help='Lyrics of the song is required and should be a string')
parser.add_argument('genre', type=str, help='Genre of the song is required and should be a string')
parser.add_argument('duration_mins', type=float, help='Duration of the song is required and should be float')
parser.add_argument('date', type=str, help='Date of the song is required and should be string')
parser.add_argument('album_id',type=int, help='Album id of the song is required and should be integer')

#---Configure the album data output in a relevant manner---
album_data_fields = {
    "id":fields.Integer,
    "name":fields.String,
    "lyrics":fields.String,
    "genre":fields.String,
    "duration_mins":fields.Float,
    "date":fields.DateTime
}

#---API to perform the CRUD operations on Individual Song data---
class SongsIndividualApi(Resource):
    #---To get the data about an individual song using the song id---
    @auth_required("token")
    @roles_accepted("Admin","General_User","Creator")
    @check_token_expiration
    def get(self,id):
        song = view_song_by_its_id(id)
        if song is None:
            return {"message":"No song is present for this song id"}, 400
        else:
            return song, 201
    def post(self):
        pass
    #---To update the data of an individual song---
    @auth_required("token")
    @roles_accepted("Admin","Creator")
    @check_token_expiration
    def put(self,id):
        #---Parsing the request arguments---
        args = parser.parse_args()
        data = request.get_json()

        #---Extracting the request parameters---
        song_name = data.get('name')
        song_lyrics = data.get('lyrics')
        song_genre = data.get('genre')
        song_duration_mins = data.get('duration_mins')
        song_date_created = data.get('date')
        album_id = data.get('album_id')

        #---matching it with the relevant conditions---
        result = update_song_by_its_id(id,song_name=song_name,song_lyrics=song_lyrics,song_genre=song_genre,song_duration_mins=song_duration_mins,song_date_created=song_date_created,album_id=album_id)
        if result is None:
            return {"message":"Song is not present with the id"}, 400
        else:
            return {"message":"Song data is updated"}, 201
    #---Deleting the song based on the id---
    @auth_required("token")
    @roles_accepted("Admin","Creator")
    @check_token_expiration
    def delete(self,id):
        delete_song_by_its_id(id)
        return {"message":"Song is deleted"}, 201