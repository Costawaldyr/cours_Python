"""Exercice 1 :
Soit l’entité ‘Facture’ contenant l'identifiant et le nom du client ainsi que le
montant à payer et l'état du paiement (=1 si la facture a été payée et =0 si la facture n'a pas été payée).

entité Facture
composantes: IdC: entier
             Nom: chaîne
             Montant : réel
             Paiement : entier
fent
Soit un fichier d'entités du type ‘Facture’. Le fichier est trié en ordre croissant sur le champ ‘IdC’.
Rédigez en Python un programme qui permet la création d’un fichier :
1. Avec les données suivantes :"""
#Fichier de clients : 1/A/100/1; 1/A/300/1; 1/A/40/1; 3/D/100/0; 3/D/120/1; 3/D/80/1; 3/D/40/1; 6/M/100/0; 6/M/100/0; 9/T/120/1
#2. D’une manière aléatoire
import pickle

class Facture:
    def __init__(self,Idc = 0, nom = "", montant = 0.0, paiement = 0):
        self.Idc = Idc
        self.nom = nom
        self.montant = montant
        self.paiement = paiement
    def __str__(self):
        return f"{self.Idc}/{self.nom}/{self.montant}/{self.paiement}"  
    
def creer_fichier_factures(factures, fichier):
        with open(fichier,"wb") as file:
            for facture in factures:
                pickle.dump(facture,file)
    
def lire_fichier_factures(fichier):
        factures = []
        with open(fichier, "rb") as file:
            while file.peek(1):
                factures.append(pickle.load(file))
        return factures        


def lire_fichier_factures_sequentiellement(fichier):
    with open(fichier, "rb") as file:
        while file.peek(1):
            facture = pickle.load(file)
            print(facture)


    
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
    print("Création du fichier de factures...")
    creer_fichier_factures(factures, fichier)
    print("Fichier créé avec succès.\n")   
    
    print("Lecture du fichier de factures dans une liste...")
    factures_lues = lire_fichier_factures(fichier)
    for facture in factures_lues:
        print(facture)
    print("\nLecture terminée.")
     
    print("Lecture du fichier de factures sequentiellement...")
    lire_fichier_factures_sequentiellement(fichier)
    print("\nLecture terminée.")
          


