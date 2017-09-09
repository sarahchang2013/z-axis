import webbrowser


class Movie():
    """This is a class of movies with titles, posters and trailers"""

    # Initialize the object with given variables.
    def __init__(self, movie_title, poster_image, trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
