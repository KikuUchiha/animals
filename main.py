import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self, host, user, password, database, use_pure=True, ssl_disabled=True):
        try:
            self.connection = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database,
                use_pure=use_pure,
                ssl_disabled=ssl_disabled
            )
            self.cursor = self.connection.cursor()
        except Error as e:
            print(f"Error: {e}")
            self.connection = None
            self.cursor = None

    def execute_query(self, query, params=None):
        if self.connection and self.cursor:
            self.cursor.execute(query, params or ())
            self.connection.commit()

    def fetch_all(self, query, params=None):
        if self.connection and self.cursor:
            self.cursor.execute(query, params or ())
            return self.cursor.fetchall()
        return []

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

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
        
    def add_commands(self, new_commands):
        self.commands += ', ' + new_commands

class PackAnimal(Animal):
    def __init__(self, name, birthdate, load_capacity):
        super().__init__(name, birthdate)
        self.load_capacity = load_capacity
        
class Registry:
    def __init__(self, db):
        self.db = db
        self.animals = []

    def load_animals(self):
        # Загрузка домашних животных
        pet_query = "SELECT имя, команды, дата_рождения FROM Домашние_Животные"
        pets = self.db.fetch_all(pet_query)
        for pet in pets:
            self.animals.append(Pet(name=pet[0], birthdate=pet[2], commands=pet[1]))
        
        # Загрузка вьючных животных
        pack_animal_query = "SELECT имя, дата_рождения FROM Вьючные_Животные"
        pack_animals = self.db.fetch_all(pack_animal_query)
        for pack_animal in pack_animals:
            self.animals.append(PackAnimal(name=pack_animal[0], birthdate=pack_animal[1], load_capacity=None))

    def add_animal(self, animal):
        self.animals.append(animal)
        if isinstance(animal, Pet):
            query = "INSERT INTO Домашние_Животные (имя, команды, дата_рождения) VALUES (%s, %s, %s)"
            self.db.execute_query(query, (animal.name, animal.commands, animal.birthdate))
        elif isinstance(animal, PackAnimal):
            query = "INSERT INTO Вьючные_Животные (имя, дата_рождения) VALUES (%s, %s)"
            self.db.execute_query(query, (animal.name, animal.birthdate))

    def show_commands(self, animal_name):
        for animal in self.animals:
            if isinstance(animal, Pet) and animal.name == animal_name:
                print(animal.commands)
                return
        print("Animal not found or not a Pet")

