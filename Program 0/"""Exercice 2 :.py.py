"""Écrire un programme qui permet de vérifier si la saisie est un entier positif inférieur à 1000. Le
programme affiche « nombre accepté » si la saisie est correcte, et « nombre refusé » dans le cas
contraire. """

A = int(input("Entrez un nombre entier possitif inferieur a 1000 : "))

if A > 0 and A < 1000:
    # IF 0 < A < 1000:
    print("Nombre accepté")
else:
    print("Nombre refusé")    

"""Écrire un programme python qui permet de saisir deux entiers x et y et de vérifier ensuite si x est
divisible par y. 
"""

x = int(input("X ?"))
y = int(input("Y ?"))

if y != 0 and x % y == 0:
    print(x ,"est divisible pour", y)
else:
    print(x, "n'est pas divisible par," ,y)    

"""Soit un entier n à deux chiffres. Tester, avec un programme python, la parité de chacun des 2
chiffres de n.
Exemple : n=16-> 1 est impair et 6 est pair. """

x = int(input("x?"))
diz = x//10
unit = x%10
print ("dizaine: ",diz,end=" ")
if diz%2==0 :
    print("pair")
else : 
    print("impair")
print ("unite: ",unit,end=" ")
if unit%2==0 :
    print("pair")
else : 
    print("impair")

    #====================================
    nbr = int(input("nombre?"))
if 10<= nbr<=99:
    d = nbr//10 
    u = nbr%10 
    print("d:" , d , " / u:" , u)
    if d%2 == 0 :# si diz est pair ?
        print("diz pair")
    else :      
        print("diz impair")
    if u%2 == 0 :# si unit est pair ?
        print("unit pair")
    else :      
        print("unit impair")
else:
    print("Erreur")
       
"""
Écrire un programme python qui lit les paramètres d'une équation de premier degré ax+b=0 et
affiche la solution. Attention, il faut aussi tenir compte des éventuelles impossibilités."""
a = float(input("Entrez A :"))
b = float(input("Entrez B : "))

if a == 0:
    if b == 0:
        print("L'equation a une infinite de soluctions")
    else:
        print("L'equation n'as pas de soluction")    
else:
    x = -b / a 
    print("La soluction est ", x )        


"""Exercice 6 :
Ecrire un programme python qui permet de saisir un nombre puis déterminer s’il appartient à un
intervalle donné, sachant que les extrémités de l’intervalle sont fixées par l’utilisateur.    """
nombre = int(input("Entrez un nombre : "))
a = int(input("Entrez un nombre inferieur A"))
b = int(input("Entrez la valeur superieur b :"))

if a < nombre < b or b < nombre < a:
    print(nombre, "est dans l'intervale")
else:
    print(nombre," n'est pas dans l'intervalle")    

#2iem solution
"""
if a < b:
    bi = a 
    bs = b
else :
    bi = b
    bs = a
if (bi < nbr < bs):
    print(nbr," dans l'intervalle")
else :
    print(nbr," pas dans l'intervalle")
"""



"""Écrire un programme python qui permet de saisir deux entiers et un caractère et d’effectuer
l’opération arithmétique qui correspond à la valeur de l’opérande (‘+’, ‘*’, ‘-‘, ‘/’, ‘%’). Le code devra
afficher le résultat de l’opération ou un message d’erreur en cas de saisie d'un opérande invalide. """

a = int(input("Entrez le premier nombre : "))
b = int(input("Entrez le deuxième nombre : "))
operateur = input("Entrez l'opérateur (+, -, *, /, %) : ")
if operateur == '+':
    resultat = a + b
elif operateur == '-':
    resultat = a - b
elif operateur == '*':
    resultat = a * b
elif operateur == '/':
    if b != 0:
        resultat = a / b
    else:
        print("Erreur : Division par zéro")
        exit()
elif operateur == '%':
    if b != 0:
        resultat = a % b
    else:
        print("Erreur : Modulo par zéro")
        exit()
        
else:
    print("Opérateur invalide")
print("Le résultat de", a, operateur, b, "est", resultat)

"""Écrire un programme python qui permet de saisir deux entiers et un caractère et d’effectuer
l’opération arithmétique qui correspond à la valeur de l’opérande (‘+’, ‘*’, ‘-‘, ‘/’, ‘%’). Le code devra
afficher le résultat de l’opération ou un message d’erreur en cas de saisie d'un opérande invalide. """

a = int(input("Entrez le premier nombre : "))
b = int(input("Entrez le deuxième nombre : "))
operateur = input("Entrez l'opérateur (+, -, *, /, %) : ")

match operateur:
    case "+":
        resultat = a + b
        print("Le résultat de", a, operateur, b, "est", resultat)
    case "-":
        resultat = a - b
        print("Le résultat de", a, operateur, b, "est", resultat)
    case "*":
        resultat = a * b
        print("Le résultat de", a, operateur, b, "est", resultat)
    case "/":
        if b != 0:
            resultat = a / b
            print("Le résultat de", a, operateur, b, "est", resultat)
        else:
            print("Erreur: division par zero")    
    case "%":
        if b != 0:
            resultat = a % a 
            print("Le résultat de", a, operateur, b, "est", resultat)
        else:
            print("Erreur: modulo par zero")
    case _ : print("Operateur invalide")         
       

from random import randint
#solution 1
#nombre pair
x = 2 * randint(3, 10)
print(x)
#nombre impair
b = 2 * randint(3, 9) + 1
print(b)


# solution 2
#nombre pair
y = randint(6, 20)
while y % 2 != 0:
    y = randint(6,20)
print(y)    
#nombre impair
a = randint(6, 19)
while a % 2 == 0:
    a = randint(6,19)
print(a)  
