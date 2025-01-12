from random import randint 
def affTab(m):
    for i in range(len(m)):
        print(m[i])
    print("----------------")
    
if __name__ == '__main__':
    n = randint(1,8)
    print("n=",n)
    l=n
    c=n*n
    m = [[0]*c for i in range(l)]
    #print(m)
    affTab(m)

    for i in range (len(m[0])):
        m[n-1][i]=n**3
    affTab(m)
    
    for j in range (len(m[0])):
        for i in range (len(m)-2,-1,-1):
            m[i][j]=m[i+1][j] - (j+1)
    affTab(m)
    print("on rech", n*n)
    i = n-1
    j = 0
    while not(m[i][j]==(n*n) or (i==0 and j==(n*n)-1)):
        i-=1
        if i<0:
            i = n-1
            j+=1
    if m[i][j]==(n*n) :
        print("trouvé en ligne",i," et col",j)
    else:
        print("pas trouvé")