
#TD3 LES ENTITÉS
"""Exercice 01 :
1. Définir la classe Voiture :
✓ Attributs :
➢ marque (chaîne de caractères) :
➢ modele (chaîne de caractères
➢ annee (entier) : l'année de fabrication de la voiture
➢ couleur (chaîne de caractères) : la couleur de la voiture (
➢ kilometrage (entier) : le kilométrage de la voiture.
✓ Méthodes :
➢ __init__(self, marque, modele, annee, couleur, kilometrage) : initialise les
attributs de la voiture.
➢ __str__(self) : affiche les informations de la voiture (marque, modèle, année,
couleur, kilométrage).
2. Créer des instances de la classe Voiture :
➢ Créez au moins deux voitures différentes avec des attributs variés.
➢ Affichez les informations de chaque voiture à l'aide de la méthode __str__(self).
➢ Ajoutez du kilométrage à la deuxième voiture à l'aide de la fonction
ajouter_kilometrage(maVoiture, km) que vous devez créer (vérifiez que km est
positif)."""
class Voiture:
    """ marque = ""
    modele = ""
    annee = 0
    kilometrage = 100"""
    def __init__(self, marque ="Audi", modele="S3", annee= 2024,couleur="Noir", kilometrage=100):
         self.marque = marque
         self.modele= modele
         self.annee= annee
         self.couleur= couleur
         self.kilometrage= kilometrage

    def __str__(self):
        return f" voiture {self.marque}, {self.modele}, annee: {self.annee}, couleur {self.couleur}, kilometrage {self.kilometrage}km"
    print(" ")

def ajouter_kilometrage(v, km):
    v = Voiture()
    if km > 0:
        v.kilometrage += km 
    else:
        print("le kilometrage ajouter doit etre positif.")       

v1 = Voiture()
v2 = Voiture("BmW","M3", 2023, "rouge", 25000)
v3 = Voiture("Tesla", "S1", 2024,"Vert", 54000)
print(v1)
print(v2)  
print(v3)  

ajouter_kilometrage(v2, -2000)
print("\nApres ajout de kilometrage:")
print(v2)

#-----------Solution avec fonction 



"""Exercice 02 :
Ecrire un programme Python pour gérer les notes d'un groupe d'étudiants. Chaque étudiant
possède les informations suivantes :
➢ Nom de l'étudiant : une chaîne de caractères représentant le nom de l'étudiant.
1
a) ➢ Liste des notes : une liste d'entiers représentant les notes obtenues par l'étudiant
dans différentes matières.
Créer une classe Etudiant qui contient les informations suivantes :
✓ Le nom de l'étudiant.
✓ Les notes obtenues dans les différentes matières.
b) Créez au moins 3 Etudiants différents avec des attributs variés (minimum 3 notes).
c) Créer une fonction qui calcule la moyenne des notes d’un étudiant grâce à une fonction
que vous allez créer.
d) Créer une fonction qui affiche les informations de tous les étudiants, y compris leur nom,
leurs notes et leur moyenne.
e) Créer une fonction qui permet de trouver et afficher l'étudiant ayant la meilleure moyenne.
f) Créer une fonction qui permet de trouver et afficher l'étudiant ayant la moins bonne
moyenne."""

class MaClass:
    nom = ""
    note = 0
    def __init__(self, nom = "", note = 0):
        self.nom = nom
        self.note = note

    def __str__(self):
        return f"{self.nom}/{self.note}" 
      


"""Exercice 03 :
1. Créer les entités suivantes :
a. « Perso » dont les composantes sont : nom (str), PV (int), ATK (int), DEF (int).
b. « Team » dont les composantes sont : nom_team (str), Player[5] (Perso).
2. Ecrire une fonction nommé « init_Perso (p) » qui initialise les composantes d’un
Personnage. Le nom par défaut est « player », les autres composantes vaudront : PV : 100 +
random(10) , ATK =10 + random(10) , DEF= 5 + random(5).
3. Ecrire une fonction nommée « fight (p1, p2) » qui calcule le nombre de dégâts qu’inflige p1
sur p2 (dégâts = ATK de p1 – DEF de p2). Les dégâts seront directement enlevés au PV de
p2 dans la fonction.
4. Ecrire une fonction nommée « PvP (p1, p2) » qui simule une bataille entre p1 et p2. Les 2
Perso attaques chacun à leur tour (avec p1 qui commence) jusqu’à ce que l’un meurt (cad
PV <=0). La fonction dira quel Perso (son nom) a gagné. La fonction peut renvoyer une
valeur (1 pour p1 et 2 pour p2) annonçant le joueur vainqueur.
5. Ecrire une fonction nommé « init_Team (t) » qui initialise les composantes d’une équipe de
5 personnages avec comme nom par défaut « team ».
6. Ecrire une fonction nommée « TvT (T1, T2) » qui simule une bataille entre les 2 équipes.
On commence par faire une fight entre les premier Perso de chaque équipe. Quand un Perso
meurt, l’équipe prend son perso suivant. Une équipe perd quand elle n’a plus de Perso vivant.
La fonction dira quelle équipe (son nom) a gagné.
7. Tester toutes les fonctions ci-dessus. Pour ce, modifiez les noms par défaut des joueurs et
des équipes."""



