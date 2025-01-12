
"""Exercice 02 :
Ecrire un programme Python pour gérer les notes d'un groupe d'étudiants. Chaque étudiant
possède les informations suivantes :
➢ Nom de l'étudiant : une chaîne de caractères représentant le nom de l'étudiant.
1
a) ➢ Liste des notes : une liste d'entiers représentant les notes obtenues par l'étudiant
dans différentes matières.
Créer une classe Etudiant qui contient les informations suivantes :
✓ Le nom de l'étudiant.
✓ Les notes obtenues dans les différentes matières.
b) Créez au moins 3 Etudiants différents avec des attributs variés (minimum 3 notes).
c) Créer une fonction qui calcule la moyenne des notes d’un étudiant grâce à une fonction
que vous allez créer.
d) Créer une fonction qui affiche les informations de tous les étudiants, y compris leur nom,
leurs notes et leur moyenne.
e) Créer une fonction qui permet de trouver et afficher l'étudiant ayant la meilleure moyenne.
f) Créer une fonction qui permet de trouver et afficher l'étudiant ayant la moins bonne
moyenne."""

class Etudiant:
    def __init__(self,nom = "", note = None):
        if note is None:
            note=[]
        self.nom =  nom
        self.note = note
    def __str__(self):
        return f"{self.nom} | Note obtenue : {self.note}"   
    
def calculMoy(nom, note):
    for i in range(len(nom)):
        sommeMoy = 0
        for j in range(len(note[i])):
            sommeMoy += note[i][j]
        sommeNote = len(note[i])
        moyenne = sommeMoy / sommeNote
        print(f"{nom[i]} a une moyenne de :{moyenne}")  

def moyenne(notes):
    if not note : #si pas note retune 0
        return 0
    return sum(notes)/len(notes)

def affichageClass(etudiants):
    for etudiant in etudiants:
        print(etudiant)

def trouver_meilleure_moyenne(etudiants):
    meilleur = etudiants[0]
    for etudiant in etudiants[1:]:
        if moyenne(etudiant.note) > moyenne(meilleur.note):
            meilleur = etudiant
    print(meilleur)  

def trouver_derniere_moyenne(etudiants):
    dernier = etudiants[0]
    for etudiant in etudiants[1:]:
        if moyenne(etudiant.note) < moyenne(dernier.note):
            dernier = etudiant
    print(dernier)                      
 

if __name__ == '__main__':
    print("-----------------B-------------------")
    
    nom = ["Alfredo Alvaro", "Joao Silva", "Daniela Santos", "Santiago Cacillia"]   
    note = [[13,9,10,17], [15,19,13,13], [8.5,13,9,10], [18,17.5,13,15]]  

 
    listeNote = [0] * len(nom)

    for i in range(len(nom)):
        listeNote[i] = Etudiant(nom[i],note[i])

    for Etudiant in listeNote:
        print(Etudiant) 
    print("-----------------C--------------------") 
    calculMoy(nom,note)
    
    