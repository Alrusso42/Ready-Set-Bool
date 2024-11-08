def apply_de_morgan_rpn(expression):
    """Transforme une expression RPN en forme normale négative (FNN) en appliquant les lois de De Morgan."""
    stack = []
    operators = {'|': '&', '&': '|'}  # Inverser les opérateurs logiques pour la loi de De Morgan

    for token in expression:
        #print(f"Token actuel : {token}")

        if token in operators:
            # Opération logique entre les deux derniers éléments
            right = stack.pop()
            left = stack.pop()
            #print(f"Appliquer l'opérateur {token} sur {left} et {right}")
            stack.append(f"{left}{right}{token}")
            #print(f"Pile après opération {token} : {stack}")

        elif token == '!':
            # Applique la négation à chaque variable individuelle
            if stack:
                top = stack.pop()
                #print(f"Appliquer la négation sur : {top}")
                # Applique la négation à chaque lettre de l'expression
                negated_expression = ''.join(f"{ch}!" if ch.isalpha() else operators[ch] if ch in operators else ch for ch in top)
                stack.append(negated_expression)
                #print(f"Pile après la négation : {stack}")

        elif token == '>':
            # Implication : A > B devient !A | B
            right = stack.pop()
            left = stack.pop()
            #print(f"Implication : transformer {left} > {right} en {left}!{right}|")
            stack.append(f"{left}!{right}|")
            #print(f"Pile après implication : {stack}")

        elif token == '=':
            # Équivalence : A = B devient (A & B) | (!A & !B)
            right = stack.pop()
            left = stack.pop()
            #print(f"Équivalence : transformer {left} = {right} en {left}{right}&{left}!{right}!&|")
            stack.append(f"{left}{right}&{left}!{right}!&|")
            #print(f"Pile après équivalence : {stack}")

        else:
            # Ajouter les variables directement dans la pile
            stack.append(token)
            #print(f"Pile après ajout de la variable {token} : {stack}")

    # Retourne l'expression finale sous forme RPN en FNN
    #print(f"Expression finale : {stack[0]}")
    return stack[0]


def negation_normal_form(expression):
    """Applique la transformation en forme normale négative (FNN) sur une expression en notation polonaise inversée."""
    return apply_de_morgan_rpn(expression)


def main():
    # Tester les différents cas d'expressions
    print(f"{negation_normal_form('AB&!')}")  # A!B!|
    print(f"{negation_normal_form('AB|!')}")  # A!B!&
    print(f"{negation_normal_form('AB>')}")  # A!B|
    print(f"{negation_normal_form('AB=')}")  # AB&A!B!&|
    print(f"{negation_normal_form('AB|C&!')}")  # A!B!&C!|


# Appeler la fonction main pour tester les cas
if __name__ == "__main__":
    main()
