import turtle

# Configuration de l'écran
window = turtle.Screen()
window.bgcolor("white")
window.title("Dessin d'une rose")

# Configuration de la tortue
rose = turtle.Turtle()
rose.shape("turtle")
rose.speed(10)  # Ajuste la vitesse (1 à 10)

# Dessin des pétales
rose.color("red")
for i in range(36):  # Nombre de pétales (36 donne une forme de rose)
    rose.circle(100, 60)  # Taille et courbure des pétales
    rose.left(100)  # Angle pour former les pétales
    rose.circle(100, 60)
    rose.left(10)  # Angle de rotation pour le pétale suivant

# Tige
rose.color("green")
rose.right(90)
rose.forward(300)

# Fermeture de la fenêtre en cliquant
window.exitonclick()

