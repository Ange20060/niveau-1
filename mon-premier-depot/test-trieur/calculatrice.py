def calculer(a, b, operation):
    if operation == "+":
        return a + b

    elif operation == "-":
        return a - b

    elif operation == "*":
        return a * b

    elif operation == "/":
        if b == 0:
            return "Erreur : division par zéro impossible."
        return a / b

    else:
        return "Erreur : opération inconnue."


while True:
    print("\n--- Calculatrice ---")
    print("Tape q pour quitter.")

    premier = input("Premier nombre : ")

    if premier.lower() == "q":
        break

    deuxieme = input("Deuxième nombre : ")

    if deuxieme.lower() == "q":
        break

    operation = input("Opération (+, -, *, /) : ")

    if operation.lower() == "q":
        break

    a = float(premier)
    b = float(deuxieme)

    resultat = calculer(a, b, operation)

    print("Résultat :", resultat)
