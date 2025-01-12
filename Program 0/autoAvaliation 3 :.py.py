"""Exercice 1 :
Écrire un programme qui consiste à faire deviner à l’utilisateur un nombre (compris entre 10000 et
50000). Le programme répondra à chaque saisie si le nombre à découvrir est plus petit, ou plus
grand jusqu’à ce que l’utilisateur découvre le nombre secret."""

from random import randint

def new_func(nombre_secret, nombre):
    while not nombre == nombre_secret :
        nombre = int(input("Introduisez un nombre compris entre 10.000 et 50.000 :"))
        if  nombre< nombre_secret:
            print("Plus grand")
        elif nombre == nombre_secret:
            print("Felicitation, vous avez reussir") 
        else:
            print("Plus petit")
    print("Le nombre secret est :", nombre_secret)   

if __name__ == '__main__':
    nombre_secret = randint(10000,50000)
    nombre = 0
    new_func(nombre_secret, nombre)

"""Exercice 2 :
Écrire un programme qui dont les règles sont les mêmes que l’exercice précédent sauf qu’on
inverse les rôles. CAD que c’est l’utilisateur qui choisit le nombre secret et que c’est au programme
de le trouver."""

codeSecret = int(input("Entrez votre nombre secret entres 10.000 et 50.0000 :"))
nbr = 10000
while nbr != codeSecret:
    nbr += 1
    print(nbr)    

"""Exercice 3 :
Écrire un programme java qui affiche un motif triangulaire dont la hauteur du triangle (c’est-à-dire
son nombre de lignes) sera fournie en donnée (lue au clavier). Exemple de trace d'exécution :
Donner le nombre de lignes : 6
******
*****
****
***
**
*
"""
n = 6
for i in range(n, -1,-1):
    print("*" * i)