#Partie création de données :
"""
Exercice 1 :
Soit l’entité ‘Facture’ contenant l'identifiant et le nom du client ainsi que le
montant à payer et l'état du paiement (=1 si la facture a été payée et =0
si la facture n'a pas été payée).
entité Facture
composantes: IdC: entier
Nom: chaîne
Montant : réel
Paiement : entier
fent
Soit un fichier d'entités du type ‘Facture’. Le fichier est trié en ordre
croissant sur le champ ‘IdC’.
Rédigez en Python un programme qui contient les données suivantes :
Fichier de clients : 1/A/100/1; 1/A/300/1; 1/A/40/1; 3/D/100/0;
3/D/120/1; 3/D/80/1; 3/D/40/1; 6/M/100/0; 6/M/100/0; 9/T/120/1"""
class Facture:
    idc= 0
    nom = ""
    montant = 0.0
    paiement= 0
    def __str__(self):
        return f"{self.idc}/{self.nom}/{self.montant}/{self.paiement}"
    
if __name__ == '__main__':
    ####solution 1
    f1 = Facture()
    f1.idc = 1
    f1.nom = "A"
    f1.montant = 100
    f1.paiement = 1

    f2 = Facture()
    f2.idc = 1
    f2.nom = "A"
    f2.montant = 300
    f2.paiement = 1

    f3 = Facture()
    f3.idc = 1
    f3.nom = "A"
    f3.montant = 40
    f3.paiement = 1

    f4 = Facture()
    f4.idc = 3
    f4.nom = "D"
    f4.montant = 100
    f4.paiement = 0

    f5 = Facture()
    f5.idc = 3
    f5.nom = "D"
    f5.montant = 120
    f5.paiement = 1

    f6 = Facture()
    f6.idc = 3
    f6.nom = "D"
    f6.montant = 80
    f6.paiement = 1

    f7 = Facture()
    f7.idc = 3
    f7.nom = "D"
    f7.montant = 40
    f7.paiement = 1

    f8 = Facture()
    f8.idc = 6
    f8.nom = "M"
    f8.montant = 100
    f8.paiement = 0

    f9 = Facture()
    f9.idc = 6
    f9.nom = "M"
    f9.montant = 100
    f9.paiement = 0

    f10 = Facture()
    f10.idc = 9
    f10.nom = "T"
    f10.montant = 120
    f10.paiement = 1

    listeClient = [f1,f2,f3,f4,f5,f6,f7,f8,f9,f10]

    for Facture in listeClient:
        print(Facture)

# 2eme SOLUTION plus courte

class Facture:

    def __init__(self, idc =0, nom = "", montant = 0, paiement = 0):
        self.idc= idc
        self.nom = nom
        self.montant = montant
        self.paiement= paiement

    def __str__(self):
        return f"{self.idc}/{self.nom}/{self.montant}/{self.paiement}"
    
if __name__ == '__main__':
    ####solution 2
    f1 = Facture(1,"A",100,1)
    f2 = Facture(1,"A",300,1)
    f3 = Facture(1,"A",40,1)
    f4 = Facture(3,"D",100,0)
    f5 = Facture(3,"D",120,1)
    f6 = Facture(3,"D",80,)
    f7 = Facture(3,"D",40,1)
    f8 = Facture(6,"M",100,0)
    f9 = Facture(6,"M",100,0)
    f10 = Facture(9,"T",120,1)
    
   

    listeClient = [f1,f2,f3,f4,f5,f6,f7,f8,f9,f10]

    for Facture in listeClient:
        print(Facture)

# 3eme SOLUTION avec liste

class Facture:

    def __init__(self, idc =0, nom = "", montant = 0, paiement = 0):
        self.idc= idc
        self.nom = nom
        self.montant = montant
        self.paiement= paiement

    def __str__(self):
        return f"{self.idc}/{self.nom}/{self.montant}/{self.paiement}"
    
