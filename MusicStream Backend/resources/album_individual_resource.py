#---External Packages import start---
from flask_restful import Resource,reqparse, fields, marshal
from flask import request, jsonify
from flask_security import auth_required, roles_accepted
#---External Packages import end---

#---Internal Packages import start---
from utilities.album_utilities import  view_album_by_id,update_album_data,delete_album_by_its_id
from utilities.token_expiration import check_token_expiration
#---Internal Packages import end---

#---Configure the Request Parser---
parser = reqparse.RequestParser()
parser.add_argument('name', type=str, help='Name of the album is required and should be a string', required=True)
parser.add_argument('artist', type=str, help='Artist of the album is required and should be a string', required=True)


#---API to perform the CRUD operations using albums---
class AlbumIndividualApi(Resource):
    #---For getting the album with the specific album_id---
    @auth_required("token")
    @roles_accepted("Admin","General_User","Creator")
    @check_token_expiration
    def get(self,id):
        album = view_album_by_id(id)
        if album is None:
            return {"message":"No albums present with the specific id"}, 400
        else:
            return album, 201
    def post(self):
        pass
    #---For updating the album details with the specific album_id---
    @auth_required("token")
    @roles_accepted("Admin","Creator")
    @check_token_expiration
    def put(self,id):
        #---Parsing the request arguments---
        args = parser.parse_args()
        data = request.get_json()

        #---Extracting the request parameters---
        album_name = data.get("name")
        album_artist = data.get("artist")

        #---matching it with the relevant conditions---
        if album_name and album_artist:
            update_album_data(id,album_name=album_name,album_artist=album_artist)
            return {"message":"Album name and artist are updated"}, 201
        elif album_name:
            update_album_data(id,album_name=album_name)
            return {"message":"Album name is updated"}, 201
        elif album_artist:
            update_album_data(id,album_artist=album_artist)
            return {"message":"Album artist is updated"}, 201
    #---For deleting the album with the specific album_id---
    @auth_required("token")
    @roles_accepted("Admin","Creator")
    @check_token_expiration
    def delete(self,id):
        delete_album_by_its_id(id)
        return {"message":"Album data is deleted"}, 201