"""Exercice 01
Rédigez un programme qui permet de créer un fichier texte "nbr.dat" qui contient une liste de 20 entiers aléatoires.
 ces entiers sont des valeurs aléatoires comprises en 0 et 100"""
#creeation de fichier
from random import randint
with open("nbr.dat", "w") as fichier:
    for i in range(20):
        nombre = randint(0,100)
        fichier.write(f"{nombre}\n")
print("Les nombres aleatoires ont ete ecrits dans 'nbr.dat'")        
        
"""Exercice 02
Rédigez un programme qui lit un fichier texte « nbr.dat » qui contient une liste d’entiers
aléatoires. Le programme doit lire les nombres un à un"""   
#Lecture du fichier:

with open("nbr.dat", "r") as fichier:
    for ligne in fichier:
        nombre = int(ligne)
        print(nombre)

#autre solution:---------------------------
with open("nbr.dat", "r") as fichier:   
    ligne = fichier.readline()
    while ligne:
        nombre = int(ligne)
        print(nombre)
        ligne = fichier.readline()

#AURTE SOLUTION -------------------------
fich = open("nbr.dat", "r")
contenu = ""
while 1:
    ligne = fich.readline()
    if (ligne == ""):
        break
    contenu += ligne
print(contenu)
fich.close()                

"""Exercice 03
Rédigez un programme qui remplit un fichier « F.dat » avec des nombres entiers aléatoires
compris entre -100 et 100 jusqu’à l’apparition du nombre 0. Le programme doit lire "F" une
seule fois et séquentiellement et recopier les nombres positifs ou nuls dans le fichier
"FPOS.dat" et les nombres négatifs dans "FNEG.dat"."""
import random
with open("F.dat", "w") as fichier:
    nombre = random.randint(-100,100)
    while nombre != 0:
        fichier.write(f"{nombre}\n")
        nombre = random.randint(-100,100)
print("Les nombres aleatoires ont ete ecrits dans 'F.dat'")  
#_______________________________________________________________________________________
# prof ----------SOLUCTION----------------
import random

def process_numbers(input_file,positive_file,negative_file):

    with open(input_file, "r") as f1, \
         open(positive_file, "w") as fpos, \
         open(negative_file, 'w') as fneg:
         
        for line in f1:
            line = line.strip()
            if line:
                number = int(line)
                if number >= 0:
                    fpos.write(f"{number}\n")
                else:
                    fneg.write(f"{number}\n")
    print("Les nombresmont ete correctement tries dans les fichiers")

def remplissage(fich):
    #ouvrir un fichier en mode lecture
    with open(fich, 'w') as fichier:
        for i in range(20):
            nombre = random.randint(-100,100)
            #ecrire les entiers dans le fichier
            fichier.write(f"{nombre}\n")
    print("Les nombres aleatoires ont ete ecrits dans 'F.dat'") 
remplissage("F.txt")          
process_numbers("F.txt", "FPOS.txt", "FNEG.txt")        


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

"""Exercice 2 :
Soient l’entité Client’ contenant le numéro du client et son nom et l’entité Voyage contenant le numéro du client 
et le nombre total de kilomètres parcourus.
entité Client
composantes :   No : entier
                Nom : chaîne
fent                
entité Voyage
composantes :   No : entier
                Km : réel
fent
Le fichier de type Client’ contient les renseignements correspondant à chaque client. Le fichier de type Voyage
contient tous les enregistrements générés à chaque nouveau voyage. Les deux fichiers sont triés en ordre
croissant sur le champ No et respectent l’ordre chronologique des voyages.
Rédigez en Python un programme qui permet la création de deux fichiers :"""
#1. Avec les données suivantes : 
#Fichier de Clients : 1/A; 2/B; 4/D; 5/E; 6/F; 7/G; 8/H; 9/I
#Fichier de voyages : 1/1000; 2/100; 2/5000; 4/1600; 6/3500; 7/3000; 7/1100; 8/4000; 8/1900; 9/2000
#2. D’une manière aléatoire.
import pickle
class Client:
    def __init__(self, no = 0, nom = ""):
        self.no = no
        self.nom = nom
    def __str__(self):
        return f"No: {self.no}, Nom: {self.nom}"

class Voyage:
    def __init__(self, no1 = 0, km = 0):
        self.no1 = no1
        self.km = km
    def __str__(self):
        return f"No: {self.no1}, Km: {self.km}"
    
def creer_fichier_client(clients,fichier):
    with open(fichier, "wb") as file:
        for client in clients:
            pickle.dump(client,file) 

def creer_fichier_voyage(voy, fichier):
    with open(fichier, "wb" ) as file :
        for voyage in voy:
            pickle.dump(voyage, file)

def lire_fichier(fichier):
    items = []
    with open(fichier, "rb") as file:
        while file.peek(1):
            items.append(pickle.load(file))
    return items        




if __name__ == '__main__':

    clients = [
        Client(1,"A"),
        Client(2,"Q"),
        Client(4,"W"),
        Client(5,"A"),
        Client(6,"F"),
        Client(6,"T"),
        Client(7,"E"),
        Client(9,"D")
        ]
    voy = [
       Voyage(1,1000),
       Voyage(2,100),
       Voyage(2,5000),
       Voyage(4,1600),
       Voyage(6,3500),
       Voyage(7,3000),
       Voyage(7,1100),
       Voyage(8,4000),
       Voyage(8,1900),
       Voyage(9,2000)   
    ]

    fichier_clients ="clients.pkl"
    fichier_voyage ="voy.pkl"
    print("Creation du fichier de clients...")
    creer_fichier_client(clients, fichier_clients)
    print("fichier des clients cree avec succes. \n")
    print("creation du fichier voyages...\n")
    creer_fichier_voyage(voy, fichier_voyage)
    print("fichier des voyages cree avec succes. \n")
    print("Lecture du fichier de clients...")
    clieents_lus = lire_fichier(fichier_clients)
    for client in clieents_lus:
        print(client)
    print("\nLectures des clients terminee.\n")
    print("Lecture du fichier de voyages.\n")
    voyages_lus = lire_fichier(fichier_voyage)
    for voyage in voyages_lus:
        print(voyage)
    print("\nLecture des voyages terminee.\n")    

