class Personne():
    def __init__(self) -> None:
        self.age = 14

    def afficherAge(self):
        print(self.age)
    
    def bonjour(self):
        print("Hello")
    
    def modifierAge(self, newAge):
        self.age = newAge
        return self.age
    
class Eleve(Personne):
    def __init__(self):
        Personne.__init__(self)

    def allerEnCours(self):
        print("Je vais en cours")

    def affichageAge(self):
        print(f"J'ai {self.age} ans")

class Professeur:
    def __init__(self, matiere_enseignee):
        self.__matiere_enseignee = matiere_enseignee

    def enseigner(self):
        print("Le cours va commencer.")


personne_0 = Personne()
eleve_0 = Eleve()

personne_0.afficherAge()
eleve_0.afficherAge()
eleve_0.modifierAge(17)
eleve_0.affichageAge()