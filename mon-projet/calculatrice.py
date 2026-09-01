def calculer(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        if b == 0:
            return "Erreur : division par zéro"
        return a / b
    else:
        return "Opération invalide"
