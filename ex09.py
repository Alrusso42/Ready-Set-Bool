def eval_set(formula, sets):
    stack = []

    for char in formula:
        if char.isalpha():  # Si c'est une lettre (A à Z), on récupère le set correspondant
            index = ord(char) - ord('A')
            if index < 0 or index >= len(sets):
                raise ValueError(f"Invalid set reference: {char}")
            stack.append(sets[index])
        elif char == '!':  # Négation (complément)
            set_to_negate = stack.pop()
            all_elements = set(x for s in sets for x in s)  # Union de tous les sets
            stack.append(all_elements - set_to_negate)
        elif char == '&':  # Conjonction (intersection)
            set2 = stack.pop()
            set1 = stack.pop()
            stack.append(set1 & set2)
        elif char == '|':  # Disjonction (union)
            set2 = stack.pop()
            set1 = stack.pop()
            stack.append(set1 | set2)
        elif char == 'ˆ':  # Disjonction exclusive (différence symétrique)
            set2 = stack.pop()
            set1 = stack.pop()
            stack.append(set1 ^ set2)
        elif char == '>':  # Condition matérielle (implication)
            set2 = stack.pop()
            set1 = stack.pop()
            stack.append(set1 - set2)  # On considère "A > B" comme "A - B"
        elif char == '=':  # Équivalence logique (égalité des sets)
            set2 = stack.pop()
            set1 = stack.pop()
            stack.append(set1 if set1 == set2 else set())
        else:
            raise ValueError(f"Invalid operator in formula: {char}")

    if len(stack) != 1:
        raise ValueError(f"Invalid formula, stack has more than one element: {stack}")

    return list(stack[0])

def main():
    # Cas de test automatiques
    sets1 = [
        {0, 1, 2},  # A
        {0, 3, 4},  # B
    ]
    print("Result of 'AB&':", eval_set("AB&", sets1))  # [0]

    sets2 = [
        {0, 1, 2},  # A
        {3, 4, 5},  # B
    ]
    print("Result of 'AB|':", eval_set("AB|", sets2))  # [0, 1, 2, 3, 4, 5]

    sets3 = [
        {0, 1, 2},  # A
    ]
    print("Result of 'A!':", eval_set("A!", sets3))  # []

    # Demander à l'utilisateur de définir ses propres sets
    sets_input = []
    num_sets = int(input("How many sets do you want to provide? "))

    for i in range(num_sets):
        set_input = input(f"Enter set {i+1} as a space-separated list of numbers: ")
        sets_input.append(set(map(int, set_input.split())))

    formula_input = input("Enter a propositional formula in reverse polish notation (RPN): ")
    try:
        result = eval_set(formula_input, sets_input)
        print("Result of your formula:", result)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
