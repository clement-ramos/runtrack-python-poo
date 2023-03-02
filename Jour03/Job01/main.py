class Ville():
    def __init__(self, nom,nb_habits) -> None:
        self.__nom = nom
        self.__nb_habits = nb_habits

    def add_new_habits(self, number):
        self.__nb_habits += number
        return self.__nb_habits

    def get_nb_habits(self):
        return self.__nb_habits
    
class Personne():
    def __init__(self,nom,age,ville) -> None:
        self.__nom = nom
        self.__age = age
        self.__ville = ville 
        self.ajouterPopuation()

    def ajouterPopuation(self):
        self.__ville.add_new_habits(1)


ville_paris = Ville("Paris", 1_000_000)
ville_marseille = Ville("Marseille", 861_635)

print(f"Population de la ville de Paris : {ville_paris.get_nb_habits()} habitants")
print(f"Population de la ville de Marseille : {ville_marseille.get_nb_habits()} habitants")

personne_00 = Personne("John", 45, ville_paris)
personne_01 = Personne("Myrtille", 4, ville_paris)
personne_02 = Personne("Chloé", 18, ville_marseille)

print(f"La nouvelle population de la ville de Paris : {ville_paris.get_nb_habits()}habitants")
print(f"La nouvelle population de la ville de Marseille : {ville_marseille.get_nb_habits()} habitants")