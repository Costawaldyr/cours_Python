"""Exercice 3
Une compagnie aérienne propose à ses clients des voyages gratuits en
fonction des kilomètres parcourus à bord de ses avions.
Soit l’entité ‘Voyageur’ contenant le numéro du client, son nom ainsi que
le nombre de kilomètres parcourus lors du voyage correspondant à
l'enregistrement.
entité Voyageur
composantes : No : entier
Nom : chaîne
Km : réel
fent
Le fichier du type ‘Voyageur’ contient tous les enregistrements générés à
chaque nouveau voyage des clients. La liste est triée en ordre croissant sur
le champ ‘No’ et respecte l’ordre chronologique des voyages.
Rédigez un programme qui, pour chaque Voyageur, affiche son nom et le
nombre total de kilomètres parcourus. Le programme affiche aussi le
nombre total de voyageurs ayant parcouru 5000 kms ou plus.
EXEMPLE (PEU RÉALISTE)
Fichiers de voyageurs : 1/A/1000; 2/B/100; 2/B/5000; 4/D/1600;
6/F/3500; 7/G/3000; 7/G/1100; 8/H/4000; 8/H/1900; 9/I/2000
Voyageur A total de : 1000.0
Voyageur B total de : 5100.0
Voyageur D total de : 1600.0
Voyageur F total de : 3500.0
Voyageur G total de : 4100.0
Voyageur H total de : 5900.0
Voyageur I total de : 2000.0
2 voyageurs ont fait plus de 5000Km
Notes
1. Le fichier ne peut être lue qu’une seule fois et seulement d’une
manière séquentielle à partir du début du fichier.
2. Une fois que le fichier est constitué, le fichier ne peut pas être stocké
dans un (des) tableau(x) ou structure(s) similaire(s).
3. Le fichier peut être vide.
4. L’affichage peut être différent de celui de l'exemple.
5. Vous ne pouvez pas utiliser les structures de contrôles et autres
fonctionnalités du langage Python qui n’ont pas été vues en classe."""
import pickle
class Voyageur:
    def __init__(self, no=0,nom="",km=0.0):
        self.no=no
        self.nom=nom
        self.km=km
    def __str__(self):
        return f"{self.no}/{self.nom}/{self.km}"
    
def creer_fichier_voyageur(voyageurs,fichier):
    with open(fichier,"wb") as file:
        for voyageur in voyageurs:
            pickle.dump(voyageur,file)
            
def lire_fichier_voyageur(fichier):
    with open(fichier, "rb") as file:
        while file.peek(1):
            voyageur = pickle.load(file)
            print(voyageur)

def traiter_voyageur(fichier):
    with open(fichier,"rb") as file:
        if not file.peek(1):
            print("Fichier vide")
        else:
            totalKm=0
            totalVoyageurs=0
            voyageurPlusKm=5000
            voyageursEnCours=pickle.load(file)
            voyageEnCours=voyageursEnCours

            while voyageEnCours is not None:
                if voyageEnCours.no==voyageursEnCours.no:
                    totalKm += voyageEnCours.km
                    if file.peek(1):
                        voyageEnCours=pickle.load(file)
                    else:
                        voyageEnCours = None
                else:
                    print()

if __name__=='__main__':
    voyageurs =[
        Voyageur(1,"A",1000.0),
        Voyageur(2,"B",100.0),
        Voyageur(2,"B",5000.0),
        Voyageur(4,"D",1600.0),
        Voyageur(6,"F",3500.0),
        Voyageur(7,"G",3000.0),
        Voyageur(7,"G",1100.0),
        Voyageur(8,"H",4000.0),
        Voyageur(8,"H",1900.0),
        Voyageur(9,"I",2000.0),
    ]       
    fichier_voyageurs="voyageurs.pkl" 
    creer_fichier_voyageur(voyageurs, fichier_voyageurs)
    print("*************************[Fichier creer avec suces]")
    print("[Lecture du fichier]")
    lire_fichier_voyageur(fichier_voyageurs)
    print('-----------------------------')
    