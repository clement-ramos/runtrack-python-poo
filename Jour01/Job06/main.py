class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def print_age(self):
        print("L'age de l'animal " + str(self.age) + " ans")

    def viellir(self):
        self.age += 1

    def nommer(self, name):
        self.prenom = name
        print("L'animal se nomme " + self.prenom)

animal = Animal()

animal.print_age()
animal.viellir()
animal.print_age()
animal.nommer("Luna")