                                                             
"""  EXERCICE 3  """

"""Soit le tableau à 2 dimensions suivant :
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16

Rédiger les programmes permettant d’afficher ce tableau dans l’ordre :"""


def affTab(tab):
    for i in range(len(tab)):
        print(tab[i])
l = 4
c = 4
tab = [[0]* c for i in range(l)]
cpt = 1
for i in range(len(tab)):
    for j in range(len(tab[i])):
        tab[i][j]= cpt
        cpt +=1
affTab(tab)
print("------------------------------------------")        
#a. 4,3,2,1,8,7,6,5,12,11,10,9,16,15,14,13
print("                (a)")
for i in range(len(tab)):
    for j in range(len(tab[i])-1,-1,-1):
        print(tab[i][j], end=" ")
print()        
#b. 16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1
print("------------------------------------------")
print("                (b)")
for i in range(len(tab)-1,-1,-1):
    for j in range(len(tab[i])-1,-1,-1):
        print(tab[i][j], end=" ")
print()        
#c. 1,5,9,13,2,6,10,14,3,7,11,15,4,8,12,16
print("------------------------------------------")
print("                (c)")
for j in range(len(tab[0])):
    for i in range(0,len(tab)):
        print(tab[i][j], end=" ")
print()        
#d. 16,12,8,4,15,11,7,3,14,10,6,2,13,9,5,1
print("------------------------------------------")
print("                (d)")
for j in range(len(tab[0])-1,-1,-1):
    for i in range(len(tab)-1,-1,-1):
        print(tab[i][j], end=" ")
print()        
#e. 1,2,3,4,9,10,11,12,5,6,7,8,13,14,15,16
print("------------------------------------------")
print("                (e)")
for i in range(0,len(tab),2):
    for j in range(len(tab[0])):
        print(tab[i][j], end=" ")
for i in range(1,len(tab),2):
    for j in range(len(tab[0])):
        print(tab[i][j], end=" ")
print()                

#f. 1,3,5,7,9,11,13,15 (2 possibilités : affichage des colonnes paires OU affichage du genre "damier")

#g. 1,2,3,4,6,7,8,11,12,16
#h. 13,14,10,15,11,7,16,12,8,4
#i. 1,5,2,9,6,3,13,10,7,4,14,11,8,15,12,16 (très difficile à faire)