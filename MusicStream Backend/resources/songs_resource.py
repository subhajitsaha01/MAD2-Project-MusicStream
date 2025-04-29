#---External Packages import start---
from flask_restful import Resource,reqparse, fields
from flask import request, jsonify
from flask_security import auth_required, roles_accepted
from datetime import date
#---External Packages import end---

#---Internal Packages import start---
from utilities.song_utilities import view_songs, insert_song
from utilities.token_expiration import check_token_expiration
#---Internal Packages import end---

#---Configure the Request Parser---
parser = reqparse.RequestParser()
parser.add_argument('name', type=str, help='Name of the song is required and should be a string', required=True)
parser.add_argument('lyrics', type=str, help='Lyrics of the song is required and should be a string')
parser.add_argument('genre', type=str, help='Genre of the song is required and should be a string')
parser.add_argument('duration_mins', type=float, help='Duration of the song is required and should be float', required=True)
parser.add_argument('date', type=str, help='Date of the song is required and should be string', required=True)
parser.add_argument('album_id',type=int, help='Album id of the song is required and should be integer', required=True)

#---Configure the album data output in a relevant manner---
album_data_fields = {
    "id":fields.Integer,
    "name":fields.String,
    "lyrics":fields.String,
    "genre":fields.String,
    "duration_mins":fields.Float,
    "date":fields.DateTime
}

#---API to perform the CRUD operations using songs---
class SongsApi(Resource):
    #---Get the list of songs currently present for a database---
    @auth_required("token")
    @roles_accepted("Admin","General_User","Creator")
    @check_token_expiration
    def get(self):
        songs = view_songs()
        if songs is None:
            return {"message":"No songs present in the database"}, 201
        else:
            return {'songs':songs}, 201
    #---To add the song to the database---
    @auth_required("token")
    @roles_accepted("Admin","Creator")
    @check_token_expiration
    def post(self):
        #---Parsing the request arguments---
        args = parser.parse_args()
        data = request.get_json()

        #---Extracting the request parameters---
        song_name = data.get("name")
        song_lyrics = data.get("lyrics")
        song_genre = data.get("genre")
        song_duration_mins = data.get("duration_mins")
        song_date_created = date.fromisoformat(data.get("date"))
        album_id = data.get("album_id")

        #---matching it with relevant conditions---
        if not song_name and not song_duration_mins and not song_date_created:
            return {"message":"Song name, duration and date created not provided"}, 400
        if not song_name:
            return {"message":"Song name not provided"}, 400
        if not song_duration_mins:
            return {"message":"Song duration in minutes not provided"}, 400
        if not song_date_created:
            return {"message":"Song date created not provided"}, 400
        if not album_id:
            return {"message":"Album id for this song not provided"}, 400
        else:
            insert_song(song_name, song_lyrics, song_genre, song_duration_mins, song_date_created, album_id)
            return {"message":"Song is created"}, 201
    def put(self):
        pass
    def delete(self):
        pass