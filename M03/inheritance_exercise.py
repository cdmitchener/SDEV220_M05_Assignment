class Pets():
    animals = []

    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Schrodinger(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Garfield(Cat):
    def sing(self, sounds):
        return f'{sounds}'

#1 Add another Cat
class Tom(Cat):
    def sing(self, sounds):
        return f'{sounds}'

#2 Create a list of all of the pets (create 3 cat instances from the above)
my_cats = [Schrodinger('Schrodinger', 8), Garfield('Garfield', 15), Tom('Tom', 4)]

#3 Instantiate the Pet class with all your cats use variable my_pets
my_pets = Pets(my_cats)

#4 Output all of the cats singing using the my_pets instance
my_pets.walk()