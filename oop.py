class Emobilisstudent:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def hello_me(self):
        print(f"My name is {self.name} and im {self.age} years old")
#creating an object
myobj=Emobilisstudent("Mount Mason",39)
myobj.hello_me()

myobj=Emobilisstudent("Alex Wales",80)
myobj.hello_me()

myobj=Emobilisstudent("Alison Kay",20)
myobj.hello_me()

#create a class for magari, it shld have mode,make,year propeterties
#min of 3 objects

class Magari:
    def __init__(self, name, mode, make, color):
        self.name=name
        self.mode=mode
        self.make=make
        self.color=color
    def hello_me(self):
        print(f"Car name {self.name} and the is engine {self.mode} make {self.make} ,it is color {self.color}")


myobj=Magari("Toyota pagero","V12", 2030, "White")
myobj.hello_me()

myobj=Magari("G wagen","V12", 2030, "Black")
myobj.hello_me()

#assignment
class KenyanArtist:
    def __init__(self, Aname, NoOfSongs, TypeOfSongs):
        self.Aname=Aname
        self.NoOfSongs=NoOfSongs
        self.TypeOfSongs=TypeOfSongs
    def hello_me(self):
        print(f"Today's artist is {self.Aname} and he has  {self.NoOfSongs} songs. he sings {self.TypeOfSongs}")

myobj=KenyanArtist("Khaligraph Jones", 56,"Trap music")
myobj.hello_me()