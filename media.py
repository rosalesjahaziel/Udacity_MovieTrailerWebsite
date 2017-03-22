import webbrowser


class TrailerInfo():
    "This is the parent clase how content the basic infomation for a video"

    def __init__(self, trailer_title, trailer_image, trailer_youtube):
        "an isinstance have title, img poster and url youtube video"
        self.title = trailer_title
        self.poster_image_url = trailer_image
        self.trailer_youtube_url = trailer_youtube


class Movie(TrailerInfo):
    "Init class using parent TrailerInfo Class"
    def __init__(self, trailer_title, trailer_image, trailer_youtube):
        TrailerInfo.__init__(self, trailer_title,
                            trailer_image, trailer_youtube)


class Games(TrailerInfo):
    "Init class using parent TrailerInfo Class"
    def __init__(self, trailer_title, trailer_image, trailer_youtube):
        TrailerInfo.__init__(self, trailer_title,
                            trailer_image, trailer_youtube)
