def make_album(artist_name,album_title, tracks=''):
    """ Builds a dictionary describing a music album. """
    album = { 'artist' : artist_name , 'album' : album_title}
    if tracks:
        album['tracks'] = tracks
    return album
while True:
    print("\n Please tell me an artist and album name: ")
    print("(enter 'q' at any time to quit)")

    art_name = input("Artist name: ")
    if art_name == 'q':
        break

    alb_name = input("Album name: ")
    if alb_name == 'q':
        break

    formatted_name = make_album(art_name,alb_name)
    print(formatted_name)
    

album1 = make_album('beach boys','pet sounds', tracks=14)
album2 = make_album('jim hendrix' ,'electric ladyland')
#print(album1)
#print(album2)