# methode aleatoire 

import random 
import pickle

class Client:
    def __init__(self, no = 0, nom = ""):
        self.no = no
        self.nom = nom
    def __str__(self):
        return f"No: {self.no}, Nom: {self.nom}"
     
class Voyage:
    def __init__(self, id_client = 0, km = 0):
        self.id_client = id_client
        self.km = km
    def __str__(self):
        return f"No: {self.id_client}, Km: {self.km}"
     
def list_Client():
    no = [1,2,4,5,6,7,8,9]
    nom = ["A","B","D","E","F","G","H","I"]
    clients = [0] * len(no)
    for i in range(len(no)):
        clients[i] = Client(no[i], nom[i])
    return clients  

def affichage_list_client(clients):
    for client in clients:
        print(client) 

def list_Voyage():
    no1 = [1,2,2,4,6,7,7,8,8,9]
    km = [1000,100,5000,1600,3500,3000,1100,4000,1900,2000]
    voy = [0] * len(no1)
    for i in range(len(no1)):
        voy[i] = Voyage(no1[i], km[i])
    return voy    

def affichage_list_voyage(voy):
    for voyage in voy:
        print(voyage) 

def creer_liste_client_valeurRandom():
    n = random.randint(5,10)
    print("N = ", n)    
    clients = [0] * n
    no = random.randint(1,100)
    for i in range(n):
        if i > 0:
            no +=random.randint(1,3)
        nom = rand_nom()
        clients[i]=Client(no,nom)
    return clients  

def creer_liste_voyage_valeurRandom(clients):
    voyages = []
    for client in clients:
        for cpt in range(random.randint(0,3)):
            km = random.randint(2, 50) * 50
            voyage = Voyage(client.no, km)
            voyages.append(voyage)
    return voyages  

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

def creer_fichier_client(client,fichier):
    with open(fichier, "wb") as file:
        for client in clients:
            pickle.dump(client,file)      

def creer_fichier_voyage(voyage, fichier):
    with open(fichier, "wb") as file:
        for voyage in voy:
            pickle.dump(voyage,file)

"""def creer_fichier(liste,fich):
    with open(fich, "wb") as file:
        for obj in liste:
            pickle.dump(obj,file)"""  # fonction pour creer fichier idependente do nome


def lire_fichier(fichier):
    items = []
    with open(fichier, "rb") as file:
        while file.peek(1):
            items.append(pickle.load(file))
    return items        


if __name__ == '__main__':
  
    clients = list_Client()
    voy = list_Voyage()

    print("Liste des client (fixes):")
    affichage_list_client(clients)

    print("\nListe des voyages (fixes): ")
    affichage_list_voyage(voy)

    print("\nCreation de liste aleatoire...\n")
    liste_client = creer_liste_client_valeurRandom()
    liste_voyage = creer_liste_voyage_valeurRandom(liste_client)

    print("\nListe client générées aléatoirement :")
    affichage_list_client(liste_client)

    print("\nListe voyages générées aléatoirement :")
    affichage_list_voyage(liste_voyage)

    # Fichier
    
    fichier_Client = "clients.pkl"
    fichier_Voyage = "voy.pkl"

    print("Creation du fichier de clients...")
    creer_fichier_client(liste_client, fichier_Client)
    print("fichier des clients cree avec succes. \n")

    print("Creation du fichier de voyages...")
    creer_fichier_voyage(liste_voyage, fichier_Voyage)
    print("fichier des voyages cree avec succes. \n")

    print("Lecture du fichier de clients...")
    clieents_lus = lire_fichier(fichier_Client)
    for client in clieents_lus:
        print(client)
    print("\nLectures des clients terminee.\n")
    
    print("Lecture du fichier de voyages.\n")
    voyages_lus = lire_fichier(fichier_Voyage)
    for voyage in voyages_lus:
        print(voyage)
    print("\nLecture des voyages terminee.\n")    

 
"""Exercice 3 :
Soient les entités Etudiant et Absence 
entité Etudiant:                                                       entité Absence:
composantes : Id : entier                                                            Id : entier
            Nom : chaîne composantes: Id : entier                                   hAbs : entier

L'entité Etudiant permet de mémoriser le nom et l'identifiant d'un étudiant.
L'entité Absence permet de mémoriser le nombre d'heures d'absence d'un étudiant et de son identifiant.
    ✓ Le fichier d’entités Etudiant contient les renseignements de chaque étudiant de la classe.
    ✓ Le fichier d’entités Absence contient les heures d'absence de chaque étudiant.
Les 2 fichiers sont triés par ordre croissant d’identifiants et il est impossible
que des absences soient associées à un identifiant n'apparaissant pas dans la liste des étudiants.
Rédigez en Python un programme qui permet la création de deux fichiers :"""
#1. Avec les données suivantes :
#Fichier d’Etudiants : 1/A; 2/B; 3/C; 4/D; 5/E; 6/F; 7/G; 8/H; 9/I; 10/J
#Fichier d’Absences : 1/10; 1/5; 2/3; 3/4; 3/10; 4/6; 5/2; 5/2; 7/5; 8/8
#2. D’une manière aléatoire.