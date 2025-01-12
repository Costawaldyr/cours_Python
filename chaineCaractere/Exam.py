"""Exercice 13                             
                                                        (QUESTION EXAM)
Rédigez un programme qui :
1. Défini un entier N aléatoire compris entre 6 et 14 (bornes comprises), affiche ce nombre
et demande de saisir une chaine de caractères valide. Si la chaine n’est pas valide, on
redemandera à nouveau d’introduite une nouvelle chaine de caractères lue au clavier. Et
ainsi de suite jusqu’à ce que la chaine introduite soit correcte.
La saisie ne sera validée lorsque les conditions suivantes sont remplies :
    a) Sa taille correspondra exactement à N
    b) La chaine ne contient aucun caractère spécial
    c) Cette chaine contient au moins une lettre en minuscule et au moins lettre en
       majuscule.
Affiche le nombre d’occurrences des lettres présentes dans la chaine mais sans tenir
compte de la distinction entre les lettres minuscules et majuscules.
Affiche le nombre caractères (lettres et chiffres) différents présents dans la chaine.
Déplace (dans la même chaine) les éventuels chiffres en début de chaine.
Depuis la chaine de base, créer et affiche une nouvelle chaine reprenant l’ensemble des
caractères regroupés par caractère identique.
2. 3. 4. 5. Exemple
--------
N=10
Veuillez saisir une chaine de longueur 10, sans caractère spécial et qui contient au moins une lettre en
minuscule et au moins lettre en majuscule :
aazerteoor

Erreur. La chaine n'est pas valide :
Aazer9eoor

2) Nombre d'occurrences
--------
Il y a 2 occurrence(s) de la lettre : a-A
Il y a 1 occurrence(s) de la lettre : z-Z
Il y a 2 occurrence(s) de la lettre : e-E
Il y a 2 occurrence(s) de la lettre : r-R
Il y a 2 occurrence(s) de la lettre : o-O

3) Nombre de caractères différents
--------
Il y a 7 caractères différents

4) Déplacement des éventuels chiffres
--------
9Aazereoor

5) Regroupement par caractère identique
4
--------
9Aazeerroo

Notes :
Une lettre est considérée comme étant une majuscule ou une minuscule de l’alphabet (de A->Z et de
a->z).
Un caractère spécial est considéré comme un comme caractère qui n’est ni un chiffre, ni une lettre.
Une lettre est considérée comme en double peu importe sa position dans la chaine (elles ne doivent pas
obligatoirement se suivre)
Une lettre en majuscule et la même lettre en minuscule sont considérées comme 2 lettres différentes
(sauf pour le point 2).
Les méthodes pouvant être utilisées dans cet exercice sont : len, lower, upper, find et slicing à 2
paramètres ([ : ])"""

if __name__ == '__main__':
    n = randint(6,14)
    nospecial = "azertyuiopmlkjhgfdsqwxcvbnAZERTYUIOPMLKJHGFDSQWXCVBN0123456789"
    almin = "azertyuiopmlkjhgfdsqwxcvbn"
    almaj = "AZERTYUIOPMLKJHGFDSQWXCVBN"
    chiffre = "0123456789"
    print("N:",n)
    # 1)
    valide = False
    while not valide :
        ch = input(f"Veuillez saisir une chaine de taille {n}, sans caractère spécial et qui contient au moins une lettre en minuscule et au moins lettre en majuscule")
        valide = True
        if len(ch) != n:
            valide = False
        cptmin = 0
        cptmaj = 0
        for i in range (len(ch)):
            if nospecial.find(ch[i]) ==-1 :
                valide = False
            if almin.find(ch[i]) !=-1 :    
                cptmin+=1
            if almaj.find(ch[i]) !=-1 :    
                cptmaj+=1
        if cptmin<1 or cptmaj<1 :
            valide = False
    # 2)
    for i in range(len(ch)):
        cpt = 1
        if ch.lower().find(ch[i].lower())==i and chiffre.find(ch[i])==-1 :
            for j in range(i+1,len(ch)): 
                if ch[j].lower()==ch[i].lower():        
                    cpt+=1
            print("Il y a",cpt,"occurrence(s) de la lettre :"
                  ,ch[i].lower(),ch[i].upper())        
    # 3)
    cpt = 0
    for i in range(len(ch)):    
        if ch.find(ch[i])==i :  # est ce que c'est la 1er fois que je rencontre cette lettre
            cpt+=1 
    print("Il y a",cpt,"caractères différents")
    # 4)
    for i in range(len(ch)):
        if chiffre.find(ch[i])!=-1 : # si c'est un chiffre
            ch = ch[i]+ch[:i]+ch[i+1:]
    print(ch)
    # 5)
    ch2 =""
    for i in range(len(ch)):
        pos = ch2.find(ch[i])       # pos de la lettre en cours dans ch2
        if pos==-1 :                # si la lettre n'est pas dans ch2
            ch2+=ch[i]              # on l'ajoute
        else:                       # sinon, on l'intercale dans ch2
            ch2 = ch2[:pos]+ch[i]+ch2[pos:]
    print("nouvelle chaine:",ch2)        
              