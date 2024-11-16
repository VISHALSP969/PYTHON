def make_album(artist,album,no_of_tracks=''):
    album= {"artist":artist,"album":album}
    if no_of_tracks:
        album["no_of_tracks"]=no_of_tracks
    return album

album=make_album("Kj Yeshudas","Azhakiyaravanan",3)
print(album)
album=make_album("AR Rahman","Roja")
print(album)