if __name__ == '__main__':
    #######SOLUTION 3
    idc =[1,1,1,3,3,3,3,6,6,9]
    nom =["A","A","A","D","D","D","D","M","M","T"]
    montant =[100,300,40,100,120,80,40,100,100,120]
    paiement =[1,1,1,0,1,1,1,0,0,1]

    listClient =[0]*10
    for i in range(len(idc)):
        listClient[i] = Facture(idc[i], nom[i], montant[i], paiement[i])
    for Facture in listClient:    
        print(Facture)   

# 4eme SOLUTION Aleatoire
from random import randint 
import random

class Facture:

    def __init__(self, idc =0, nom = "", montant = 0, paiement = 0):
        self.idc= idc
        self.nom = nom
        self.montant = montant
        self.paiement= paiement

    def __str__(self):
        return f"{self.idc}/{self.nom}/{self.montant}/{self.paiement}"
    
if __name__ == '__main__':
    n = randint(0,20)
    print("N =",n)

    idc = [0] * n 
    if n > 0:
        idc[0]=randint(1,2)
        for i in range(1,n):
            idc[i] = idc[i -1] + randint(0,2)
            
    montant = [0] * n
    for i in range(n):
        montant[i] = round(random.uniform(10,200)/2)

    paiement = [0] * n
    for i in range(n):
        paiement[i] = randint(0,1)

    alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"    
    nom = [0] * n
    for i in range(n):
        if idc[i] <= 26:
            nom[i] = alph[idc[i] -1]
        else:
            nom[i] = "Z"

    facttures = [0] * n
    for i in range(n):
        facttures[i] = Facture(idc[i], nom[i], montant[i], paiement[i])  
    print("Liste de facture generer:")   
    
    for Facture in facttures:    
        print(Facture)    

#-------SOLUTION AVEC FONCTION--------------------#
import random

class Facture ():
    Idc = 0
    Nom = ""
    Montant = 0.0
    Paiement = 0
    def __init__(self,Idc=0,Nom="",Montant=0.0,Paiement=0):
        self.Idc=Idc
        self.Nom=Nom
        self.Montant=Montant
        self.Paiement=Paiement
    def __str__(self):
        #return f"Idc:{self.Idc},Nom:{self.Nom},Montant:{self.Montant},Paiement:{self.Paiement}"
        return f"{self.Idc}/{self.Nom}/{self.Montant}/{self.Paiement}"

def generNom():
    nom = ""
    consonne = "bcdfghjklmnprstvwxz"
    voyelle = "aeiouy"
    n= random.randint(4,8)
    for i in range(n): 
        if i%2==0:
            nom+=consonne[random.randint(0,len(consonne)-1)]
        else:
            nom+=voyelle[random.randint(0,len(voyelle)-1)]        
    return nom

if __name__ == '__main__':

    ####### SOLUTION 3
    '''
    idc = [1,1,1,3,3,3,3,6,6,9]
    nom = ["A","A","A","D","D","D","D","M","M","T"]
    mont = [100.0,300.0,40.0,100.0,120.0,80.0,40.0,100.0,100.0,120.0]
    paiement = [1,1,1,0,1,1,1,0,0,1]
    listeClient = [0]*10
    for i in range (len(idc)):
        listeClient[i]= Facture(idc[i],nom[i],mont[i],paiement[i])
    '''
    ####### SOLUTION 4 : DATA dyn

    # Taille aléatoire N 10-20
    N = random.randint(10,20)
    print("N:",N)
    idc = [0]*N
    idc[0] = random.randint(1,3)
    for i in range(1,N):
        idc[i] = idc[i-1] + random.randint(0,2)
    #print(idc)
    mont = [0]*N
    for i in range(N):
        mont[i] = round(random.uniform(10,200),2)
    #print(mont)
    paiement = [0]*N
    for i in range(N):
        paiement[i] = random.randint(0,1)
    #print(paiement)
    nom = [""]*N
    alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#SOLUTION 1) la plus simple mais qui ne fonctionne qu'avec un N max de 26
#    for i in range(N):
#        nom[i] =  alph[idc[i]-1]
#SOLUTION 2) id de type : a->z ensuite aa,bb,...
#        for j in range(0,((idc[i]-1)//26)+1):
#            nom[i] +=  alph[(idc[i]-1)%26]
#SOLUTION 3) id de type : a->z ensuite aa,ab,...,az,ba,bb,...
        # x = idc[i]
        # while x>0: 
        #     x-=1
        #     nom[i] = alph[x%26] + nom[i] 
        #     x//=26
