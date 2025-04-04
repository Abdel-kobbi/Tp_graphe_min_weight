# Graphe Complet - Matrice 

Ce projet montre comment représenter un **graphe complet** à l’aide d’une **matrice**.

## 🔢 Matrice
### ⚙️ Matrice générée automatiquement

Le programme génère automatiquement une matrice avec des poids aléatoires :
<pre>
0	42	77	40	
42	0	30	86	
77	30	0	98	
40	86	98	0	
</pre>

Chaque case `[i][j]` représente le **poids de l’arête** entre le sommet `i` et le sommet `j`.

- La diagonale est à `0`, car la distance entre un sommet et lui-même est toujours nulle.
- La matrice est **symétrique**, car le graphe est **non orienté**.
- Tous les sommets sont connectés → il s'agit d’un **graphe complet**.
### 🌐 Caractéristiques du graphe

- Graphe **complet** : tous les sommets sont reliés entre eux.
- **Pondéré** : chaque arête possède un poids (distance ou coût).
- **Non orienté** : les connexions sont symétriques.
- **Représenté par une matrice**.


## 🧮 Objectif : trouver un arbre couvrant minimum

Le projet utilise un **algorithme** pour :

- Trouver un **ensemble d’arêtes** reliant tous les sommets
- **Minimiser le coût total**
- Éviter les **cycles** → structure d’arbre

> ✨ Résultat : un **arbre de solution** qui connecte tous les sommets avec le coût minimum, sans former de cercle.


