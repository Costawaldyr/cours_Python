from random import randint
def afftab(tab):
    for i in range(len(tab)):
        print(tab[i])

n = randint(1,6)
while n % 2 != 0:
    n += 1

l = n
c = n*n
tab = [[0]*c for i in range(l)]
afftab(tab)
print()

for i in range(len(tab)):
    tab[i][c-1]= n*n*n
    for j in range(len(tab[0])-2,-1,-1):
        tab[i][j]=tab[i][j + 1] - (i + 1)
afftab(tab)        

print("--------------------------------Tableau remplis-----------------------------")

for j in range(len(tab[0])):
    tab[l-1][j] = n*n*n
for j in range(len(tab[0])):    
    for i in range(len(tab)-2,-1,-1):
        tab[i][j]= tab[i+1][j] - (j+1)
afftab(tab)        