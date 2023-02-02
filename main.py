"""
Thomas Hamel 406 tp4 : Introduction a la programation
"""
import random
from math import pi


class StringFoo:
    def __init__(self):
        self.message = ""

    def set_string(self, msg):
        self.message = msg

    def print_string(self):
        print(self.message)


sf = StringFoo()
sf.set_string("patate")
sf.print_string()

class rectangle:
    def __init__(self, largeur, longueur):
        self.largeur = largeur
        self.longueur = longueur

    def aire(self):
        return self.longueur * self.largeur

    def afficher_info(self):
        print(f"{self.longueur}{self.largeur}{self.aire()}")

print(rectangle(5, 6).aire())
class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def calcul_aire(self):
        return self.rayon ** 2 * pi

    def calcul_circonference(self):
        return self.rayon * 2 * pi

print(Cercle(5).calcul_aire())
print(Cercle(5).calcul_circonference())
