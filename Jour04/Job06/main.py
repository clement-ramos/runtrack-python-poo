class Vehicule:
    def __init__(self, marque, annee, prix, modele):
        self.marque = marque
        self.annee = annee
        self.prix = prix
        self.modele = modele

    def informationsVehicule(self):
        print(f"\nInformations véhicule:\nMarque: {self.marque}\nModèle: {self.modele}\nAnnée: {self.annee}\nPrix: {self.prix} euros")
        
    def demarrer(self):
        print("Attention, je roule .")


class Voiture(Vehicule):
    def __init__(self, marque, annee, prix, modele):
        Vehicule.__init__(self, marque, annee, prix, modele)
        self.nb_portes = 4

    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de portes: {self.nb_portes}")

    def demarrer(self):
        print("Attention je roule en Voiture")

class Moto(Vehicule):
    def __init__(self, marque, annee, prix, modele):
        Vehicule.__init__(self, marque, annee, prix, modele)
        self.nb_roues = 2

    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de roues: {self.nb_roues}")

    def demarrer(self):
        print("Attention je roule en Moto")

voiture_0 = Voiture("Audi", 2018, 20000, "A1")
moto_0 = Moto("Yamaha", 2020, 12000, "MT-07")

voiture_0.informationsVehicule()
voiture_0.demarrer()

moto_0.informationsVehicule()
moto_0.demarrer()