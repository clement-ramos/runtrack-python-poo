class Livre():
    def __init__(self, titre, auteur, pages) -> None:
        self.__titre = titre
        self.__auteur = auteur
        self.__pages = pages
        self.__disponible = True

    def get(self):
        return self.__titre, self.__auteur, self.__pages
    
    def set(self, titre, auteur, pages):
        self.__titre = titre
        self.__auteur = auteur
        if pages > 0:
            self.__pages = pages
        else:
            print("Un nombre de pages négatif est impossible")

livre1 = Livre("harry_potter", "JK", 430)

print(livre1.get())
livre1.set("harry_potter_2", "JK", 230)
print(livre1.get())
livre1.set("harry_potter_2", "JK", -230)
print(livre1.get())