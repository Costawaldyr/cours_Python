import random

def affich(tab):
    for i in range(len(tab)):
        print(tab[i])

def remplissage_tableau(tab):
    for i in range(l):
        tab[i][c-1] = N**3
    for i in range(l):
        for j in range(c -2,-1,-1):
            tab[i][j] = tab[i][j + 1] - (i + 1) 
    return tab
def rechTableau(tab):
    l = 0
    c = N**2 - 1
    while not tab[l][c] == N**2 or (l == l-1 and c == 0):
        c -= 1
        if c < 0:
            c = N**2 - 1
            l += 1
    if tab[l][c] == N**2:
        print('trouve en ligne',l,'et colonne',c)
    else:
        print('pas trouve')



if __name__=='__main__':
    N = random.randint(1,6)
    print("N=",N)
    l = N
    c = N**2
    tab = [[0]*c for i in range(l)]
    remplissage_tableau(tab)
    affich(tab)
    print('On recherche', N**2)
    rechTableau(tab)