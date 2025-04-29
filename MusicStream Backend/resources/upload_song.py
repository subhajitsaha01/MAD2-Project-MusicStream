#---External Packages import start---
from flask_restful import Resource,request,reqparse
from flask import request, jsonify, send_file
from flask_security import auth_required, roles_accepted
from datetime import date
#---External Packages import end---

#---Internal Packages import start---
from utilities.song_utilities import update_song_link_by_name
from utilities.token_expiration import check_token_expiration
#---Internal Packages import end---

#---Configure the Request Parser---
parser = reqparse.RequestParser()
parser.add_argument('name', type=str, help='Name of the song is required and should be a string', required=True)

#---API to perform the Listen operations on Individual Song data---
class SongsUploadApi(Resource):
    def get(self):
        pass
    @auth_required("token")
    @roles_accepted("Admin","Creator")
    @check_token_expiration
    def post(self):
        if request.method=='POST':
            
            #---Parsing the request arguments---
            args = parser.parse_args()
            data = request.get_json()

            #---Extracting the request parameters---
            song_name = data.get("name")
                
            try:
                f = request.files("audioFile")
                print(f.filename)
                f.save('songs/'+f.filename)
                update_song_link_by_name(song_name,f.filename)
                return {"message":"Song File Uploaded Successfully"}, 201
            except Exception as e:
                print(e)
                return {"message":"Error in uploading audio file"}, 400
    def put(self,id):
        pass
    def delete(self,id):
        pass