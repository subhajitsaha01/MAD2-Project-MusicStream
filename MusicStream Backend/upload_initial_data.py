#---External Packages import start---
from flask_security import hash_password
from datetime import date
#---External Packages import end---

#---Internal Packages import start---
from models.models import datastore, Albums, Songs, Playlist, Album_Rating, Song_Rating
from build import app
from db.database import db
#---Internal Packages import end---

with app.app_context():
    #---Insert the roles in the roles database table---
    datastore.find_or_create_role(name="Admin", description="User is an admin")
    datastore.find_or_create_role(name="General_User", description="User is a General User")
    datastore.find_or_create_role(name="Creator", description="User is a Creator")

    #---Commit the data into the database---
    db.session.commit()

    #---Add some initial data to work in the database---
    if not datastore.find_user(email="admin@email.com"):
        datastore.create_user(username="admin",email="admin@email.com",password=hash_password("admin"),active=True,roles=["Admin"])
    if not datastore.find_user(username="user"):
        datastore.create_user(username="user",email="user@email.com",password=hash_password("user"),active=True,roles=["General_User"])
    if not datastore.find_user(email="creator@email.com"):
        datastore.create_user(username="creator",email="creator@email.com",password=hash_password("creator"),active=True,roles=["Creator"])
    
    db.session.commit()

    #---Add some initial data to work in the Albums table in the database---
    ab = Albums(album_name="Midnight Serenade", album_artist="Luna Shadows")
    ab1 = Albums(album_name="Cityscape Chronicles", album_artist="Neon Noir")
    ab2 = Albums(album_name="Lost in the Woods", album_artist="Forest Echoes")
    ab3 = Albums(album_name="Oceanic Odyssey", album_artist="Aqua Symphony")

    #---Add some songs in mapping with the albums---
    song1 = Songs(song_name="Midnight Whispers", song_lyrics="Midnight whisper", song_genre="Jazz",song_duration_mins=5.9,song_date_created=date.fromisoformat('2000-06-09'),song_link="/songs/ambient-relaxing-music-for-you-15969.mp3",album=[ab])

    song2 = Songs(song_name="CityScape Chronicles", song_lyrics="""Midnight whispers
    Said 'til early in the mornin'.
    They're gettin' louder
    Without warnin'.
    Well, soon you can't stop them.
    Those late night whispers
    Early in the mornin'.""", song_genre="Electronic",song_duration_mins=4.8,song_date_created=date.fromisoformat('1995-08-12'),song_link="/songs/random-thoughts-20586.mp3",album=[ab1])

    song3 = Songs(song_name="Starlit Dreams", song_lyrics="""Midnight whispers
    Said 'til early in the mornin'.
    They're gettin' louder
    Without warnin'.
    Well, soon you can't stop them.
    Those late night whispers
    Early in the mornin'.""", song_genre="Folk/Acoustic",song_duration_mins=4.5,song_date_created=date.fromisoformat('2001-10-08'),song_link="/songs/random-acoustic-electronic-guitar-136427.mp3",album=[ab2])

    song4 = Songs(song_name="Channa Mereya", song_lyrics="""Midnight whispers
    Said 'til early in the mornin'.
    They're gettin' louder
    Without warnin'.
    Well, soon you can't stop them.
    Those late night whispers
    Early in the mornin'.""", song_genre="Romantic",song_duration_mins=2.5,song_date_created=date.fromisoformat('2021-11-09'),song_link="/songs/morax-unlocked-hacker-mode-142916.mp3",album=[ab2])

    #---Add the data to the database table---
    db.session.add(ab)
    db.session.add(ab1)
    db.session.add(ab2)
    db.session.add(ab3)

    db.session.add(song1)
    db.session.add(song2)
    db.session.add(song3)
    db.session.add(song4)
    
    #---Add the initial data to the playlist table in the database---
    play = Playlist(playlist_name="New Playlist 1 Romantic",playlist_description="Playlist containing romantic songs",date_created=date.fromisoformat('2024-02-25'),created_by_user=1,songs=[song2, song3])
    play1 = Playlist(playlist_name="New Playlist 2 Example",playlist_description="Playlist containing example songs",date_created=date.fromisoformat('2024-03-27'),created_by_user=2,songs=[song1, song2, song3, song4])
    play2 = Playlist(playlist_name="New Playlist 3 Mythology",playlist_description="Playlist containing mythology songs",date_created=date.fromisoformat('2024-12-27'),created_by_user=3,songs=[song3, song4])
    play3 = Playlist(playlist_name="New Playlist 4 Bollywood",playlist_description="Playlist containing bollywood songs",date_created=date.fromisoformat('2024-12-01'),created_by_user=1,songs=[song1, song3, song4])
    
    #---Adding the data to the database---
    db.session.add(play)
    db.session.add(play1)
    db.session.add(play2)
    db.session.add(play3)
    
    #---Commit the data into the database---
    db.session.commit()
    
    #---Adding the data for album rating table in the database---
    rating1 = Album_Rating(album_id=1,user_id=1,rating=4)
    rating2 = Album_Rating(album_id=2,user_id=1,rating=3)
    rating3 = Album_Rating(album_id=3,user_id=1,rating=2)
    rating4 = Album_Rating(album_id=4,user_id=1,rating=5)
    rating5 = Album_Rating(album_id=2,user_id=3,rating=4)
    rating6 = Album_Rating(album_id=3,user_id=3,rating=5)
    
    #---Adding the data to the database
    db.session.add(rating1)
    db.session.add(rating2)
    db.session.add(rating3)
    db.session.add(rating4)
    db.session.add(rating5)
    db.session.add(rating6) 
    
    #---Adding the data for song rating table in the database---
    song_rating1 = Song_Rating(song_id=1,user_id=1,rating=5)
    song_rating2 = Song_Rating(song_id=2,user_id=1,rating=4)
    song_rating3 = Song_Rating(song_id=3,user_id=1,rating=2)
    song_rating4 = Song_Rating(song_id=4,user_id=1,rating=3)
    song_rating5 = Song_Rating(song_id=1,user_id=3,rating=3)
    
    #---Adding the data to the database
    db.session.add(song_rating1)
    db.session.add(song_rating2)
    db.session.add(song_rating3)
    db.session.add(song_rating4)
    db.session.add(song_rating5)
    
    #---Commit the data into the database---
    db.session.commit()
    
    