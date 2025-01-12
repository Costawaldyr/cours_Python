def aff2d(tab2d):
    for row in range(len(tab2d)):
        print(tab2d[row])
def affPascal(tab2d):
    for i in range (len(tab2d)):
        for j in range (len(tab2d[0])):
            if tab2d[i][j]!=0:
                print(tab2d[i][j],end="\t")
        print()
def affPascal2(tab2d):
    for i in range (len(tab2d)):
        for j in range (i+2):
            print(tab2d[i][j],end="\t")
        print()
#programme principal        
l, c = 5, 6
tab2d = [[0] * c for i in range(l)] # Initialisation de la matrice
tab2d[0][0] = 1
tab2d[0][1] = 1
aff2d(tab2d)
print("-------------------------------------")
for i in range(1, l): # On commence à la ligne 1
    tab2d[i][0] = 1
    for j in range(1, c):
        tab2d[i][j] = tab2d[i-1][j] + tab2d[i-1][j-1] # Calcul
aff2d(tab2d)
print("-------------------------------------")
affPascal(tab2d)
print("-------------------------------------")
affPascal2(tab2d)