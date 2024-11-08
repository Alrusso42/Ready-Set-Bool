## Notation Polonaise Inverse (NPI)

### Qu'est-ce que c'est ?
La **notation polonaise inverse (NPI)** est une manière d'écrire des expressions où les **opérateurs viennent après les opérandes**. Cela élimine le besoin de parenthèses pour définir l'ordre des opérations.

### Exemple :
- **Infixe (classique)** : `(A + B) * C`
- **NPI** : `A B + C *`

### Comment ça fonctionne ?
1. **Lire la formule de gauche à droite**.
2. **Empiler les opérandes** (valeurs `0` ou `1`).
3. **Appliquer les opérateurs** (comme `!`, `&`, `|`, etc.) sur les éléments de la pile.
4. **Le résultat final** est le seul élément restant dans la pile.

### Exemple d'évaluation :
Pour la formule `10&` :
- `1` (True) et `0` (False) sont empilés.
- L'opérateur `&` (AND) applique la conjonction : `True AND False = False`.

Résultat : `False`

### Avantages de la NPI :
- **Pas de parenthèses** nécessaires.
- **Évaluation simple** avec une pile.
- **Rapide** à évaluer par ordinateur.
