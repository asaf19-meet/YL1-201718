##class Animal(object):
##    def __init__(self,sound,name,age,favority_color):
##        self.sound = sound
##        self.name = name
##        self.age = age
##        self.favority_color = favority_color
##    def eat(self,food):
##        print("Yummy!! " + self.name + " is eating " + food)
##    def description(self):
##        print(self.name + " is " + str(self.age) + " years old and loves the color " + self.favority_color)
##    def make_sound(self,times):
##        print((self.sound+ " " )*times)
##dog = Animal("wof","roxy",5,"green")
##dog.eat("ice cream")
##dog.description()
##dog.make_sound(76)
class Person(object):
    def __init__(self,name,age,city,gender,fav_breakfast,fav_song):
        self.name = name
        self.age = age
        self.city = city
        self.gender = gender
        self.fav_breakfast = fav_breakfast
        self.fav_song = fav_song
    def eatBF(self):
        print(self.name + " is eating his favorit breakfast - " + self.fav_breakfast)
    def song(self):
        print("Almog's favorit song is " + self.fav_song)
Almog = Person("Almog",33,"tivon","male","hamburger","chagaroon macaroon")
Almog.eatBF()
Almog.song()
class song(object):
    def __init__(self,lyrics):
        self.lyrics=lyrics
    def sing_me_a_song(self):
        for i in self.lyrics:
            print(i)
flower_song = song(["bla","bal","lab"])
flower_song.sing_me_a_song()

    
    


