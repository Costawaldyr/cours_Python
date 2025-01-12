from random import randint

def affich(tab):
    for i in range(len(tab)):
        print(tab[i])

if __name__=='__main__':
    
    n = randint(2,20)
    while n % 2 != 0 :
        n = randint(2,20)
    print(n)
    
    tab = [[0]*n for i in range(n)]
    print("\nmatrice initial")
    affich(tab)
    
    #valeurs de 2 ligne central obtenues par randint(0,n)
    for j in range(n):
        tab[n//2][j] = randint(0,n)
        tab[(n//2)-1][j] = randint(0,n)
    print("\nmatrice centrale remplie")
    affich(tab)
    
    #valeur au dessus des lignes centrales , en sommant les valeurs des 2 element de la meme colonne et 2 lignes en dessous
    for i in range((n//2)-2,-1,-1):
        for j in range(len(tab[0])):
            tab[i][j] = tab[i+1][j] + tab[i+2][j]
    print("\nremplissage de la ligne au-dessus")
    affich(tab)
    #valeur en dessous de la ligne centrale, en multipliant  les valeurs 2elements de la meme colonne et des 2lignes de element calcule
    for i in range((n//2),len(tab)):
        for j in range(len(tab[0])):
            tab[i][j] = tab[i-1][j] * tab[i-2][j]
    print("\nremplissage de la ligne en dessous\n")
    affich(tab)
    
    #Recherche
    print("On rech", n**2)
    
    i = n-1
    j = n-1
    while not( tab[i][j] == n**2 or (i == n-1 and j == 0)):
        if j % 2 == 1: # si j est impair
            i -= 1 # je monte
            if i < 0: # si on deborde
                i = 0
                j -= 1 # passer a la colonne a gauche
        else:
            i += 1 # on descend
            if i == n:
                i = n-1 
                j -= 1
    if tab[i][j] == n**2:
        print(f"trouvee dans la  ligne {i} et colonne {j}")
    else:
        print("Pas trouve")