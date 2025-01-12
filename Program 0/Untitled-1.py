"""Exercice 12 :
Écrire un programme permettant de lire un nombre N entier positif et créer un nouveau
nombre par l’écriture des chiffres de N de droite à gauche.
Exemple : si N=9876, le nouveau nombre sera 6789"""
from random import randint
n= randint(0,999999)
nbr=0
chiffre=0
print("n:",n)
    #solution la plus simple
    #boucle tant que (chiffre N n'est pas fini)
while n!=0:
    #on extrait le chiffre le plus a droite
    chiffre = n%10
    # on div /10 le N
    n = n//10 #  n//=10
    #on fait *10 sur mon nouveau nbr
    nbr = nbr*10 # nbr*=10
    #on add le chiffre extrait de N a nbr
    nbr = nbr+chiffre # nbr+=chiffre
    # fin TQ
print(nbr)


