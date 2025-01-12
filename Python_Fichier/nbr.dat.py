"""Rédigez un programme qui permet de créer un fichier texte "nbr.dat" qui contient une liste de 20 entiers aléatoires.
 ces entiers sont des valeurs aléatoires comprises en 0 et 100"""

from random import randint
with open("nbr.dat", "w") as fichier:
    for i in range(20):
        nombre = randint(0,100)
        fichier.write(f"{nombre}\n")
print("Les nombres aleatoires ont ete ecrits dans 'nbr.dat'")        
        
