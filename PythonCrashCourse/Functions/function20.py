def make_album(artist,album,no_of_tracks=''):
    album= {"artist":artist,"album":album}
    if no_of_tracks:
        album["no_of_tracks"]=no_of_tracks
    return album

while True:
    print("(Enter 'q' to exit at any time.)")
    artist = input("Enter artist name : ")
    if artist=='q':
        break
    album_name = input("Enter album name : ")
    if album_name=='q':
        break
    no_of_tracks = input("Enter number of tracks : ")
    if no_of_tracks=='q':
        break
    album = make_album(artist,album_name,no_of_tracks)
    print(album)
