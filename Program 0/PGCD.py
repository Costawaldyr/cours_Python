"""ecrire une fonction qui retourne le PGCD de deux nombres entiers positifs"""
print(""" PGCD """)
def pgcd(a,b):
    while (b > 0):
        a , b = b , a % b 
    return a     
print(pgcd(112,30))

a = int(input("Entrez en nombre:"))
b = int(input("Entrez un nombre :"))
if a < b :
    pgcd_1 = a
else:
    pgcd_1 = b
print("le pgcd de {a} et {b} est:")
while not (a % pgcd_1 == 0 and b % pgcd_1 == 0):
    pgcd_1 -= 1
print(pgcd_1)                    