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
