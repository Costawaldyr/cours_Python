"""Exercice 1
Une société de distribution d'eau dispose d’un fichier contenant toutes les
factures de ses clients. Soit l’entité ‘Facture’ contenant l'identifiant et le nom
du client ainsi que le montant à payer et l'état du paiement (=1 si la facture
a été payée et =0 si la facture n'a pas été payée).
entité Facture
composantes: IdC: entier
             Nom: chaîne
             Montant : réel
             Paiement : entier
fent
Soit un fichier d'entités du type ‘Facture’. Le fichier est triée en ordre
croissant sur le champ ‘IdC’.
Rédigez en Python un programme
    ✓ qui affiche, pour chaque client, son nom, le montant total à payer
    ✓ qui affiche le nom du client devant payer la plus petite somme totale (qu'elle soit déjà payée ou pas)
    ✓ qui affiche le nombre de factures impayées à ce jour
    ✓ qui affiche le nombre total de clients différents présents dans la liste de clients
    ✓ qui affiche la somme totale de toutes les factures, payées ou pas.

EXEMPLE (PEU RÉALISTE)
Fichier de clients : 1/A/100/1; 1/A/300/1; 1/A/40/1; 3/D/100/0; 3/D/120/1; 3/D/80/1; 3/D/40/1; 6/M/100/0; 6/M/100/0; 9/T/120/1
Le client A doit payer 440 €
Le client D doit payer 340 €
Le client M doit payer 200 €
Le client T doit payer 120 €
Il y a 4 clients différents

Le client T doit payer le plus petit montant total (120 €)
Le nombre de factures pour lesquels les clients n'ont pas payé dans
les délais = 3
La somme totale des factures est de 1100 €
Notes
    1. Le fichier ne peut être lue qu’une seule fois et seulement d’une manière séquentielle à partir du début du fichier.
    2. Une fois que le fichier est constitué, le fichier ne peut pas être stocké dans un (des) tableau(x) ou structure(s) similaire(s).
    3. Le fichier peut être vide.
    4. L’affichage peut être différent de celui de l'exemple.
    5. Vous ne pouvez pas utiliser les structures de contrôles et autres fonctionnalités du langage Python qui n’ont pas été vues en classe."""

import pickle

class Facture:
    def __init__(self, IdC=0, Nom="", Montant=0, Paiement=0):
        self.IdC = IdC
        self.Nom = Nom
        self.Montant = Montant
        self.Paiement = Paiement

    def __str__(self):
        return f"{self.IdC}/{self.Nom}/{self.Montant}/{self.Paiement}"

def creer_fichier_factures(factures, fichier):
    with open(fichier,"wb") as file:
        for facture in factures:
            pickle.dump(facture, file)
            
def lire_fichier_factures_sequentiellement(fichier):
    with open(fichier, "rb") as file:
        while file.peek(1):
            facture = pickle.load(file)
            print(facture)

def traiter_factures(fichier):
    with open(fichier, "rb") as file:
        if not(file.peek(1)):
            print("fichier vide !")
        else :
    # 1 declarer les var de trav
            totClient = 0
            nomClientMin = ""
            totClientMin = float('inf')
            factImpayee = 0
            nbrDeClientDif = 0
            sommeTot = 0
            factureEnCours = pickle.load(file)
            ClientEnCours = factureEnCours
    # 2 on parcour le fichier
            while factureEnCours is not None:  
                if factureEnCours.IdC == ClientEnCours.IdC: # op a chaque fact                    
                    totClient += factureEnCours.Montant
                    sommeTot += factureEnCours.Montant
                    if factureEnCours.Paiement == 0:
                        factImpayee += 1 
                    if file.peek(1):
                        factureEnCours = pickle.load(file)  
                    else:
                        factureEnCours =  None    
                else : # ici on cloture le client prec
                    print(f"Le client {ClientEnCours.Nom} doit payer {totClient}")
                    nbrDeClientDif += 1
                    if totClient < totClientMin:
                        totClientMin = totClient
                        nomClientMin = ClientEnCours.Nom
                    # remise a 0 des var de travail et maj du enCours
                    totClient = 0    
                    ClientEnCours = factureEnCours
    # 3) post traitement == la derniere cloture
            print(f"Le client {ClientEnCours.Nom} doit payer {totClient}")
            nbrDeClientDif += 1
            if totClient < totClientMin:
                totClientMin = totClient
                nomClientMin = ClientEnCours.Nom
    # 4) aff des res finaux  
            print(f"{nomClientMin} a le total minimum de {totClientMin}")
            print(f"Nombre de factures impayées : {factImpayee}")
            print(f"Nombre de clients différents : {nbrDeClientDif}")
            print(f"Somme totale : {sommeTot}")
           
if __name__ == '__main__':
    factures = [
        Facture(1, "A", 100, 1),
        Facture(1, "A", 300, 1),
        Facture(1, "A", 40, 1),
        Facture(3, "D", 100, 0),
        Facture(3, "D", 120, 1),
        Facture(3, "D", 80, 1),
        Facture(3, "D", 40, 1),
        Facture(6, "M", 100, 0),
        Facture(6, "M", 100, 0),
        Facture(9, "T", 120, 1)
    ]  
    fichier = "factures.pkl"  
    creer_fichier_factures(factures, fichier)
    lire_fichier_factures_sequentiellement(fichier)
    print("*********************************")
    traiter_factures(fichier)
