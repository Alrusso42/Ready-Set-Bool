def map(x: int, y: int) -> float:
    # La valeur maximale possible pour x et y (65535)
    max_value = 65535

    # Calculer l'indice unique pour les coordonnées (x, y)
    index = y * (max_value + 1) + x

    # La valeur maximale combinée possible (65536 * 65536 - 1)
    max_combined_value = (max_value + 1) ** 2 - 1

    # Normaliser l'indice dans l'intervalle [0, 1]
    result = index / max_combined_value

    # Retourner la valeur formatée sans notation scientifique
    return result

# Fonction principale pour tester
def main():
    x = int(input("Enter x coordinate (0-65535): "))
    y = int(input("Enter y coordinate (0-65535): "))

    # Vérifier si les coordonnées sont dans l'intervalle valide
    if 0 <= x <= 65535 and 0 <= y <= 65535:
        result = map(x, y)
        # Afficher le résultat sans notation scientifique en utilisant f-string
        print(f"Mapped value for coordinates ({x}, {y}) is: {result:.10f}")  # 10 décimales
    else:
        print("Error: Coordinates out of range!")

if __name__ == "__main__":
    main()
