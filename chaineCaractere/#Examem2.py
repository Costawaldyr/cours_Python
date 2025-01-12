#Examem2
"""Exercice 6 (question exam)
Rédigez en Python un programme qui :
1. 2. 3. 4. Défini un entier N aléatoire compris entre 4 et 16 (bornes comprises), affiche ce nombre
et demande de saisir une chaine de caractères valide. Si la chaine n’est pas valide, on
redemandera à nouveau d’introduite une nouvelle chaine de caractères lue au clavier. Et
ainsi de suite jusqu’à ce que la chaine introduite soit correcte.
La saisie ne sera validée lorsque les conditions suivantes sont remplies :
a) a. Sa taille correspondra exactement à N
b) b. La chaine contient exactement 1 caractère qui n’est pas une lettre (donc soit
un caractère spécial, soit un chiffre)
c) c. Cette chaine contient au moins une lettre en minuscule et au moins lettre en
majuscule.
Affiche le nombre de voyelles différentes présentes dans la chaine mais sans tenir compte
de la distinction entre les lettres minuscules et majuscules.
Convertit (dans la même chaine) toutes les minuscules en majuscules et toutes les
majuscules en minuscules.
Permute (dans la même chaine) les sous chaines de lettres qui sont séparées par le
caractère qui n’est pas une lettre.
6
5. Depuis la dernière chaine obtenue, créer et affiche une nouvelle chaine reprenant
l’ensemble des caractères mais en un seul exemplaire (on supprime donc les caractères
doublons, en triples, etc.) en tenant compte de la distinction entre les lettres minuscules
et majuscules.
Exemple
----------
N=10
Veuillez saisir une chaine de longueur 10, qui contient exactement 1 caractère qui n’est pas une lettre
et qui contient au moins une lettre en minuscule et au moins lettre en majuscule :
aazerteoor
Erreur. La chaine n'est pas valide :
AazeR!eooR
2) Nombre de voyelles différentes : 3
--------
3) Chaine convertie :
aAZEr!EOOr
--------
4) Permutation des sous chaines :
--------
EOOr!aAZEr
5) Nouvelle chaine sans doublons :
--------
S2 : EOr!aAZ
Notes :
Une lettre est considérée comme étant une majuscule ou une minuscule de l’alphabet (de A->Z et de
a->z).
Un caractère spécial est considéré comme un comme caractère qui n’est ni un chiffre, ni une lettre.
Une lettre est considérée comme en double peu importe sa position dans la chaine (elles ne doivent pas
obligatoirement se suivre)
Une lettre en majuscule et la même lettre en minuscule sont considérées comme 2 lettres différentes.
Les méthodes pouvant être utilisées dans cet exercice sont : len, lower, upper, find et slicing à 2
paramètres ([ : ])"""

import random
n = random.randint(4,16)
print("N = ", n)

nospecial = "azertyuiopmlkjhgfdsqwxcvbnAZERTYUIOPMLKJHGFDSQWXCVBN0123456789"
almin = "azertyuiopmlkjhgfdsqwxcvbn"
almaj = "AZERTYUIOPMLKJHGFDSQWXCVBN"
chiffre = "0123456789"
voy = "aeiouy"

valide = False
while not valide:
    chaine = input("Saisis un chaine de caracteres valide: ")
    valide = True
    if len(chaine) != n:
        valide = False
    cptmin = 0
    cptmaj = 0
    for i in range(len(chaine)):
        if nospecial.find(chaine[i]) == -1:
            valide = False
        if almaj.find(chaine[i]) != -1:
            cptmaj += 1
        if almin.find(chaine[i]) != -1:
            cptmin += 1
    if cptmaj < 1 or cptmin < 1:
        valide = False

#2 voyelle
ch2 = ""
for voyelles in chaine:
    if voyelles.lower() in voy:
        ch2 += voyelles
print("VOYELLES: ",ch2)

#3
ch3 = ""
for i in range(len(chaine)):
    if chaine[i] == chaine[i].lower():
        ch3 = ch3[:i] + chaine[i].upper() + ch3[i+1:]
    else:
        ch3 = ch3[:i] + chaine[i].lower() + ch3[i+1:]
print(ch3++++++

#4
ch4 =""
for i in range(len(chaine)):
    ch4 = chaine[i] + ch4
print("Le chaine permute", ch4)

#5
ch5 = ""
for i in chaine:
    if i not in ch5:
        ch5 += i
print("Le  chaine sans doublons", ch5)
