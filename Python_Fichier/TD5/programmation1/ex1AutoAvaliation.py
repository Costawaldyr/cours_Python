import pickle

class Don:
    def __init__(self, IdDonateur=0, Nom="", Somme=0):
        self.IdDonateur = IdDonateur
        self.Nom = Nom
        self.Somme = Somme

    def __str__(self):
        return f"{self.IdDonateur}/{self.Nom}/{self.Somme}"

def creer_fichier_dons(dons, fichier):
    with open(fichier, "wb") as file:
        for don in dons:
            pickle.dump(don, file)

def lire_fichier_dons_sequentiellement(fichier):
    with open(fichier, "rb") as file:
        while file.peek(1):
            don = pickle.load(file)
            print(don)

def traiter_dons(fichier):
    with open(fichier, "rb") as file:
        if not file.peek(1):
            print("Fichier vide !")
        else:
            # 1. Déclarer les variables de travail
            sommeDonateur = 0
            nomDonateurMax = ""
            sommeDonateurMax = 0
            nombreDonateurs = 0
            sommeTotale = 0
            nombreDons = 0
            donEnCours = pickle.load(file)
            DonateurEnCours = donEnCours

            # 2. Parcourir le fichier
            while donEnCours is not None:  
                if donEnCours.IdDonateur == DonateurEnCours.IdDonateur: # opérations pour chaque don                   
                    sommeDonateur += donEnCours.Somme
                    sommeTotale += donEnCours.Somme
                    nombreDons += 1
                    if file.peek(1):
                        donEnCours = pickle.load(file)  
                    else:
                        donEnCours = None    
                else: # ici on clôture le donateur précédent
                    print(f"Le donateur {DonateurEnCours.Nom} a donné {sommeDonateur} € ({nombreDons} dons)")
                    nombreDonateurs += 1
                    if sommeDonateur > sommeDonateurMax:
                        sommeDonateurMax = sommeDonateur
                        nomDonateurMax = DonateurEnCours.Nom
                    # remise à zéro des variables de travail et mise à jour du donateur en cours
                    sommeDonateur = 0
                    nombreDons = 0
                    DonateurEnCours = donEnCours

            # post-traitement pour la dernière clôture
            print(f"Le donateur {DonateurEnCours.Nom} a donné {sommeDonateur} € ({nombreDons} dons)")
            nombreDonateurs += 1
            if sommeDonateur > sommeDonateurMax:
                sommeDonateurMax = sommeDonateur
                nomDonateurMax = DonateurEnCours.Nom

            # 4. Affichage des résultats finaux
            sommeMoyenne = sommeTotale / nombreDonateurs
            print(f"Il y a {nombreDonateurs} donateurs différents pour l'année 2020")
            print(f"{nomDonateurMax} est le donateur ayant donné la plus grande somme")
            print(f"La somme totale donnée = {sommeTotale} €")
            print(f"La somme moyenne donnée = {sommeMoyenne:.2f} €")

if __name__ == '__main__':
    dons = [
        Don(1, "N", 100),
        Don(1, "N", 150),
        Don(1, "N", 200),
        Don(3, "B", 250),
        Don(5, "A", 300),
        Don(7, "Y", 120),
        Don(9, "C", 100),
        Don(9, "C", 120),
        Don(9, "C", 80)
    ]
    
    fichier = "dons.pkl"  
    creer_fichier_dons(dons, fichier)
    lire_fichier_dons_sequentiellement(fichier)
    print("*********************************")
    traiter_dons(fichier)
