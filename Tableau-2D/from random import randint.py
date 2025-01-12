from random import randint

def affTab(tab):
    for i in range(len(tab)):
        print(tab[i])


n = randint(3,25)
while n % 2 == 0:
    n = randint(3,25)
print("La valeur de N est :", n)  



import random

# Générer un nombre N impair entre 3 et 25
N = 3 + 2 * random.randint(0, 11)  # 3, 5, 7, ..., 25

# Initialiser le tableau
tableau = [[0 for _ in range(N)] for _ in range(N)]

# Remplir le tableau selon les règles
for i in range(N):
    for j in range(N):
        if i % 2 == 0 and j % 2 != 0:  # Lignes paires, colonnes impaires
            tableau[i][j] = random.randint(0, N)
        elif i % 2 != 0 and j % 2 == 0:  # Lignes impaires, colonnes paires
            tableau[i][j] = random.randint(N, 20)
        elif i == j and i != 0:  # Diagonale principale (sauf 0,0)
            tableau[i][j] = i * j
        else:  # Numérotation des numéros pairs
            tableau[i][j] = (i + j) * 2

# Afficher le tableau pour vérification
print("Tableau généré :")
for ligne in tableau:
    print(ligne)

# Recherche des éléments impairs dans des colonnes adjacentes avec while
colonne = N - 1
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

#-------------------------------------------------------------------------------


import random

# Générer un nombre N impair entre 3 et 25
N = 3 + 2 * random.randint(0, 11)  # 3, 5, 7, ..., 25

# Initialiser le tableau
tableau = [[0 for _ in range(N)] for _ in range(N)]

# Remplir le tableau selon les règles
for i in range(N):
    for j in range(N):
        if i % 2 == 0 and j % 2 != 0:  # Lignes paires, colonnes impaires
            tableau[i][j] = random.randint(0, N)
        elif i % 2 != 0 and j % 2 == 0:  # Lignes impaires, colonnes paires
            tableau[i][j] = random.randint(N, 20)
        elif i == j and i != 0:  # Diagonale principale (sauf 0,0)
            tableau[i][j] = i * j
        else:  # Numérotation des numéros pairs
            tableau[i][j] = (i + j) * 2

# Afficher le tableau pour vérification
print("Tableau généré :")
for ligne in tableau:
    print(ligne)

# Recherche des éléments impairs dans des colonnes adjacentes
element_trouve = 0  # Variable pour arrêter la recherche si un couple est trouvé
ligne_resultat_1, colonne_resultat_1 = -1, -1
ligne_resultat_2, colonne_resultat_2 = -1, -1

for colonne in range(N - 1, -1, -1):  # Commence en haut à droite
    for ligne in range(N):
        if tableau[ligne][colonne] % 2 != 0 and colonne < N - 1:
            if tableau[ligne][colonne + 1] % 2 != 0:  # Vérifier à droite
                element_trouve = 1
                ligne_resultat_1, colonne_resultat_1 = ligne, colonne
                ligne_resultat_2, colonne_resultat_2 = ligne, colonne + 1
        if tableau[ligne][colonne] % 2 != 0 and colonne > 0:
            if tableau[ligne][colonne - 1] % 2 != 0:  # Vérifier à gauche
                element_trouve = 1
          
