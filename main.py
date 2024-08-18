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
