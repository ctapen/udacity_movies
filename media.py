import webbrowser
# Create class Movie to hold movie info around title, storyline, image, trailer


class Movie():
    """ This class Movie stores info about a movie."""
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        """ This has variables about movie like title, trailer"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """ Creates capability to open trailer link via browser """
        webbrowser.open(self.trailer_youtube_url)
