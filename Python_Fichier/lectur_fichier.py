fich = open("nbr.dat", "r")
contenu = ""
while 1:
    ligne = fich.readline()
    if (ligne == ""):
        break
    contenu += ligne
print(contenu)
fich.close()    