import json

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        print(f'{self.name} is eating.')

class Bird(Animal):
    def make_sound(self):
        print(f'{self.name} is singing.')

class Mammal(Animal):
    def make_sound(self):
        print(f'{self.name} is murmuring.')

class Reptile(Animal):
    def make_sound(self):
        print(f'{self.name} is hissing.')

class ZooKeeper:
    def feed_animal(self, animal):
        print(f'ZooKeeper is feeding {animal.name}.')

class Veterinarian:
    def heal_animal(self, animal):
        print(f'Veterinarian is healing {animal.name}.')

class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_staff(self, employee):
        self.staff.append(employee)

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            zoo_data = {'animals': [(type(a).__name__, a.name, a.age) for a in self.animals],
                        'staff': [(type(s).__name__, s.name) for s in self.staff]}
            json.dump(zoo_data, file)

    def load_from_file(self, filename):
        with open(filename, 'r') as file:
            zoo_data = json.load(file)
            # Восстановление информации о животных и сотрудниках требует дополнительной логики


# Создание экземпляров сотрудников и животных
zookeeper = ZooKeeper()
vet = Veterinarian()

parrot = Bird('Parrot', 5)
cat = Mammal('Cat', 3)
snake = Reptile('Snake', 4)

# Создание зоопарка и добавление в него информации
zoo = Zoo()
zoo.add_staff(zookeeper)
zoo.add_staff(vet)
zoo.add_animal(parrot)
zoo.add_animal(cat)
zoo.add_animal(snake)

# Сохранение информации о зоопарке в файл
zoo.save_to_file('zoo_data.json')

# Загрузка информации о зоопарке из файла
zoo.load_from_file('zoo_data.json')