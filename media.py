class Movie():
    """Initializes the Movie class to display relevant content
        title: takes in string for the title of the movie
        storyline: takes in string for storyline of the movie
        poster: takes in a string to the url of the movie poster image
        trailer_url: takes in a string to the url of the Youtube trailer link of the movie
    """

    def __init__(self, title, storyline, poster, trailer_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer_url
