class Voiture:
    """id = 0
    marque ="Marque inconnue"
    modele = "marque inconnue"
    annee = 0"""

    def __innit__(self, id = 0 ,marque = "M" ,modele = "N",annee = 0):
         self.id = id
         self.marque =marque
         self.modele = modele
         self.annee = annee
     

    def __str__(self):
        return f"voiture:{self.id}: {self.marque}{self.modele}, annee: {self.annee}"




v1 = Voiture()
print(type(v1))
print(v1)
v1.id = 5
v4 = Voiture()
v3 = Voiture(2,"audi", "A3",2024)
v2 = Voiture(1, "audi","A5",2023)
print(v1.id)
print(v1.marque)
print(v2)
print(v3)
print(v4) 
