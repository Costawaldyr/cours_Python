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

    