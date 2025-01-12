"""Rédigez un programme qui détermine un nombre N entier impair et (pseudo) aléatoire
compris entre 3 et 25 (3 et 25 compris) puis remplisse un tableau de N lignes et N colonnes de
la manière suivante :
a) Les valeurs des éléments des lignes paires et des colonnes impaires (en jaune dans
l'exemple) sont des nombres aléatoires compris entre 0 et N (bornes comprises).

b)Les valeurs des éléments des lignes impaires et des colonnes paires (en bleu dans
l'exemple) sont des nombres aléatoires compris entre N et 20 (bornes comprises).

c)Les valeurs des éléments restants vaudront une numérotation des numéros pairs en
commençant à 0.

d)Les valeurs des éléments de la diagonale allant du coin supérieur gauche au coin
inférieur droit (sauf l'élément de la ligne 0 et de la colonne 0) sont obtenus en
calculant le produit du numéro de la ligne et du numéro de colonne de l’élément.

Une fois le tableau entièrement constitué, le programme doit déterminer si au moins 2
éléments d’une même ligne et de colonnes adjacentes sont impairs. La recherche doit
commencer dans le coin supérieur droit du tableau et ligne par ligne. Lorsqu’un bord du
tableau est atteint, la recherche se poursuit dans la ligne inférieure de la même colonne.
Dès que 2 nombres impairs sont trouvés, le programme doit arrêter la recherche et afficher les
numéros des lignes et colonnes des 2 éléments impairs. Si aucun élément ne vérifie la
condition, un message doit s’afficher pour l’indiquer."""
from random import randint
def afftab(tab):
    for i in range(len(tab)):
        print(tab[i])


n = randint(3,25)

while n % 2 == 0:
    n += 1 
print("N est egal a : ", n)

tab = [[0]*n for i in range(n)]

for i in range(n):
    for j in range(n):
        if i % 2 == 0 and j % 2 != 0:
            tab[i][j]= randint(0,n)
        elif i % 2 != 0 and j % 2 == 0:
            tab[i][j] = randint(n,20)
        elif i == j and i != 0:
            tab[i][j] = i * j
        else:
            tab[i][j]= (i + j) * 2    
afftab(tab)

colonne = n-1
ligne = 0
element_trouve = 0  # Variable pour indiquer si un couple a été trouvé
ligne_resultat_1, colonne_resultat_1 = -1, -1
ligne_resultat_2, colonne_resultat_2 = -1, -1

while colonne >= 0 and element_trouve == 0:
    ligne = 0
    while ligne < N and element_trouve == 0:
        if tableau[ligne][colonne] % 2 != 0:
            # Vérifier à droite si on n'est pas sur la dernière colonne
            if colonne < N - 1 and tableau[ligne][colonne + 1] % 2 != 0:
                element_trouve = 1
                ligne_resultat_1, colonne_resultat_1 = ligne, colonne
                ligne_resultat_2, colonne_resultat_2 = ligne, colonne + 1
            # Vérifier à gauche si on n'est pas sur la première colonne
            elif colonne > 0 and tableau[ligne][colonne - 1] % 2 != 0:
                element_trouve = 1
                ligne_resultat_1, colonne_resultat_1 = ligne, colonne
                ligne_resultat_2, colonne_resultat_2 = ligne, colonne - 1
        ligne += 1
    colonne -= 1

# Résultat
if element_trouve == 1:
    print(f"Deux nombres impairs trouvés :")
    print(f"({ligne_resultat_1}, {colonne_resultat_1}) = {tableau[ligne_resultat_1][colonne_resultat_1]} et ({ligne_resultat_2}, {colonne_resultat_2}) = {tableau[ligne_resultat_2][colonne_resultat_2]}")
else:
    print("Aucun couple d'éléments impairs trouvés dans des colonnes adjacentes.")
