import random 
class Etudiant:
    def __init__(self,id_etudiant = 0, nom_etudiant =""):
        self.id_etudiant = id_etudiant
        self.nom_etudiant = nom_etudiant
    def __str__(self):
        return f"{self.id_etudiant}/{self.nom_etudiant}"    

class Absence:   
    def __init__(self,id_etudiant  = 0, hAbs = 0):
        self.id_etudiant = id_etudiant
        self.hAbs = hAbs
    def __str__(self):
        return f"{self.id_etudiant}/{self.hAbs}"   
    
def list_Etudiant():
    id_etudiant = [1,2,3,4,5,6,7,8,9,10]
    nom_etudiant = ["A","B","C","D","E","F","G","H","I","J"]
    list_etudiant = [0] * len(id_etudiant)
    for i in range(len(id_etudiant)):
        list_etudiant[i] = Etudiant(id_etudiant[i], nom_etudiant[i])
    return list_etudiant   

def list_Absence():
    id_etudiant = [1,1,2,3,3,4,5,5,7,8]
    hAbs = [10,5,3,4,10,6,2,2,5,8]
    list_hAbs = [0]* len(id_etudiant)
    for i in range(len(id_etudiant)):
        list_hAbs[i]= Absence(id_etudiant[i], hAbs[i])
    return list_hAbs   
    

def creer_list_etudiant_rand():
    n = random.randint(5,10)
    print("N = ", n)
    list_etudiant = [0] * n
    id_etudiant = 0
    for i in range(n):
        id_etudiant += random.randint(1,3)  
        list_etudiant[i] = Etudiant(id_etudiant, rand_nom())
    return list_etudiant  


def rand_nom():
    consonne = "bcdfghjklmnprstvwxz"
    voyelle = "aeiouy"
    n = random.randint(4,9)
    ch =""
    for i in range(n):
        if i % 2 == 0:
            ch += consonne[random.randint(0,len(consonne)-1)]
        else:
            ch += voyelle[random.randint(0,len(voyelle)-1)]
    return ch.capitalize()  

def creer_list_Absence_rand(list_etudiant):
    list_hAbs = []
    for etudiant in list_etudiant:
        for cpt in range(random.randint(0,3)):
            hAbs = random.randint(2,10)
            list_hAbs.append(Absence(etudiant.id_etudiant, hAbs))
    return list_hAbs  


def affichage_list_Etudient(list_etudiant):
    for etudiant in list_etudiant :
        print(etudiant) 

def affichage_list_Absence(list_hAbs):
    for absence in  list_hAbs:
        print(absence) 


if __name__=='__main__':
    fichier_etudiant =  list_Etudiant()
    fichier_absence = list_Absence()

    print("Liste des Etudiant(fixes):")
    affichage_list_Etudient(fichier_etudiant)
    print("\nListe des Absence (fixes): ")
    affichage_list_Absence(fichier_absence)

    print("\nÉtudiants générés aléatoirement :")
    etudiants_aleatoires = creer_list_etudiant_rand()
    affichage_list_Etudient(etudiants_aleatoires)

    print("\nAbsences générées aléatoirement :")
    absences_aleatoires = creer_list_Absence_rand(etudiants_aleatoires)
    affichage_list_Absence(absences_aleatoires)











    




