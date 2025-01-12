from random import randint
"""Exercice 0.1
Rédigez un programme qui génère une chaîne de caractères qui contient entre 10 et 19 lettres
aléatoire. Utiliser la chaine alphabet pour vous aider."""

"                            METHODE TRES IMPORTANTE POUR GENERER UNE CHAINE DE CARACTERES ALEATOIRE"

alphabet = "abcdefghijklmnopqrstuvwxyz"
n = randint(10,19)
print("Le nombre de N:",n)

ch = " "
for i in range(n):
    ch += alphabet[randint(0,25)]
    print(ch)
print("str:", ch)
print()

"""Exercice 0.2
Rédigez un programme qui génère une chaîne de caractères qui contient entre 4 et 9 lettres
aléatoire. Cette chaine devra être constituée d’une alternance entre consonnes et voyelles (en
commençant par une consonne).
Utiliser les chaines voyelle= "aeiouy" et consonne="bcdfghjklmnpqrstvwxz" pour vous aider."""

voyelles = "aeiouy"
consonne = "bcdfghjklmnpqrstvwxz"
chaine = " "
n = randint(4,9)
for i in range(n):
    if i % 2 == 0:
        chaine += consonne[randint(0,len(consonne)-1)]
    else:
        chaine += voyelles[randint(0,len(voyelles)-1)]     
print("STR:",chaine)
print()        



"""Exercice 1.1
Rédigez un programme qui demande à l’utilisateur une chaîne de caractères ch et un caractère
c. Ensuite, détermine le nombre d’occurrences de c dans ch en étant sensible à la case (Cad :
tenir compte des majuscules/minuscules). La seule fonction pouvant être utilisée dans cet exercice
est : len()
Exemple : pour ch="AMOPAZEAA", c=’A’, le caractère A apparaît 4 fois dans ch."""

ch = input("Introduire une chaine de caracteres Ex:'AMOPAZEAA': ")
c = input("Introduire un caractere (1 seule lettre) Ex:'A': ")
while len(c) != 1:
    c = input("introduire une seule lettre: ")

cpt = 0

for i in range(len(ch)):
    if ch[i] == c :
        cpt += 1
print("Le caratcteres", c, "apparait",cpt,"fois dans ",ch)    

"""Exercice 1.2
Rédigez un programme qui demande à l’utilisateur une chaîne de caractères ch et un caractère
c. Ensuite, détermine le nombre d’occurrences de c dans ch en étant insensible à la case (Cad :
SANS tenir compte de la distinction majuscules/minuscules). Les fonctions pouvant être
utilisées dans cet exercice sont : len, lower et upper
Exemple : pour ch="AmopazeaA", c=’a’, le caractère ‘a/A’ apparaît 4 fois dans ch."""
ch1 = input("introduire une chaine: ")
c1 = input("introduire un caractere: ")
while len(c1) != 1:
    c1 = input("Introduire une seule lettre:")
    
cpt = 0
for i in range(len(ch1)):
    if ch1[i]== c1.upper() or ch1[i]== c1.lower():
        cpt += 1
print("Le caractere ", c1.upper(),"/",c1.lower(),"apparait", cpt,"fois dans ch")        

"""Exercice 2
Rédiger un programme qui demande à l’utilisateur une chaîne de caractères S et un caractère C
et détermine ensuite la position de l’occurrence de C la plus à gauche dans S. Si C ne se trouve
pas dans S, la réponse est -1. Les méthodes pouvant être utilisées dans cet exercice sont : len,
lower et upper 1"""
s = input("introduire une chaine : ")
c = input("introduire un caracteres ")
while len(c) != 1:
    c = input("1 seule lettre")

pos = 0
while not (s[pos]==c or pos == len(s)-1):
#while (s[pos] !=c and pos <len(s))  
    pos += 1
if pos == len(s)-1:
    print("-1")
else:
    print("position", pos)      
#Autre solution
     
s = input("introduire une chaine : ")
c = input("introduire un caracteres ")
while len(c) != 1:
    c = input("1 seule lettre")

pos = 0
while not (s[pos]==c or pos == len(s)-1):
#while (s[pos] !=c and pos <len(s))  
    pos += 1
if s[pos]==c:
    print("position", pos)  
