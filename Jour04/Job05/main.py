import math

class Forme:
    def __init__(self):
        pass

    def aire(self):
        return 0


# class Rectangle(Forme):
#     def __init__(self, largeur, hauteur):
#         Forme.__init__(self)
#         self.largeur = largeur
#         self.hauteur = hauteur

#     def aire(self):
#         return self.hauteur * self.largeur


class Cercle(Forme):
    def __init__(self, radius):
        Forme.__init__(self)
        self.radius = radius

    def aire(self):
        return (self.radius ** 2) * math.pi


cercle = Cercle(15)
print(f"Aire du Cercle: {cercle.aire()}")
