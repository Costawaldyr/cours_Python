from random import randint 
def affTab(m):
    for i in range(len(m)):
        print(m[i])
    print("----------------")
    
if __name__ == '__main__':
    n = (randint(1,9)*2)+1
    print("n=",n)
    m = [[0]*n for i in range(n)]
    #print(m)
    affTab(m)

    for i in range (len(m)):
        for j in range (len(m[0])):
            m[i][j]= (i+2)*(j+2)
    affTab(m)
    x = randint(0,n*n)
    print("on rech", x)
    i = 0
    j = 1
    while not(m[i][j]==x or (i==n-2 and j==n-1)):
        j+=1
        if j==n:
            i+=1
            j=i+1
    if m[i][j]==x :
        print("trouvé en ligne",i," et col",j)
    else:
        print("pas trouvé")