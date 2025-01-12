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

import random
class Facture:
    def __init__(self,Idc = 0, nom = "", montant = 0.0, paiement = 0):
        self.Idc = Idc
        self.nom = nom
        self.montant = montant
        self.paiement = paiement
    def __str__(self):
        return f"{self.Idc}/{self.nom}/{self.montant}/{self.paiement}"  
    
if __name__ == '__main__':
    Idc = [1,1,1,3,3,3,3,6,6,9]
    nom = ["A","A","A","D","D","D","D","M","M","T"]
    montant = [100,300,40,100,120,80,40,100,100,120]
    paiement = [1,1,1,0,1,1,1,0,0,1]

    listClient = [0] * Idc
    for i in range(len(Idc)):
       listClient[i] = Facture(Idc[i],nom[i],montant[i],paiement[i])
    for Facture in listClient:
        print(Facture)
          




