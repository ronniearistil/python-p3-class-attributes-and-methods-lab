class Song:
    # Class attributes
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        # Initialize instance attributes
        self.name = name
        self.artist = artist
        self.genre = genre

        # Update class attributes
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        """Increment the total song count."""
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        """Add genre to the genres list if not already present."""
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        """Add artist to the artists list if not already present."""
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        """Increment the count of songs for a given genre."""
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        """Increment the count of songs for a given artist."""
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

# Test the Song class
if __name__ == "__main__":
    # Create song instances
    song1 = Song("99 Problems", "Jay-Z", "Rap")
    song2 = Song("Halo", "Beyonce", "Pop")
    song3 = Song("God's Plan", "Drake", "Rap")

    # Check class attribute values
    print(Song.count)  # Output: 3
    print(Song.genres)  # Output: ['Rap', 'Pop']
    print(Song.artists)  # Output: ['Jay-Z', 'Beyonce', 'Drake']
    print(Song.genre_count)  # Output: {'Rap': 2, 'Pop': 1}
    print(Song.artist_count)  # Output: {'Jay-Z': 1, 'Beyonce': 1, 'Drake': 1}