#SOLUTION 4) on genere des noms aleatoire qui peuvent etre identique pour des ID differents
    nom[0] = generNom()
    for i in range(1,N):
        if idc[i]==idc[i-1]:
            nom[i]=nom[i-1]
        else:
            nom[i] = generNom()   
    #print(nom)
    listeClient = [0]*N
    for i in range (len(idc)):
        listeClient[i]= Facture(idc[i],nom[i],mont[i],paiement[i])
    for fact in listeClient:
        print(fact)
   
"""Exercice 2 :
Soient l’entité ‘Client’ contenant le numéro du client et son nom et l’entité ‘Voyage’ contenant le numéro du client et le nombre total de kilomètres
parcourus.
entité Client composantes :No : entier, Nom : chaîne
fent
entité Voyage composantes : No : entier ,Km : réel
fent
Le fichier de type ‘Client’ contient les renseignements correspondant à chaque client. Le fichier de type ‘Voyage’ contient tous les enregistrements
générés à chaque nouveau voyage. Les deux fichiers sont triés en ordre croissant sur le champ ‘No’ et respectent l’ordre chronologique des voyages.
Rédigez en Python un programme qui contient les données suivantes :
Fichier de Clients : 1/A; 2/B; 4/D; 5/E; 6/F; 7/G; 8/H; 9/I
Fichier de voyages : 1/1000; 2/100; 2/5000; 4/1600; 6/3500; 7/3000; 7/1100; 8/4000; 8/1900; 9/2000"""

#EXERCICE2
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
    
def list_Client():
    no = [1,2,4,5,6,7,8,9]
    nom = ["A","B","D","E","F","G","H","I"]
    clients = [0] * len(no)
    for i in range(len(no)):
        clients[i] = Client(no[i], nom[i])
    return clients  

def affichage_list_client(clients):
    for Client in clients:
        print(Client) 



def list_Voyage():
    no1 = [1,2,2,4,6,7,7,8,8,9]
    km = [1000,100,5000,1600,3500,3000,1100,4000,1900,2000]
    voy = [0] * len(no1)
    for i in range(len(no1)):
        voy[i] = Voyage(no1[i], km[i])
    return voy    

def affichage_list_voyage(voy):
    for Voyage in voy:
        print(Voyage) 

if __name__ == '__main__':

    clients = list_Client()
    voy = list_Voyage()

    print("Liste des client (fixes):")
    affichage_list_client(clients)

    print("\nListe des voyages (fixes): ")
    affichage_list_voyage(voy)


#AUTRE SOLUTION 

#EXERCICE-2 aleatoire
import random
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



"""Exercice 3 :
Soient les entités Etudiant et Absence
entité Etudiant entité Absence
composantes : Id : entier Nom : chaîne composantes: Id : entier
hAbs : entier
fent fent
L'entité Etudiant permet de mémoriser le nom et l'identifiant d'un étudiant.
L'entité Absence permet de mémoriser le nombre d'heures d'absence d'un
étudiant et de son identifiant.
✓ Le fichier d’entités Etudiant contient les renseignements de
chaque étudiant de la classe.
✓ Le fichier d’entités Absence contient les heures d'absence de
chaque étudiant.
Les 2 fichiers sont triés par ordre croissant d’identifiants et il est impossible
que des absences soient associées à un identifiant n'apparaissant pas dans
la liste des étudiants.
Rédigez en Python un programme qui contient les données suivantes :
Fichier d’Etudiants : 1/A; 2/B; 3/C; 4/D; 5/E; 6/F; 7/G; 8/H; 9/I; 10/J
Fichier d’Absences : 1/10; 1/5; 2/3; 3/4; 3/10; 4/6; 5/2; 5/2; 7/5; 8/8"""
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


def affichage_list_Etudient( list_etudiant):
    for Etudiant in list_etudiant :
        print(Etudiant) 

def affichage_list_Absence(list_hAbs):
    for Absence in  list_hAbs:
        print(Absence) 


if __name__=='__main__':
    fichier_etudiant =  list_Etudiant()
    fichier_absence = list_Absence()
    print("Liste des Etudiant(fixes):")
    affichage_list_Etudient(fichier_etudiant)
    print("\nListe des Absence (fixes): ")
    affichage_list_Absence(fichier_absence)


#Autre solution avec de fonction genere aleatoire
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


    