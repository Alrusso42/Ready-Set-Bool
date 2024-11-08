import argparse

def adder(a, b):
    while b != 0:
        carry = a & b        # Calculer les retenues (AND)
        a = a ^ b            # Additionner sans les retenues (XOR)
        b = carry << 1       # Décaler les retenues à gauche

    return a

# Fonction principale
def main():
    # Création du parseur d'arguments
    parser = argparse.ArgumentParser(description="Addition de deux nombres naturels sans utiliser l'addition directe.")
    
    # Définir les arguments a et b
    parser.add_argument("a", type=int, help="Le premier nombre naturel")
    parser.add_argument("b", type=int, help="Le deuxième nombre naturel")
    
    # Analyser les arguments de la ligne de commande
    args = parser.parse_args()

    # Appel de la fonction adder avec a et b comme arguments
    result = adder(args.a, args.b)

    # Affichage du résultat
    print(f"La somme de {args.a} et {args.b} est {result}")

# Si ce script est exécuté directement, appeler la fonction main
if __name__ == "__main__":
    main()
