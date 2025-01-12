"""AUTO Evaluation:"""

"""Exercice 1
Rédiger un programme qui demande à l’utilisateur une chaîne de caractères S et construise
une nouvelle chaîne S2 qui est la chaîne S dépouillée de tous ses caractères " " initiaux.
Exemple : " ABCDEF" devient : "ABCDEF"""
s = "  ABCDEF"
s2 = ""
ajouter = False
for i in range(len(s)):
    if s[i] != " ":
        ajouter = True
    if ajouter:
        s2 += s[i]
print(s2)    

S = input("Entrez une chaine de caracteres: ")
S2 = ""
espace = False
# --------------------------
for i in S:
    if i != " ":
        espace = True   # Active le drapeau lorsque le premier caractère non espace est trouvé
    if espace:
            S2 += i
print(S)
print(S2)      


"""Exercice 2
Rédiger un programme qui demande à l’utilisateur une chaîne de caractères S et construise
une nouvelle chaîne S2 qui est la chaîne S dépouillée de tous ses caractères " " initiaux, finaux
ainsi que tous les doublons d’espace intermédiaire.
Exemple : " C’est un EXERCICE d’auto-évaluation "
devient : "C’est un EXERCICE d’auto-évaluation """

"""Exercice 3
Rédiger un programme qui demande à l'utilisateur une chaîne de caractères S et affiche le
nombre de fois où apparaît chaque voyelle (donc pas les autres caractères : consonnes, chiffres,
caractère spéciaux) dans S. On n’affichera pas les voyelles qui ne sont pas reprises dans S.
Exemple : "ABOARBAZFGHYEREEA"
✓ A : 4
✓ E : 3
✓ O : 1
✓ Y : 1
I et U ne seront pas affichés car il n’y a pas de I ni de U dans la chaine de caractère S.
Consigne et restriction :
- Vous ne pouvez parcourir la chaine S qu’une seule fois.
- Vous pouvez créer un tableau et une chaine de caractère supplémentaire."""

"""
Exercice 4
Rédigez un programme qui, à partir d'une chaîne de caractères lue au clavier, modifie la chaîne
initiale en éliminant tous les doublons de lettre. Les caractères restants doivent être ceux qui
sont rencontrés pour la dernière fois dans cette chaine. En clair, chaque lettre ne peut apparaître
qu'une et une seule fois et c'est l'occurrence la plus à droite qui subsiste.
Exemple : Si la chaîne est AZARZA, elle devient RZA
Consigne et restriction :
- Vous ne pouvez pas créer de tableaux et/ou chaines de caractères supplémentaire."""

"""Exercice 5
Rédigez un programme capable de mettre une majuscule aux premières lettres d’un nom
composé de plusieurs mots (minimum un mot).
Par exemple: “NoRtH BRidGe of CARolIna” produira la sortie: “North Bridge Of Carolina”
Consigne et restriction :
- Vous ne pouvez pas créer de tableaux et/ou chaines de caractères supplémentaire."""