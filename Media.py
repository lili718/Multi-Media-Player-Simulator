#Lia Johnson CS 172 Spring 2019
#ID: lej42
#Purpose: the Media parent class and the song, picture and movie classes of type media
#Date: May 2, 2019

class Media():
    def __init__(self, name, mtype, rating):
        self.__name = name
        self.__rating = str(rating)
        self.__mtype = mtype
    
    def getType(self):
        return self.__mtype
    
    def getName(self):
       return self.__name
    
    def getRating(self):
        return self.__rating
    
    def __str__(self):
        myStr = "This is \"" + self.getName() + "\" it is a " + self.getType() + " with a rating of " + self.getRating() + "."
        return myStr

class Movie(Media):
    ext =".mp4"
    def __init__(self, name, rating, director, rtime):
        super().__init__(name, "Movie" , rating)
        self.__director = director
        self.__rtime = rtime
        
    def getDirector(self):
        return self.__director
    
    def getRuntime(self):
        return self.__rtime

    def play(self):
        print(super().getName() + ", playing now\n")
        
    def __str__(self):
        myStr = super().__str__() + " This movie was directed by " + self.getDirector() + " and has a runtime of " + self.getRuntime() + "."
        return myStr

class Song(Media):
    ext = ".mp3"
    def __init__(self, name, rating, artist, album):
        super().__init__(name, "Song", rating)
        self.__artist = artist
        self.__album = album
        
    def getArtist(self):
        return self.__artist
    
    def getAlbum(self):
        return self.__album
    
    def play(self):
        print(super().getName() + " by " + self.getArtist() + ", playing now.")
        
    def __str__(self):
        myStr = super().__str__() + " It is by " + self.getArtist() + " from their album: " + self.getAlbum() + "."
        return myStr

class Picture(Media):
    ext = ".jpg"
    def __init__(self, name, rating, reso):
        super().__init__(name, "Picture", rating)
        self.__reso = reso
    
    def getReso(self):
        return self.__reso
    
    def show(self):
        print("Showing", super().getName() + Picture.ext)
        
    def __str__(self):
        myStr = super().__str__() + " Its resolution is " + self.getReso() + "."
        return myStr
    