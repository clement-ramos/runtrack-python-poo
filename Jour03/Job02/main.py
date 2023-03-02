class CompteBancaire():
    def __init__(self, numero_de_compte, nom, prenom, solde, decouvert) -> None:
        self.__numero_de_compte = numero_de_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.decouvert = decouvert

    def afficher(self):
        print(f"numero de compte {self.__numero_de_compte}")
        print(f"nom {self.__nom}")
        print(f"prenom {self.__prenom}")
        print(f"solde {self.__solde}")

    def afficherSolde(self):
        print(f"solde {self.__solde} de {self.__prenom}")

    def versement(self, montant, client):
        if self.__solde > montant:
            self.__solde -= montant
            client.__solde += montant
  
    def retrait(self, montant):
        if self.decouvert:
            self.__solde -= montant
        elif self.__solde > montant:
            self.__solde -= montant
        else:
            print("Vous n'avez pas les fonds necessaire et ne pouvait pas etre a decouvert")
            self.afficherSolde()

compte_0 = CompteBancaire("708001", "RAMOS", "Clement", 200, False)
compte_1 = CompteBancaire("708002", "RAMOS", "Jean", 360, True)

compte_0.afficher()
compte_1.afficher()

compte_0.versement(233,compte_1)
compte_0.retrait(493)
compte_1.retrait(493)
compte_0.afficherSolde()
compte_1.afficherSolde()

compte_0.versement(333,compte_1)
compte_0.afficherSolde()
compte_1.afficherSolde()