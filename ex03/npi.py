import sys

def eval_formula(formula: str) -> bool:
    # Une pile pour stocker les valeurs booléennes
    stack = []
    
    # On parcourt chaque caractère de la chaîne (la formule)
    for c in formula:
        if c == '0':
            stack.append(False)  # 0 = False
        elif c == '1':
            stack.append(True)   # 1 = True
        elif c == '!':
            if stack:
                top = stack.pop()
                stack.append(not top)  # Négation (¬)
        elif c == '&':
            if len(stack) >= 2:
                b = stack.pop()
                a = stack.pop()
                stack.append(a and b)  # Conjonction (∧)
        elif c == '|':
            if len(stack) >= 2:
                b = stack.pop()
                a = stack.pop()
                stack.append(a or b)  # Disjonction (∨)
        elif c == 'ˆ':
            if len(stack) >= 2:
                b = stack.pop()
                a = stack.pop()
                stack.append(a != b)  # Disjonction exclusive (⊕)
        elif c == '>':
            if len(stack) >= 2:
                b = stack.pop()
                a = stack.pop()
                stack.append((not a) or b)  # Implication (⇒)
        elif c == '=':
            if len(stack) >= 2:
                b = stack.pop()
                a = stack.pop()
                stack.append(a == b)  # Équivalence logique (⇔)
        else:
            print(f"Erreur : caractère invalide '{c}'")
            return False  # Retourner False si un caractère invalide est rencontré
    
    # Le résultat final est l'élément restant dans la pile
    return stack.pop() if stack else False

# Fonction principale pour tester
if __name__ == "__main__":
    # Vérifie si un argument a été passé
    if len(sys.argv) != 2:
        print("Usage : python script.py <formula>")
        sys.exit(1)

    # L'argument de la ligne de commande (la formule en NPI)
    formula = sys.argv[1]

    # Appel de la fonction avec la formule donnée en argument
    result = eval_formula(formula)
    print(f"Résultat de l'évaluation : {result}")
