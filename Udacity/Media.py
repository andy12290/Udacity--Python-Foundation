import webbrowser

class Movie():
    """ This is movie class to show you the trailer and story."""

    VALID_RATING = ['G', 'PG', 'CC']
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
