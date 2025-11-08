print("********#########")
class Cat:
    def sound(self):
        return "meow"
class Dog:
     def sound(self):
        return "bark"
     
for animal in (Cat(),Dog()):
    print(animal.sound())