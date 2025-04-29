#   Python File for running the final application

#---External Packages import start---
from flask import Flask,request
from flask_security import auth_required, roles_accepted
#---External Packages import end---

#---Internal Packages import start---
from db.database import db
from build import app
from utilities.song_utilities import update_song_link_by_name
from utilities.token_expiration import check_token_expiration
#---Internal Packages import end---

@auth_required("token")
@roles_accepted("Admin","Creator")
@check_token_expiration
@app.route('/music_stream/api/upload/song',methods=['POST'])
def upload_audio():
    if request.method=='POST':
        name = request.form['name']
        print(name)        
        try:
            f = request.files["audioFile"]
            print(f.filename)
            f.save('songs/'+f.filename)
            update_song_link_by_name(name,f.filename)
            return {"message":"Song File Uploaded Successfully"}, 201
        except Exception as e:
            print(e)
            return {"message":"Error in uploading audio file"}, 400

#   Running the application inside the main method
if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0')