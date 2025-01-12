sortie=""
a= int(input())
if a == "exit":
    sortie = a
b = int(input())
operation =input("Entrez une operation")


while not sortie:
    a = int(input())
    b = int(input())
    operation =input("Entrez une operation")
    match operation:
        case "+": print(a + b)
        case "-": print(a - b)
        case "*": print(a * b)
        case "/": 
            if b != 0:
                print(a / b)
            else:
                print("Erreur! Division par zero")
        case "%":
            if b != 0:
                print(a % b)
            else:
                print("Erreur! modulo par zero")
        case _:
            print("Operation inconnue")