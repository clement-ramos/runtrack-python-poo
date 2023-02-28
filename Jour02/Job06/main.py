class Commande():
    def __init__(self,nb_cmd, liste_plat, statut):
        self.__nb_cmd = nb_cmd
        self.__liste_plat = liste_plat
        self.__statut = statut
    def ajout_plat(self, new_plat):
        self.__liste_plat.append(new_plat)
    def annule(self):
        self.__statut = "Annuler"
    