import random

def affich(tab):
    for i in range(len(tab)):
        print(tab[i])

def remplissage_Tab(tab):
    for i in range(len(tab)):
        for j in range(len(tab[0])):
            tab[i][j]= (i+2) * (j+2)

def rech(tab,x):
    i = 0
    j = 1
    while not (tab[i][j] == x or (i == n-2 and j == n-1)):
        j += 1
        if j == n :
            i += 1
            j = i + 1
    if tab[i][j]== x :
        print(f"Trouve sur la ligne {i} et colonne {j}")
    else:
        print("Pas trouve")

if __name__=='__main__':
    
    n = random.randint(3,20)
    while not n % 2 == 1:
        n = random.randint(3,20)
    print("N :",n)
    
    print("\nMatrice initiale\n")
    tab = [[0]*n for i in range(n)]
    affich(tab)
    
    print("\nMatrice remplie\n")
    remplissage_Tab(tab)
    affich(tab)
    
    x = random.randint(0, n**2)
    print(f"\nOn recherche {x}\n")
    rech(tab,x)
    