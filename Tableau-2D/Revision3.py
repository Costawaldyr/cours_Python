#3
import random
def affichTab(tab):
    for i in range(len(tab)):
        print(tab[i])

def remplissageTableau(tab):
    for i in range(c):
        tab[l-1][i] = N**3
    for j in range(c):
        for i in range(l -2,-1,-1):
            tab[i][j] = tab[i + 1][j] - (j+1)
    return tab

def rechercheTableau(tab):
    l = N-1
    c = 0
    while not(tab[l][c]==N**2 or (c == (N**2) - 1 and l == 0)):
        l -= 1
        if l < 0:
            l = N-1
            c += 1
    if tab[l][c]==N**2:
        print('trouve en ligne',l,'et colonne',c)
    else:
        print('pas trouvee')


if __name__=='__main__':
    N = random.randint(1,8)
    print('N=',N)
    l = N
    c = N**2
    tab = [[0]*c for i in range(l)]
    remplissageTableau(tab)
    affichTab(tab)
    print('On recherche', N**2)
    rechercheTableau(tab)
