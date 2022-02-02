from dis import dis


class UserProfile:
    __likes = []
    __dislikes = []
    
    def __init__(self, likes=[], dislikes=[]):
        self.__likes = likes
        self.__dislikes = dislikes

    @property
    def likes(self):
        return self.__likes

    @property
    def dislikes(self):
        return self.__dislikes

    @likes.setter
    def likes(self, likes = []):
        likes = [i for i in likes if i not in self.likes]
        self.likes.extend(likes)

    @dislikes.setter
    def dislikes(self, dislikes = []):
        dislikes = [i for i in dislikes if i not in self.dislikes]
        self.dislikes.extend(dislikes)