import random
def affichTab(tab):
    for i in range(len(tab)):
        print(tab[i])

def diagonale(tab):
    for i in range(1,N-1):
        tab[i][i] = i

def dernierLigne(tab):
    for i in range(len(tab[0])):
        tab[N-1][i] = 67
        
def dernierColonne(tab):
    for i in range(len(tab[0])-1):
        tab[i][N-1] = 27

def auDessusDiagonal(tab):
    for i in range(N):
        for j in range(i+1,N):
            if i != N-1 and j != N-1:
                tab[i][j] = random.randint(25,30)

def enDessousDiagonale(tab):
    for i in range(1,N):
        for j in range(i):
            if i != N-1 and j != N-1:
                tab[i][j] = random.randint(30,35)

def ligneCentrales(tab):
    for i in range(N):
            tab[N//2][i] = random.randint(0,N)
            tab[(N//2)-1][i] = random.randint(0,N)
    return tab

def rempliAuDessus(tab):
    for i in range((N//2)-2,-1,-1):
        for j in range(len(tab[0])):
            tab[i][j] = tab[i+1][j] + tab[i+2][j]

def rempliEnDessous(tab):
    for i in range((N//2),N):
        for j in range(len(tab)):
            tab[i][j]= tab[i-1][j] * tab[i-2][j]

if __name__=='__main__':
    N = random.randint(1,8)
    print('N=',N)
    l = N
    c = N
    tab = [[0]*c for i in range(l)]
    print("\nTable de zero")
    affichTab(tab)
    print("\nDiagonale")
    diagonale(tab)
    affichTab(tab)
    print("\nDernieR Ligne")
    dernierLigne(tab)
    affichTab(tab)
    print("\nDernier Collone")
    dernierColonne(tab)
    affichTab(tab)
    print("\nAu dessus de la diagonal")
    auDessusDiagonal(tab)
    affichTab(tab)
    print("\nEn dessous de la diagonal")
    enDessousDiagonale(tab)
    affichTab(tab)