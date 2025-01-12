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




