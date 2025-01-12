#Exercice 3
import pickle

class Etudiant:
    def __init__(self, Id = 0, Nom = ""):
        self.Id = Id
        self.Nom = Nom
    def __str__(self):
        return f"{self.Id}/{self.Nom}"    
    
class Absence:   
    def __init__(self, Id = 0, hAbs = 0):
        self.Id = Id
        self.hAbs = hAbs
    def __str__(self):
        return f"{self.Id}/{self.hAbs}"    

def creer_fichier(liste, fichier):
    with open(fichier, "wb") as file:
        for obj in liste:
            pickle.dump(obj, file)

def lire_fichier(fichier):
    with open(fichier, "rb") as file:
        while file.peek(1):
            obj = pickle.load(file)   
            print(obj)         

if __name__=='__main__':
    etudiants =[
        Etudiant(1,"A"),
        Etudiant(2,"B"),
        Etudiant(3,"C"),
        Etudiant(4,"D"),
        Etudiant(5,"E"),
        Etudiant(6,"F"),
        Etudiant(7,"G"),
        Etudiant(8,"H"),
        Etudiant(9,"I"),
        Etudiant(10,"J")
    ]

    absences =[
        Absence(1,10),
        Absence(1,5),
        Absence(2,3),
        Absence(3,4),
        Absence(3,10),
        Absence(4,6),
        Absence(5,2),
        Absence(5,2),
        Absence(7,5),
        Absence(8,8),
    ]

    fichier_etudiants = "etudiants.pkl"
    fichier_absences = "absences.pkl"

    print("Création du fichier de etudiantes...")
    creer_fichier(etudiants,fichier_etudiants)
    print("Fichier créé avec succès.\n") 
    print("Lecture du fichier...") 
    lire_fichier(fichier_etudiants)
    
    print("Création du fichier de absences...")
    creer_fichier(absences,fichier_absences)
    print("Fichier créé avec succès.\n")  
    print("Lecture du fichier...")
    lire_fichier(fichier_absences)


