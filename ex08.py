import itertools

def powerset(s):
    # Créer le powerset, d'abord les sous-ensembles de taille 0, puis 1, 2, ...
    result = []
    for r in range(len(s) + 1):
        # Pour chaque taille r, on génère toutes les combinaisons possibles
        result.extend(itertools.combinations(s, r))
    return [list(subset) for subset in result]

def main():
    # Demander à l'utilisateur de définir un set, avec une possibilité de test automatique
    user_input = input("Veuillez entrer un ensemble d'entiers (séparés par des espaces) ou appuyez sur Entrée pour utiliser un ensemble de test automatique : ")

    if user_input.strip() == "":
        # Test automatique si l'utilisateur n'entre rien
        s = [1, 2, 3]  # Exemple d'ensemble pour le test automatique
        print("Aucun ensemble fourni. Exécution du test automatique avec l'ensemble : ", s)
    else:
        # Convertir l'entrée de l'utilisateur en liste d'entiers
        try:
            s = list(map(int, user_input.split()))
        except ValueError:
            print("Erreur: Veuillez entrer uniquement des entiers.")
            return

    # Calculer le powerset de l'ensemble donné (que ce soit l'entrée de l'utilisateur ou le test automatique)
    result = powerset(s)

    # Affichage du powerset
    print("Ensemble des puissances de", s, ":")
    print(result)

# Appel de la fonction main pour exécuter le programme
if __name__ == "__main__":
    main()
