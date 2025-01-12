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

if 



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

