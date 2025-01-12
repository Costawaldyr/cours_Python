"""Exercice 2
Soit l’entité Eleve
entité Eleve:
    composantes :   Id : entier
                    Nom : chaîne
                    Note : entier
fent
Rédigez un programme qui pour tous les élèves apparaissant dans un
fichier, affiche son nom et sa moyenne (somme des notes divisée par le
nombre de notes). Le programme doit également afficher le nombre total
d’élèves et le nombre d’élèves ayant obtenu plus de 10 de moyenne (il est
donc supposé que chaque note est sur 20 et que les notes ont le même
poids).
EXEMPLE (PEU RÉALISTE)
Fichier d’élèves : 1/A/10; 1/A/15; 1/A/6; 2/B/16; 2/B/11; 3/C/3; 5/E/11; 8/H/14; 8/H/19; 9/I/20
    Elève A moyenne de : 10.33
    Elève B moyenne de : 13.5
    Elève C moyenne de : 3
    Elève E moyenne de : 11
    Elève H moyenne de : 16.5
    Elève I moyenne de : 20
Il y a 6 élèves différents 5 élèves ont obtenus une moyenne de plus de 10 Notes
1. Le fichier ne peut être lue qu’une seule fois et seulement d’une
manière séquentielle à partir du début du fichier.
2. Une fois que le fichier est constitué, le fichier ne peut pas être stocké
dans un (des) tableau(x) ou structure(s) similaire(s).
3. Le fichier peut être vide.
4. L’affichage peut être différent de celui de l'exemple.
5. Vous ne pouvez pas utiliser les structures de contrôles et autres
fonctionnalités du langage Python qui n’ont pas été vues en classe."""

import pickle
class Éléves:
    def __init__(self,Id=0, nom = "", note = None):
        self.nom =  nom
        self.note = note
        self.Id = Id
    def __str__(self):
        return f"{self.Id}/{self.nom}/{self.note}"
    

def creer_fichier_eleves(eleves, fichier):
    with open(fichier,"wb") as file:
        for eleve in eleves:
            pickle.dump(eleve, file)

def lire_fichier_eleves(fichier):   
    with open(fichier, "rb") as file:
        if not file.peek(1):
            print("fichier vide!")
        else:
            totNotes=0
            nbrNotes=0
            totalEleves=0
            elevesAuDessusDe10=0
            eleveEnCours=pickle.load(file)
            NoteEnCours= eleveEnCours
            

if __name__ == '__main__':
    eleves = [
        Éléves(1,"A",10),
        Éléves(1,"A",15),
        Éléves(1,"A",6),
        Éléves(2,"B",16),
        Éléves(2,"B",11),
        Éléves(3,"C",3),
        Éléves(5,"E",11),
        Éléves(8,"H",14),
        Éléves(8,"H",19),
        Éléves(9,"I",20),
    ]

    fichier_eleve = "eleves.pkl"
    creer_fichier_eleves(eleves, fichier_eleve)
    print("Fichier creer avec suces")
    print("\nLecture du fichier")
    lire_fichier_eleves(fichier_eleve)
