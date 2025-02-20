class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre = []):
        self.name = name
        self.artist = artist
        self.genre = genre

        Song.count += 1
        self.add_to_genres(genre)
        self.add_to_artists(artist)


    @classmethod
    def add_to_genres(cls,genre):
        if genre not in cls.genres:
            cls.genres.append(genre)
        cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1 # Incrementing genre count if genre already exists, else setting count to 1
        print(f"Added genre: {genre}")


    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist) # this will add artist to the list
        cls.artist_count[artist] = cls.artist_count.get(artist, 0) + 1 # Incrementing genre count if genre already exists, else setting count to 1
        print(f"Added artist: {artist}")

    def display_artists(cls):
        print("Artists:")
        for artist in cls.artists:
            print(artist)

    def display_genres(cls):
        print("Genres:")
        for artist in cls.genres:
            print(genre)


     


print(Song.count)



    
