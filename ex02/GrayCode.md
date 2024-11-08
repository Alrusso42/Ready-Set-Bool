# Conversion du Binaire en Gray Code

## Qu'est-ce que le Gray Code ?

Le **Gray Code** est un code binaire dans lequel chaque nombre successif diffère d'un seul bit par rapport au précédent. Cela permet de réduire les erreurs lors des transitions entre les nombres, ce qui est particulièrement utile dans des applications comme les encodeurs rotatifs.

## Conversion du Binaire en Gray Code

### 1. Premier bit du Gray Code
Le premier bit du Gray Code est le même que celui du nombre binaire.
- Si le nombre binaire est `n`, alors le premier bit du Gray Code est simplement `n0` (le bit le plus à gauche).

### 2. Bits suivants du Gray Code
Chaque bit suivant du Gray Code est obtenu en appliquant une opération **XOR** entre le bit courant du nombre binaire et le bit précédent du Gray Code.
- Pour le bit `i` du Gray Code, on applique la formule suivante :  
  \[
  g[i] = b[i] \oplus b[i-1]
  \]
  où `b[i]` est le bit `i` du nombre binaire et `g[i]` est le bit `i` du Gray Code.

### Exemple de conversion : `n = 5`

1. En binaire, `5` est représenté comme `0101`.
2. Le premier bit du Gray Code est simplement le premier bit du nombre binaire :  
   **`g0 = b0`**, donc `g0 = 0`.
3. Le deuxième bit est calculé avec l'opération **XOR** entre `b1` et `b0` :  
   **`g1 = b1 XOR b0`** :  
   \( g1 = 1 \oplus 0 = 1 \)
4. Le troisième bit est calculé avec l'opération **XOR** entre `b2` et `b1` :  
   **`g2 = b2 XOR b1`** :  
   \( g2 = 0 \oplus 1 = 1 \)
5. Le quatrième bit est calculé avec l'opération **XOR** entre `b3` et `b2` :  
   **`g3 = b3 XOR b2`** :  
   \( g3 = 1 \oplus 0 = 1 \)

Ainsi, le **Gray Code** pour `n = 5` (en binaire `0101`) est `0111`.

## Récapitulatif

1. **Le premier bit du Gray Code** est identique au premier bit du nombre binaire.
2. **Les bits suivants** du Gray Code sont calculés en appliquant une opération **XOR** entre chaque bit du nombre binaire et le bit précédent du Gray Code.

Cela garantit que seules des transitions d'un seul bit se produisent lors du passage d'un nombre à un autre en Gray Code.

---

## Conclusion

La conversion d'un nombre binaire en Gray Code est un processus simple mais utile, notamment pour les systèmes où il est important de minimiser les erreurs lors des transitions entre les valeurs binaires. Le Gray Code est largement utilisé dans des applications comme les encodeurs rotatifs et les systèmes de communication.

