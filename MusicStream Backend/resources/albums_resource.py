#---External Packages import start---
from flask_restful import Resource,reqparse, fields
from flask import request, jsonify
from flask_security import auth_required, roles_accepted
#---External Packages import end---

#---Internal Packages import start---
from utilities.album_utilities import album_name_exists, insert_album, view_albums
from utilities.token_expiration import check_token_expiration
#---Internal Packages import end---

#---Configure the Request Parser---
parser = reqparse.RequestParser()
parser.add_argument('name', type=str, help='Name of the album is required and should be a string', required=True)
parser.add_argument('artist', type=str, help='Artist of the album is required and should be a string', required=True)

#---Configure the album data output in a relevant manner---
album_data_fields = {
    "id":fields.Integer,
    "album_name":fields.String,
    "album_artist":fields.String,
    "album_songs":fields.List
}

#---API to perform the CRUD operations using albums---
class AlbumsApi(Resource):
    #---for getting the list of albums---
    @auth_required("token")
    @roles_accepted("Admin","General_User","Creator")
    @check_token_expiration
    def get(self):
        albums = view_albums()
        if albums is None:
            return {"message":"No albums present in the database"}, 201
        else:
            return {"albums":albums}, 201
    #---for inserting the data into the Album table of the database---
    @auth_required("token")
    @roles_accepted("Admin","Creator")
    @check_token_expiration
    def post(self):
        #---Parsing the request arguments---
        args = parser.parse_args()
        data = request.get_json()

        #---Extracting the request parameters---
        album_name = data.get("name")
        album_artist = data.get("artist")

        #---matching it with relevant conditions---
        if not album_name and not album_artist:
            return {"message":"Album name and artist not provided"}, 400
        if not album_name:
            return {"message":"Album name not provided"}, 400
        if not album_artist:
            return {"message":"Album artist not provided"}, 400
        if album_name_exists(album_name):
            return {"message":"Album name exists in the database"}, 400
        else:
            insert_album(album_name, album_artist)
            return {"message":"Album is created"}, 201
    def put(self):
        pass
    def delete(self):
        pass