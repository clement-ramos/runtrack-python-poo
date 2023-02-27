import math

class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def changerRayon(self, new_rayon):
        self.rayon = new_rayon
    
    def circonference(self):
        print(2 * math.pi * self.rayon)

    def aire(self):
        print(math.pi * self.rayon * self.rayon)

    def diametre(self):
        print(self.rayon * 2)

    def afficherInfos(self):
        self.circonference()
        self.aire()
        self.diametre()

cercle1 = Cercle(4)
cercle2 = Cercle(7)

cercle1.afficherInfos()
cercle2.afficherInfos()