import pickle

class Voyageur:
    def __init__(self, No=0, Nom="", Km=0.0):
        self.No = No
        self.Nom = Nom
        self.Km = Km

    def __str__(self):
        return f"{self.No}/{self.Nom}/{self.Km}"

def creer_fichier_voyageurs(voyageurs, fichier):
    with open(fichier, "wb") as file:
        for voyageur in voyageurs:
            pickle.dump(voyageur, file)

def lire_fichier_voyageurs_sequentiellement(fichier):
    with open(fichier, "rb") as file:
        while file.peek(1):
            voyageur = pickle.load(file)
            print(voyageur)

def traiter_voyageurs(fichier):
    with open(fichier, "rb") as file:
        if not file.peek(1):
            print("Fichier vide !")
        else:
            # 1. Déclarer les variables de travail
            totalKm = 0
            totalVoyageurs = 0
            voyageurs5000KmPlus = 0
            voyageurEnCours = pickle.load(file)
            voyageEnCours = voyageurEnCours

            # 2. Parcourir le fichier
            while voyageEnCours is not None:
                if voyageEnCours.No == voyageurEnCours.No:
                    totalKm += voyageEnCours.Km
                    if file.peek(1):
                        voyageEnCours = pickle.load(file)
                    else:
                        voyageEnCours = None
                else:
                    # Clôturer le traitement du voyageur précédent
                    print(f"Voyageur {voyageurEnCours.Nom} total de : {totalKm:.1f}")
                    totalVoyageurs += 1
                    if totalKm >= 5000:
                        voyageurs5000KmPlus += 1
                    totalKm = 0
                    voyageurEnCours = voyageEnCours
            # Post-traitement pour la dernière clôture
            print(f"Voyageur {voyageurEnCours.Nom} total de : {totalKm:.1f}")
            totalVoyageurs += 1
            if totalKm >= 5000:
                voyageurs5000KmPlus += 1

            # 4. Afficher les résultats finaux
            print(f"Il y a {totalVoyageurs} voyageurs différents")
            print(f"{voyageurs5000KmPlus} voyageurs ont fait plus de 5000 Km")

if __name__ == '__main__':
    voyageurs = [
        Voyageur(1, "A", 1000.0),
        Voyageur(2, "B", 100.0),
        Voyageur(2, "B", 5000.0),
        Voyageur(4, "D", 1600.0),
        Voyageur(6, "F", 3500.0),
        Voyageur(7, "G", 3000.0),
        Voyageur(7, "G", 1100.0),
        Voyageur(8, "H", 4000.0),
        Voyageur(8, "H", 1900.0),
        Voyageur(9, "I", 2000.0)
    ]
    
    fichier = "voyageurs.pkl"
    creer_fichier_voyageurs(voyageurs, fichier)
    lire_fichier_voyageurs_sequentiellement(fichier)
    print("*********************************")
    traiter_voyageurs(fichier)
