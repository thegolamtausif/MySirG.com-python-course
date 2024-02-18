class a:
    def __init__(self,name):
        self.name=name
    def talk(self):
        raise NotImplementedError
class cat(a):
    def talk(self):
        return "meow"
class dog(a):
    def talk(self):
        return "woof" 
animals=[cat("rekha"),dog("moti")]
for animal in animals:
    print(animal.name," - ",animal.talk())

