import random
import pickle
class Etudiant:
    def __init__(self, Id=0, nom=""):
        self.Id = Id  
        self.nom = nom  
    def __str__(self):
        return f"Etudiant No: {self.Id}, Nom: {self.nom}"

class Absence:
    def __init__(self, Id=0, hAbs=0):
        self.Id =Id  
        self.hAbs = hAbs  
        
    def __str__(self):
        return f"Absence - Client ID: {self.Id}, Habs: {self.hAbs}"

def creer_liste_etudiant_valeur_fixe():
    # Liste de clients 
    idc = [1, 2, 4, 5, 6, 7, 8, 9, 10]
    nom = ["A", "B", "D", "E", "F", "G", "H", "I", "J"]
    listeetudiant = [0]*len(idc)
    for i in range (len(idc)):
        listeetudiant[i]= Etudiant(idc[i],nom[i])
        
    return listeetudiant

def creer_liste_absence_valeur_fixe():
    # Liste de voyages 
    ids = [1, 2, 2, 4, 6, 7, 7, 8, 8, 9]
    lhabs = [10, 5, 3, 4, 10, 6, 2, 2, 5, 8]
    listehabs = [0]*10
    for i in range (len(ids)):
        listehabs[i]= Absence(ids[i],lhabs[i])
    return listehabs 

def afficher_liste_etudiant(listeetudiant):
    for le in listeetudiant:
        print(le)

def afficher_liste_absence(listeabsence):
    for la in listeabsence:
        print(la)

def creer_liste_etudiant_valeur_random():
    n = random.randint(5, 10) 
    print(f"Nombre de etudiants générés: {n}")
    etudiants = [0]*n
    id_client = 0
    for i in range(n):
        id_client += random.randint(1, 3)
        etudiants[i]=Etudiant(id_client, rand_nom())
    return etudiants

def rand_nom():
    voy = "aeiouy"
    cons = "zrtpmlkjhgfdsqxcvbnw"
    n = random.randint(4, 6)  # Longueur aléatoire du nom
    ch = ""
    for i in range(n):
        if i % 2 == 0:  # Alternance consonne/voyelle
            ch += cons[random.randint(0, len(cons) - 1)]
        else:
            ch += voy[random.randint(0, len(voy) - 1)]
    return ch.capitalize()  # 1ère lettre en maj

def creer_liste_absence_valeur_random(etudiants):
    absences = []  # Liste des voyages
    for etudiant in etudiants:
        # Chaque etudiant peut avoir plusieurs absences (entre 0 et 3)
        for cpt in range(random.randint(0, 3)): 
            habs = random.randint(2, 10)
            absences.append(Absence(etudiant.Id, habs))
    return absences

def creer_fichier(liste, fichier):
    with open(fichier, "wb") as file:
        for obj in liste:
            pickle.dump(obj, file)

def lire_fichier(fichier):
    with open(fichier, "rb") as file:
        while file.peek(1):
            obj = pickle.load(file)
            print(obj)            


# Programme principal
if __name__ == "__main__":
    
    listeEtudiant=creer_liste_etudiant_valeur_fixe()
    print("Liste des etudiants (fixe) :")
    afficher_liste_etudiant(listeEtudiant)
    listeabsence=creer_liste_absence_valeur_fixe()
    print("\nListe des absences (fixe) :")
    afficher_liste_absence(listeabsence)
    # RANDOM
    liste_etudiant = creer_liste_etudiant_valeur_random()
    print("Liste des etudiants (random) :")
    afficher_liste_etudiant(liste_etudiant)   
    liste_absence = creer_liste_absence_valeur_random(liste_etudiant)
    print("\nListe des absences (random) :")
    afficher_liste_absence(liste_absence)

    fichier_etudiants = "etudiants.pkl"
    fichier_absences = "absences.pkl"

    print("Création du fichier de etudiantes...")
    creer_fichier(listeEtudiant,fichier_etudiants)
    print("Fichier créé avec succès.\n") 
    print("Lecture du fichier...") 
    lire_fichier(fichier_etudiants)
    
    print("Création du fichier de absences...")
    creer_fichier(listeabsence,fichier_absences)
    print("Fichier créé avec succès.\n")  
    print("Lecture du fichier...")
    lire_fichier(fichier_absences)