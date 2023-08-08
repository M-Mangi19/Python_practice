class Pet():
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.energy = 100
        self.health = 25


    def sleep(self):
        self.energy = self.energy + 25
        return self

    def eat(self):
        self.energy = self.energy + 5
        self.health = self.health + 10
        return self

    def play(self):
        self.health = self.health + 5
        self.energy = self.energy - 15
        print(f"Ripley did a {self.tricks}")
        return self

    def noise(self):
        print("Meeeoooooowwwww")
        return self

    def cat_health(self):
        print(f"Ripley's energy level is: {self.energy}")
        print(f"Ripley's health level is: {self.health}")
        return self


class Ninja():
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        self.pet.play()
        return self


    def feed(self):
        self.pet.eat()
        return self

    def bathe(self):
        self.pet.noise()
        return self




ripley = Pet("Ripley", "cat", "back-flip")

matt = Ninja("Matt", "Mangiaracina", "cat-nip", "chicken", ripley)

matt.walk().feed().bathe()
ripley.cat_health()