else:
    print("-1")      


"""Exercice 3
Rédiger un programme qui demande à l’utilisateur une chaîne de caractères S et un caractère C
et détermine ensuite la position de l’occurrence de C la plus à droite dans S. Si C ne se trouve
pas dans S, la réponse est -1. Les méthodes pouvant être utilisées dans cet exercice sont : len,lower et upper"""

s = input("introduire une chaine : ")
c = input("introduire un caracteres ")
while len(c) != 1:
    c = input("1 seule lettre")
pos = len(s)-1
while not (s[pos]==c or pos == -1):
    pos -= 1
print("position: ", pos)  

"""if pos == len(s)-1:
    print("-1")
else:
    print("position", pos) """     


"""Exercice 4.1
Rédiger un programme qui demande à l’utilisateur une chaîne de caractères S et un caractère C
et supprime ensuite dans la chaîne S la première occurrence du caractère stocké dans C. Les
méthodes pouvant être utilisées dans cet exercice sont : len, lower, upper, find et slicing ([ : :])"""

s = input("introduire une chaine : ")
c = input("introduire un caracteres ")
while len(c) != 1:
    c = input("1 seule lettre")

pos = s.find(c)
print(pos) 

s = s[:pos] + s[pos + 1 :]
print(pos)

"""Exercice 4.2
Rédiger un programme qui demande à l’utilisateur une chaîne de caractères S et un caractère C
et supprime ensuite dans la chaîne S tous les caractères identiques à celui stocké dans C. Les
méthodes pouvant être utilisées dans cet exercice sont : len, lower, upper, find et slicing ([ : :])"""
s = input("introduire une chaine : ")
c = input("introduire un caracteres ")
while len(c) != 1:
    c = input("1 seule lettre")

while s.find(c) != -1 :
    pos = s.find(c)
    print(pos)
    s = s[:pos] + s[pos + 1:]
    print(s)



"""Exercice 5
Rédigez un programme qui lit une chaîne de caractères Ch et ensuite affiche, pour chaque
caractère de Ch, la position où ce caractère est apparu pour la première fois dans Ch.
Exemple: si Ch="ABCADB", la suite 1, 2, 3, 1, 5, 2 sera affichée. En effet, le 1 er caractère
(‘A’) apparaît pour la première fois en première place. Le caractère suivant (‘B’) apparaît pour
la première fois en 2ème place. Le caractère suivant (‘C’) apparaît pour la première fois en 3ème
position. Le caractère suivant (‘A’) apparaît pour la première fois en 1ère position..."""

ch = "ABCADB"

for i in range(len(ch)-1):
    print(ch.find(ch[i]) +1, end=",")
print(ch.find(ch[len(ch)-1])+1)    
    


"""Exercice 6
Rédigez un programme qui, à partir d'une chaîne de caractères lue au clavier, détermine une
nouvelle chaîne en éliminant tous les doublons de lettre de la chaîne initiale. En clair, chaque
lettre ne peut apparaître qu'une et une seule fois et c'est l'occurrence la plus à gauche qui
subsiste.
Exemple : Si la chaîne est AZARZA, elle devient AZR (les 2ème et 3ème A ne sont pas
recopiés puisqu’un A apparaît déjà ; de même pour le 2ème Z)"""

ch = input("introduire la chaine: ")
ch1 = " "
for i in range(len(ch)):
    if ch1.find(ch[i]) == -1:
        ch1 += ch[i]
    else: #pour garde 2 copie de caracter dans la chaine
        if ch1[ch1.find(ch[i])+1:].find(ch[i]) == -1:
            ch1 += ch[i]   
print(ch1) 


"""Exercice 7
Rédigez un programme qui demande à l’utilisateur une chaîne ch de caractères et vérifie si la
chaîne ch est un palindrome (la même chaîne lue de gauche à droite ou de droite à gauche).
Exemple : RADAR, KAYAK,…"""

ch = input("Introduire une chaine : ")
ch1 = ch
print(ch1)
if ch == ch[::-1]:
    print("Chaine",ch,"est un palindrome")
else:
    print(ch," N'est pas un palindrome")

# 2eme Solution

ch = input("Introduire une chaine: ") 
ch2 =" "
for i in range(len(ch)):
    ch2=ch[i] + ch2
