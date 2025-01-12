"""Exercice 1 (facile) :
Écrire un programme qui permet de saisir 2 notes (de 0 à 20) : une pour le cours de français, une
pour le cours de math. Le programme affichera l’information suivante en fonction des résultats :
- « Réussite » : dans le cas où Math et Français sont réussis.
- « Echec total » : dans le cas où Math et Français sont ratés.
- « Examen de passage en Français » : dans le cas où Math est réussi et Français est raté.
- « Examen de passage en Math. » : dans le cas où Math est raté et Français est réussi."""
from random import randint

math = randint(0,20)
print("Notes de Math :", math)
francais = randint(0,20)
print("Notes de Francais :", francais)

if math >= 10 and francais >= 10 :
    print("Reussite")
elif math >= 10 and francais < 10:
    print("Examen de passage en Francais")
elif francais >= 10 and math < 10:
    print("Examen de passage en Math") 
else:
    print("Echec total")           

"""Exercice 2 (facile) :
Écrire un programme qui calcule et affiche la moyenne arithmétique de 2 nombres si la somme de
ces 2 nombre est paire. Si cette somme est impaire, on calculera et affichera plutôt la moyenne
géométrique.
Remarque :
• La moyenne arithmétique est la somme des valeurs divisée par le nombre de valeurs.
• La moyenne géométrique est la racine Nième du produit des valeurs."""    
from math import *
a = randint(0,20)
b = randint(0,20)
somme = a + b 
if somme % 2 == 0:
    moy = somme // 2
    print("Moyenne arithmetique", moy)
else:
    moy_2 = sqrt(a*b) 
    print("La moyenne geometrique", moy_2) 

"""Exercice 3 (moyen) :
Écrire un programme permettant de lire une date (j/m/a) et déterminer le jour de la semaine.
Pour janvier et février, il faut augmenter m de 12 et diminuer a de 1. Ensuite calculer :
s ← [a/100]
JD ← 1720996,5 - s + s \ 4 + [365,25*a] + [30,6001*(M+1)] + j
JD ← JD - [JD/7]*7
JS ← [JD] MOD 7
Si JS = 0, le jour est mardi, ...., si JS = 6, le jour est lundi.
NOTE : le programme est valable pour les dates postérieures à 1582."""   

jour = int(input("?"))
mois = int(input("?"))
annee = int(input("?"))
if mois == 1 or 2 :
    mois += 12
    annee -= 1

s = (annee /100)
jd = 1720996,5 - s + s / 4 + int(365,25 * annee)  + int(30,6001 * (mois + 1) + jour)
jd = jd - int(jd/7) * 7
js = int(jd) % 7
if js == 0:
    print("Le jour est ,mardi")
elif js == 6:
    print("le jour est lundi")    


"""Exercice 4 (difficile) :
Reprendre l’exercice 1 mais avec 3 notes (ajoutons le cours d’informatique). Par contre, l’étudiant
a droit à 3 points de balance (c’est-à-dire maximum 3 points en dessous de 10. Donc au pire un
7/20, un 8/20 et un 9/20, ou encore trois 9/20). Écrire un programme qui permet de saisir ces 3
notes (de 0 à 20) et qui affichera l’information suivante en fonction des résultats :
- « Réussite » : dans le cas où Math, Français, Informatique sont réussis avec max 3 points
de balance (le nombre de points de balance doit aussi être indiqué).
- « Examen de passage en … » : pour chaque note en échec (s’il y a plus de 3 points de
balance).
Notons que les points de balance ne sont valables que pour la réussite totale. Donc si un
étudiant a une note de 6/20 ou moins il sera ajourné d’office."""

