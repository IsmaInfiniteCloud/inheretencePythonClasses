#Shape inheritence exercice in Python OOP

class Shape:
    def init(self, nom):
        self.nom = nom
 
    def get_aire(self):
    """Retourne l'aire de la forme"""
        raise NotImplementedError

    def __str__(self):
    """Retourne une chaine de caractère qui décrit la forme"""
        return f"La forme est {self.nom} et a une aire de {self.get_aire()}"
class Rectangle(Shape):
    def init(self, longueur, largeur):
        super().init("rectangle")
        self.longueur = longueur
        self.largeur = largeur
 
    def get_aire(self):
    """Retourne l'aire du rectangle"""
        return self.longueur * self.largeur
class Triangle(Forme):
    def init(self, base, hauteur):
    super().init("triangle")
    self.base = base
    self.hauteur = hauteur
 
    def get_aire(self):
    """Retourne l'aire du triangle"""
        return (self.base * self.hauteur) / 2

class Cercle(Shape):
    def init(self, rayon):
    super().init("cercle")
    self.rayon

rec = Rectangle(6, 5)
print(rec)
triangle = Triangle(5, 8)
print(triangle)
cercle = Cercle(4)
print(cercle)
