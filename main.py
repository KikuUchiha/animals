class Animal:
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate
        
    def make_sound(self):
        pass
        
class Pet(Animal):
    def __init__(self, name, birthdate, commands):
        super().__init__(name, birthdate)
        self.commands = commands
        
class PackAnimal(Animal):
    def __init__(self, name, birthdate, load_capacity):
        super().__init__(name, birthdate)
        self.load_capacity = load_capacity
        
class Registry:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def show_commands(self, animal_name):
        for animal in self.animals:
            if isinstance(animal, Pet) and animal.name == animal_name:
                print(animal.commands)
                return
        print("Animal not found or not a Pet")

