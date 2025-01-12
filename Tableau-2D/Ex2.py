import random

def affich(tab):
    for i in range(len(tab)):
        print(tab[i])
    print("----------------")    


if __name__=='__main__':
    n = random.randint(1,6)
    print("N=",n)
    l = n
    c = n**2
    tab = [[0]*c for i in range(l)]
    print(tab)
    
    print("-------------les éléments de la dernière colonne sont tous égaux à N3--------------")
    
    for i in range(len(tab)):
        tab[i][c-1]=n**3
    affich(tab)
    
    print("-----------------------")
    for i in range(len(tab)):
        for j in range(len(tab[i])-2,-1,-1):
            tab[i][j]= tab[i][j+1] - (i+1)
    affich(tab)
    
    print("on rech", n*n)
    i = 0
    j = (n*n)-1
    while not(tab[i][j]==(n*n) or (i==n-1 and j==0)):
        j-=1
        if j<0:
            j = (n*n)-1
            i+=1
    if tab[i][j]==(n*n) :
        print("trouvé en ligne",i," et col",j)
    else:
        print("pas trouvé")