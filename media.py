import webbrowser

class TrailerInfo():
    
    def __init__(self, trailer_title, trailer_image, trailer_youtube):
        self.title = trailer_title
        self.poster_image_url = trailer_image
        self.trailer_youtube_url = trailer_youtube

class Movie(TrailerInfo):

    def __init__(self,trailer_title, trailer_image, trailer_youtube):
        TrailerInfo.__init__(self, trailer_title, trailer_image, trailer_youtube)

class Games(TrailerInfo):
   
    def __init__(self,trailer_title, trailer_image, trailer_youtube):
        TrailerInfo.__init__(self, trailer_title, trailer_image, trailer_youtube)
