class Rectangle():
    def __init__(self, longueur, largeur) -> None:
        self.__longueur = longueur
        self.__largeur = largeur

    def perimetre(self):
        return (2 * self.__longueur) + (2 * self.__largeur)

    def surface(self):
        return self.__longueur * self.__largeur

    def __set_longueur(self, newlongueur):
        self.__longueur = newlongueur

    def __set_largeur(self, newlargeur):
        self.__largeur = newlargeur

    def get_longueur(self):
        return self.__longueur

    def get_largeur(self):
        return self.__largeur
    
    def changeSize(self, newlongueur, newlargeur):
        rectangle_0.__set_largeur(newlargeur)
        rectangle_0.__set_longueur(newlongueur)
    
class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        Rectangle.__init__(self, longueur, largeur)
        self.__hauteur = hauteur

    def volume(self):
        return self.surface() * self.__hauteur
    
rectangle_0 = Rectangle(15, 30)
para_0 = Parallelepipede(15, 30, 20)

print(f"Premier rectangle : \n perimetre :{rectangle_0.perimetre()} \n surface :{rectangle_0.surface()}")

print(f"Premier para : \n perimetre :{para_0.perimetre()} \n surface :{para_0.surface()} \n surface :{para_0.volume()}")

rectangle_0.changeSize(10, 20)

print(rectangle_0.get_largeur())
print(rectangle_0.get_longueur())