class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        print("Je suis " + self.prenom + " " + self.nom)


personne1 = Personne("John", "Doe")
personne2 = Personne("Jean", "Dupont")

personne1.SePresenter()
personne2.SePresenter()