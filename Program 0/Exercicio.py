"""Écrire un programme qui permet de :
a)Créer un tableau Tab de taille 20 et remplit ce tableau avec des entiers compris entre -20 et 20.
b)Calculer et afficher la somme et la moyenne de tous les éléments du tableau.
c)Recherche et affiche la valeur minimum et maximum parmi tous les élément du tableau.
d)Augmente de 1 tous les élément d'un tableau.Après modification, le tableau sera affiche a l'ecran.
e)D'inverser L'ordre des elements d'un tableau de N  nombres (dans une 2eme tableau.)
f) D'inverser l'ordre des element d'un tableau de N nombres (dans un meme tableau sans creer de nouveau tableau) """

from random import randint
if __name__ == '__main__':
# a)
    N = 20
    tab = [0]* N
    for i in range(len(tab)):
        tab[i] = randint(-20,20)
    print(tab)
# b)
    somme = 0
    for i in range(len(tab)):
        somme += tab[i]
        moyenne = somme / N
    print(f"La somme de tous les element du tableau est: {somme}")
    print(f"Moyenne du tableau est : {moyenne}")             
# c)
    max = 0
    min = 0
    for i in range(1,len(tab)):
        if tab[i] < tab[min]:
            min = i
        elif tab[i] > tab[max]:
            max = i
    print("Minimun est :", tab[min], "en position", min)
    print("Maximun est :", tab[max], "en position", max)    

# d)
    for i in range(len(tab)):
        tab[i] += 1
    print(tab)    
        
# e)
    tab2 =[0]* N
    for i in range(len(tab)):
        tab2[i] = tab[len(tab) -1 -i]
    print(tab2)            

# f)
    for i in range(len(tab)//2):
        tmp = tab2[i]
        tab2[i]= tab2[len(tab) -1 -i]
        tab2[len(tab) -1 -i] = tmp
    print(tab2)  

    #pour trier la table
    min_index = 0
    for i in range(len(tab2)):
        min_index = i
        for j in range(i + 1, len(tab2)):
            if tab2[j] < tab2[min_index]:
                min_index = j
        tab2[i], tab2[min_index] = tab2[min_index], tab2[i]
    print(tab2)      

