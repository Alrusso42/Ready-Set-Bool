def reverse_map(n: float) -> tuple:
    # La valeur maximale possible de l'indice
    max_index = 65536 * 65536 - 1

    # Vérifier que n est bien dans l'intervalle [0, 1]
    if not (0 <= n <= 1):
        print("Error: n is out of range.")
        return None

    # Calculer l'indice à partir de n
    index = int(n * max_index)

    # Décomposer l'indice en x et y
    x = index % 65536
    y = index // 65536

    return (x, y)

# Fonction principale pour tester
def main():
    test_values = [
        0.0,  # Cas de test avec la valeur minimale
        1.0,  # Cas de test avec la valeur maximale
        0.5,  # Cas de test avec une valeur intermédiaire
        0.25, # Autre cas de test
        0.75  # Autre cas de test
    ]

    for n in test_values:
        result = reverse_map(n)
        if result is not None:
            print(f"reverse_map({n}) = {result}")

if __name__ == "__main__":
    main()
