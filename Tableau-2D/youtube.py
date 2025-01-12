matrice=[]
for i in range(3):
    ligne=[]
    for j in range(6):
        ligne.append(0)
    matrice.append(ligne)
for l in matrice:  
    print(l)

#transpose d'une matrice

matrice=[]
matriceTranspose=[]
print('veuillez saisir les elements de la matrice : \n')
for i in range(4):
    ligne=[]
    for j in range(6):
        print('A[',i,'][',j,'] =' , end='')
        ligne.append(int(input()))
    matrice.append(ligne)
for j in range(6):
    ligne=[]
    for i in range(4):
        ligne.append(matrice[i][j])
    matriceTranspose.append(ligne)
print('La matrice est: ')
for l in matrice:
    for e in l :
        print(e,end='\t')
    print()
print('La matrice transpose est: ')
for l in matriceTranspose:
    for e in l :
        print(e,end='\t')
    print()
