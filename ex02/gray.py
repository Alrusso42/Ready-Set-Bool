import sys

# Fonction pour convertir un nombre en Gray Code
def gray_code(n: int) -> int:
    return n ^ (n >> 1)

# Fonction main pour tester la conversion
def main():
    # Vérifier si un argument a été fourni
    if len(sys.argv) != 2:
        print("Usage: python gray_code.py <number>")
        return

    # Récupérer le nombre depuis l'argument
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("Veuillez entrer un nombre entier valide.")
        return

    # Calculer le Gray Code
    gray = gray_code(n)

    # Afficher le résultat
    print(f"Gray Code de {n} : {gray} (en binaire : {bin(gray)[2:]})")

if __name__ == "__main__":
    main()
