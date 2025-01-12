import pickle

class Eleve:
    def __init__(self, Id, Nom, Note):
        self.Id = Id
        self.Nom = Nom
        self.Note = Note

    def __str__(self):
        return f"{self.Id}/{self.Nom}/{self.Note}"

def creer_fichier_eleves(eleves, fichier):
    with open(fichier, "wb") as file:
        for eleve in eleves:
            pickle.dump(eleve, file)

def lire_fichier_eleves_sequentiellement(fichier):
    with open(fichier, "rb") as file:
        if not file.peek(1):
            print("Fichier vide !")
        else:
            # 1 declarer les var de trav
            totNotes = 0
            nbrNotes = 0
            totalEleves = 0
            elevesAuDessusDe10 = 0
            eleveEnCours = pickle.load(file)
            NoteEnCours = eleveEnCours
            # 2 on parcour le fichier
            while NoteEnCours is not None:
                if NoteEnCours.Id == eleveEnCours.Id : # op a chaque note
                    totNotes += NoteEnCours.Note
                    nbrNotes += 1 
                    # maj du enCours
                    if file.peek(1):
                        NoteEnCours = pickle.load(file)  
                    else:
                        NoteEnCours = None  
                else:  # on cloture l'eleve precedent
                    moyenne = totNotes / nbrNotes
                    print(f"L'élève {eleveEnCours.Nom} a une moyenne de {moyenne:.2f}")
                    if moyenne > 10:
                        elevesAuDessusDe10 += 1
                    totalEleves +=1
                    # remise a 0 des var de travail et maj du enCours
                    totNotes = 0
                    nbrNotes = 0
                    eleveEnCours = NoteEnCours
            # 3) post traitement == la derniere cloture
            moyenne = totNotes / nbrNotes
            print(f"L'élève {eleveEnCours.Nom} a une moyenne de {moyenne:.2f}")
            if moyenne > 10:
                elevesAuDessusDe10 += 1
            totalEleves +=1
            # 4) aff des res finaux       
            print(f"Nombre total d'élèves : {totalEleves}")
            print(f"Nombre d'élèves avec plus de 10 de moyenne : {elevesAuDessusDe10}")

if __name__ == "__main__":
    eleves = [
        Eleve(1, "A", 10),
        Eleve(1, "A", 15),
        Eleve(1, "A", 6),
        Eleve(2, "B", 16),
        Eleve(2, "B", 11),
        Eleve(3, "C", 3),
        Eleve(5, "E", 11),
        Eleve(8, "H", 14),
        Eleve(8, "H", 19),
        Eleve(9, "I", 20)
    ]
    
    fichier = "eleves.pkl"
    print("Création du fichier d'élèves...")
    creer_fichier_eleves(eleves, fichier)
    print("Fichier créé avec succès.\n")

    print("Lecture du fichier d'élèves...")
    lire_fichier_eleves_sequentiellement(fichier)
    print("\nLecture terminée.")
