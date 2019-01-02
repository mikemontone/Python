{'artist': 'beach boys', 'album': 'pet sounds', 'tracks': 14}
{'artist': 'jim hendrix', 'album': 'electric ladyland'}
op - sundev41 $ cat make_album.py
def make_album(artist_name,album_title, tracks=''):
    """ Builds a dictionary describing a music album. """
    album = { 'artist' : artist_name , 'album' : album_title}
    if tracks:
        album['tracks'] = tracks
    return album

album1 = make_album('beach boys','pet sounds', tracks=14)
album2 = make_album('jim hendrix' ,'electric ladyland')
print(album1)
print(album2)
