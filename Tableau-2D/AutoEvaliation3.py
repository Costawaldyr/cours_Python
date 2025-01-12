from random import randint

def affich(tab):
    for i in range(len(tab)):
        print(tab[i])
        
def diagonalPrincipale(tab):
    for i in range(len(tab)):
        tab[i][i] = randint(1,11)
        
def diagonaleSecondaire(tab):
    for i in range(len(tab)):
        tab[i][c - 1 - i] = randint(-6,-2)
        
def triangleOrange(tab):
    cpt = 1
    for i in range(len(tab)):
        for j in range(len(tab[0])):
            if i < j and i + j < n-1: #remplissage en haut
                tab[i][j]=cpt
                cpt += 1
            elif i > j and i + j > n-1: # remplissage en bas
                tab[i][j]=cpt
                cpt += 1
                
def triangleBlanc(tab): #triangle blanc  a gauche
    for i in range(n):
        for j in range(n):
            if j < i and i + j < n-1:
                tab[i][j]= i
                
def triangleRouge(tab): #triangle rouge a droite
    for i in range(n):
        for j in range(n):
            if j > i and i + j > n-1:
                tab[i][j]= j
                
def rech(tab):
    i = n-1
    j = n-1
    x = 2*n
    print(f"On recherche {x}")
    while not (tab[i][j]==x or (i ==n-1 and j ==0)):
        if i % 2 == 0:
            j -= 1
            if j < 0:
                j = n - 1
                i -= 1
            else:
                j -= 1
        
if __name__ == '__main__':
    n = randint(5,10)
    print("N=",n)
    l = n
    c = n
    tab = [[0]*c for i in range(l)]
    print("\nMatrice initiale avec zero:")
    affich(tab)
    print("\nDiagonale principale:")
    diagonalPrincipale(tab)
    affich(tab)
    print("\nDiagonale secondaire:")
    diagonaleSecondaire(tab)
    affich(tab)
    print("\nTriangle orange haut et bas")
    triangleOrange(tab)
    affich(tab)
    print("\nTriangle blanc a gauche")
    triangleBlanc(tab)
    affich(tab)
    print("\nTriangle rouge a droite")
    triangleRouge(tab)
    affich(tab)