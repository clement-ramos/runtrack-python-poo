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

class Professeur(Personne):
    def __init__(self, matiere_enseignee):
        self.__matiere_enseignee = matiere_enseignee


    def enseigner(self):
        print("Le cours va commencer")

professeur_0 = Professeur("SVT")
eleve_0 = Eleve()

eleve_0.bonjour()
eleve_0.allerEnCours()
eleve_0.modifierAge(15)
eleve_0.affichageAge()

professeur_0.modifierAge(40)
professeur_0.bonjour()
professeur_0.enseigner()
