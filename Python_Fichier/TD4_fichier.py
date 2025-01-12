#exercice 2
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

 