print(ch2)
if ch == ch2:
    print("Plindrome")
else:
    print("Pas un palindrome")     
#----------OUTRE--SOLUTION-------------
i = 0

while not (ch[i]!= ch[len(ch)-1-i] or i>len(ch)//2):
    i += 1   
if (i>len(ch)//2):
    print("Palindrome")
else:
    print("Pas un palindrome")
    
"""Exercice 8
Rédigez un programme java capable de mettre une majuscule aux premières lettres d’un nom
composé de deux mots. Par exemple NoRtH CARolIna produira la sortie North Carolina
Remarque :
Les méthodes pouvant être utilisées dans cet exercice sont : len, lower, upper, find et slicing 
([: :])"""

ch = "NoRtH CARolIna"
ch = ch.lower()
print(ch)
ch = ch[0].upper()+ch[1:]
print(ch)
pe = ch.find(" ") #pe = position espace
print(pe)
ch = ch[:pe +1] + ch[pe +1:pe+2].upper()+ch[pe+2:]
print(ch)



"""Exercice 9
Rédigez un programme capable d’entrer un nom de personne au format Prénoms Nom de
famille et de l’imprimer sous forme Nom de famille, prénom, initiale du 2ème prénom. Par
exemple : William Jefferson Clinton produira la sortie Clinton, William J.
Remarque :
([ : :])
Les méthodes pouvant être utilisées dans cet exercice sont : len, lower, upper, find et slicing"""

ch = "William Jefferson Clinton"
print(ch)

ch2 = "" #Clinton, William J.

pe = ch.find(" ")# position du premier espace
print(pe)

pe2 = ch.find(" ",pe + 1) #position du 2eme espace
print(ch.find(" ",pe + 1))
print(ch[pe2 + 1:])

ch2 += ch[pe2 + 1:] + ", " + ch[ :pe + 2] + "."
print(ch2)

#   2eme solution
ch2 = ch[ch.find(" ",ch.find(" "))]
 

"""
Exercice 10
Rédiger un programme qui demande à l'utilisateur une chaîne de caractères S et affiche le
résultat de son compactage par la méthode dite RLE (Run Length Encoding) qui prend chaque
caractère et affiche le nombre de fois où il apparaît à la suite. Ne créez pas la chaîne compactée.
Faites seulement l'affichage de chaque caractère suivi du nombre de répétitions consécutives.
Exemple: "AAAZEEEEA" sera codé: "A3Z1E4A1"
✓ A (le caractère) 3 (le nombre de répétitions consécutives)
✓ Z (le caractère) 1 (le nombre de répétitions consécutives)
✓ E (le caractère) 4 (le nombre de répétitions consécutives)
✓ A (le caractère) 1 (le nombre de répétitions consécutives)"""
#QUESTION EXAMEN
ch = "AAAZEEEEAAAA"
ch2 = ch[0] # Le premier caractère de la chaîne
cpt = 1 # pour compter les répétitions

for i in range(1, len(ch)):
    if ch2 == ch[i]:
        cpt += 1
    else:
         print(ch2,cpt, end="", sep="")
         ch2 == ch[i]
         cpt = 1
print(ch2,cpt, end="", sep="")            


"""Exercice 11
Les exercices suivants doivent servir à la programmation d’un jeu du pendu.
Exercice 11.1
Rédigez un programme qui à partir d’une chaîne de caractères S construise une chaîne de
caractères S2 où les caractères extrêmes de S (premier et dernier) sont recopiés à leur place et
où tous les autres sont remplacés par des «-»
Exemple : S=RHODODENDRON et S2=R----------N"""

#Solution sans boucle for :
s = "RHODODERNDRON"

s2 = s[0] + "-" * (len(s) - 2  )+ s[-1] #len(s)-2 c'est la taille de la chaine - 2 caracteres R et N
print(s2)

#Autre solution facille:
s2 = s[0] + "------" + s[-1]
print(s2)

#Solution avec la boucle:
s = "RHODODERNDRON"
s2 = " "
for i in range(len(s)):
    if i == 0 or i == len(s) -1 :
        s2 = s2 + s[i]
    else:
        s2 = s2 + "-" 
print(s2)      
#Autre solution Prof
s2 = s[0]
for i in range(1,len(ch)-1):
    s2 += "-"
    s2+= s[len(s)-1]
print(s2)    


"""Exercice 11.2
Rédigez un programme qui à partir des chaînes de caractères S et S2 de l’exercice précédent et
d’un caractère C, remplace dans S2 les «-» par le caractère C lorsque celui-ci se trouve à cette
position dans S.
Exemple : S=RHODODENDRON, S2=R----------N et C=D. S2 devient R--D-D---D--N"""

s = "RHODODERNDRON"
s2="R----------N"
c = input("Introduire un caractere: ")
while len(c) != 1:
    c = input("Introduire un seul caracter: ")
print("On remplace le '-' par ", c,"dans s2")

for i in range(1,len(s)-1):
    if s[i] == c:
        s2 = s2[:i] + c + s2[i + 1:]  
    print(s2)     
    

"""Exercice 11.3
En remettant les 2 exercices ensemble, nous obtenons un jeu du pendu complet.
Écrire un programme permettant de jouer au « Pendu ».3"""
def affPendu(i):
    if i==0:
        print("     -------------");
        print("      |        |  ");
        print("      |           ");
        print("      |           ");
        print("      |           ");
        print("      |           ");
        print("      |           ");
        print("      |           ");
        print("------------------");
    elif i==1:
        print("     -------------");
        print("      |        |  ");
        print("      |        @  ");
        print("      |           ");
        print("      |           ");
        print("      |           ");
        print("      |           ");
        print("      |           ");
        print("------------------");
    elif i==2:
        print("     -------------");
        print("      |        |  ");
        print("      |        @  ");
        print("      |       /|  ");
        print("      |           ");
        print("      |           ");
        print("      |           ");
        print("      |           ");
        print("------------------");
    elif i==3:
        print("     -------------");
        print("      |        |  ");
        print("      |        @  ");
        print("      |       /|\\ ");
        print("      |           ");
        print("      |           ");
        print("      |           ");
        print("      |           ");
        print("------------------");
    elif i==4:
        print("     -------------");
        print("      |        |  ");
        print("      |        @  ");
        print("      |       /|\\ ");
        print("      |       /   ");
        print("      |           ");
        print("      |           ");
        print("      |           ");
        print("------------------");
    elif i==5:
        print("     -------------");
        print("      |        |  ");
        print("      |        @  ");
        print("      |       /|\\ ");
        print("      |       / \\");
        print("      |           ");
        print("      |           ");
        print("      |           ");
        print("------------------");

if __name__ == '__main__':
    ch = "RHODODENDRON"
    ch2 = ch[0]+"-"*(len(ch)-2)+ch[-1]
    print(ch2)
    max = 5
    cpt = 0
    LettresJouees = ""
    while ch2.find("-")!=-1 and cpt<max:
        lettre = input("lettre?")
        while len(lettre)!=1 :
            lettre = input("lettre?")
        LettresJouees+=lettre 
        replace = False
        for i in range (1,len(ch)-1):
            if ch[i]==lettre : 
                ch2 = ch2[:i]+lettre+ch2[i+1:]
                replace = True
        if not replace:
            cpt+=1
            print(cpt,"essai(s) utilisé(s) sur un maximum de",max,"essais.")
        affPendu(cpt);
        print("Lettres Jouees: ",LettresJouees)            
        print(ch2)
    if cpt<max :            
       print("bravo ! Trouvé en ",cpt, "essais")         
    else : 
        print("Perdu! Il fallait trouver ",ch )

 

"""Exercice 12
Rédigez en python un programme qui convertit (dans la même chaine) toutes les minuscules
en majuscules et toutes les majuscules en minuscules.
Exercices d’auto-évaluation :
Les méthodes pouvant être utilisées dans tous les exercices sont len, lower, upper, find et
slicing ([ : :])""" #question examen

ch = input("str?")
print("chaine:",ch)
for i in range(len(ch)):
    if ch[i] == ch[i].lower():
        ch = ch[:i] + ch[i].upper()+ch[i+1:]
    else : 
        ch = ch[:i] + ch[i].lower()+ch[i+1:]
print("nouvelle chaine:",ch)




