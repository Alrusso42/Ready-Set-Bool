import argparse

def multiplier(a: int, b: int) -> int:
    result = 0
    while b > 0:
        # Si le bit actuel de b est 1, on ajoute a au résultat
        if b & 1:  # Si b est impair (bit de poids faible est 1)
            result = result + a  # Ajout de a à result
            
        # Décaler a à gauche pour le prochain bit de b
        a = a << 1  # Equivalent à multiplier a par 2
        
        # Décaler b à droite pour passer au prochain bit
        b = b >> 1  # Diviser b par 2 (on passe au bit suivant)
        
    return result

def main():
    # Créer un parser pour les arguments en ligne de commande
    parser = argparse.ArgumentParser(description="Multiplier deux nombres entiers en utilisant des opérations bit à bit.")
    
    # Ajouter les arguments pour a et b
    parser.add_argument('a', type=int, help="Le premier nombre à multiplier")
    parser.add_argument('b', type=int, help="Le deuxième nombre à multiplier")
    
    # Parser les arguments
    args = parser.parse_args()
    
    # Appeler la fonction multiplier avec les arguments
    result = multiplier(args.a, args.b)
    
    # Afficher le résultat
    print(f"Multiplication de {args.a} et {args.b} donne : {result}")

if __name__ == "__main__":
    main()
