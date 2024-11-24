from itertools import product

def evaluate_rpn(formula, assignments):
    stack = []
    for char in formula:
        if char.isalpha():  # Variable (A, B, etc.)
            stack.append(assignments[char])
        elif char == '!':  # NOT
            if len(stack) < 1:
                return False, "Error: Invalid usage of '!' operator"
            val = stack.pop()
            stack.append(not val)
        elif char == '&':  # AND
            if len(stack) < 2:
                return False, "Error: Invalid usage of '&' operator"
            val2 = stack.pop()
            val1 = stack.pop()
            stack.append(val1 and val2)
        elif char == '|':  # OR
            if len(stack) < 2:
                return False, "Error: Invalid usage of '|' operator"
            val2 = stack.pop()
            val1 = stack.pop()
            stack.append(val1 or val2)
        else:
            return False, f"Error: Invalid character in formula: {char}"

    if len(stack) != 1:
        return False, f"Error: Invalid formula, stack has more than one element: {stack}"

    return stack[0], None  # Return the result of the expression and no error

def sat(formula):
    # Vérifier que la formule contient seulement des opérateurs valides et des variables
    valid_operators = {'|', '&', '!'}
    valid_chars = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ") | valid_operators

    # Si la formule contient des caractères invalides, on retourne une erreur spécifique
    for char in formula:
        if char not in valid_chars:
            return False, f"Error: Invalid character in formula: {char}"

    # Extraire les variables (toutes les lettres majuscules)
    variables = set(char for char in formula if char.isalpha())

    # Si pas de variables présentes, la formule est invalide
    if not variables:
        return False, "Error: No variables in the formula"

    # Générer toutes les combinaisons possibles de valeurs pour les variables
    all_assignments = product([False, True], repeat=len(variables))

    # Tester chaque combinaison de valeurs
    for assignment in all_assignments:
        assignments = dict(zip(variables, assignment))
        result, error = evaluate_rpn(formula, assignments)
        if error:
            return False, error  # Return the error message if there's an issue
        if result:
            return True, None  # If the formula is satisfied for this combination, return True

    return False, "Error: No satisfying assignment found"  # If no combination satisfies the formula

# Main function to run the tests
def main():
    test_cases = [
        ("AB|", True),
        ("AB&", True),
        ("AA!&", False),
        ("AA^", False)
    ]

    for formula, expected in test_cases:
        result, error = sat(formula)
        if error:
            print(f"False, {error}")
        else:
            print(result)

# Appel de la fonction main
if __name__ == "__main__":
    main()
