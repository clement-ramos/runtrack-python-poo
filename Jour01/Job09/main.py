# Créer la classe “Produit” avec des attributs “nom”, “prixHT”, “TVA”. Implémenter la
# méthode “CalculerPrixTTC” qui retourne le prix produit avec la TVA. Ajouter la méthode
# “afficher” qui liste l’ensemble des informations du produit.
# Créer plusieurs produits et calculer leurs TVA.
# Ajouter des méthodes permettant de modifier le nom du produit et son prix. Ainsi que
# des méthodes permettant retourner chaque information du produit.
# Modifier le nom et le prix de chaque produit et afficher en console le nouveau prix des
# produits.
# La fonction print ne doit être utilisé dans la classe “Produit”.

class Produit():
    def __init__(self, name, prixHT, TVA) -> None:
        self.nom = name
        self.prixHT = prixHT
        self.TVA = TVA
        

    def CalculerPrixTTC(self):
        return (self.prixHT + self.prixHT * self.TVA)
    
    def afficher(self):
        print(self.nom, self.prixHT, self.TVA)

    def change_name_price(self,name,price):
        self.nom = name
        self.prixHT = price

switch = Produit("switch", 300, 0.2)
switch.afficher()
print(switch.CalculerPrixTTC())

switch.change_name_price("Ordinateur", 1000)
switch.afficher()
print(switch.CalculerPrixTTC())


