from random import randint 
def affTab(m):
    for i in range(len(m)):
        print(m[i])
    print("----------------")
    
if __name__ == '__main__':
    n = randint(1,10)*2
    print("n=",n)
    m = [[0]*n for i in range(n)]
    for j in range(len(m[0])):
        m[n//2][j]= randint(0,n)
        m[(n//2)-1][j]= randint(0,n)
    affTab(m)
    for i in range((n//2)-2,-1,-1):
        for j in range(len(m[0])):
            m[i][j]=m[i+1][j]+m[i+2][j] 
    affTab(m)        
    for i in range((n//2)+1,len(m)):
        for j in range(len(m[0])):
            m[i][j]=m[i-1][j]*m[i-2][j] 
    affTab(m)               
    x = n*n
    print("on rech ",x)
    i=n-1
    j=n-1
    while not(m[i][j]==x or (i==n-1 and j==0)):
        if j%2==1: # si impair, je monte
            i-=1
            if i<0: # si je déborde :
                i=0 # on remet a jour i pour repartir dans lautre sens
                j-=1 # on décale dune rangee vers la gauche
        else:
            i+=1 # on descend
            if i==n:# si on déborde en bas
                i=n-1 # on remet à n-1
                j-=1 # on décale d'une colonne vers la gauche
    if m[i][j]==x :
        print("trouvé en ligne",i," et col",j)
    else:
        print("pas trouvé")