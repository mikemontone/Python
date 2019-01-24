#!/opt/bb/bin/python3.6
def make_album(artist_name,album_title, tracks=''):
   """ Builds a dictionary describing a music album. """
   album = { 'artist' : artist_name , 'album' : album_title}
   if tracks:
       album['tracks'] = tracks
   return album

#album1 = make_album('beach boys','pet sounds', tracks=14)
#album2 = make_album('jim hendrix' ,'electric ladyland')
#print(album1)
#print(album2)

while True:
    print("\n Please tell my the artist's name:")
    print("(enter 'q' at any time to quit)")

    artist_name = input("Artist name: ")
    if artist_name == 'q':
        break
    album_title = input("Album title: ")
    if album_title == 'q':
        break
    made_album = make_album(artist_name,album_title)
    print(made_album)

