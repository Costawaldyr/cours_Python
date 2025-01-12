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
    no1 = [1,2,2,4,5,6,7,7,8,8,9]
    km = [1000,100,50000,16000,3500,3000,1100,4000,1900,2000]
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
    
