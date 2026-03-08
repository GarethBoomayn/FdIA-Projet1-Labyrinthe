# Devoir I - Algorithmes de Recherche dans un Labyrinthe

## Description

Ce projet implémente trois algorithmes de recherche pour résoudre le problème de navigation dans un labyrinthe :
- **DFS (Depth-First Search)** : Recherche en profondeur
- **BFS (Breadth-First Search)** : Recherche en largeur
- **A\*** : Recherche informée avec heuristique de Manhattan

## Structure du Projet

```
Devoir_I/
├── maze.py          # Génération et gestion du labyrinthe
├── dfs.py           # Implémentation de DFS
├── bfs.py           # Implémentation de BFS
├── astar.py         # Implémentation de A*
├── main.py          # Point d'entrée principal
├── requirements.txt # Dépendances
└── README.md        # Documentation
```

## Prérequis

- Python 3.11 ou supérieur

## Installation

Aucune dépendance externe n'est requise. Le projet utilise uniquement la bibliothèque standard Python.

```bash
# Vérifier la version de Python
python --version
```

## Utilisation

Pour exécuter le programme :

```bash
python main.py
```

Le programme va :
1. Générer un labyrinthe 16x16 avec une graine aléatoire (seed=42)
2. Exécuter les trois algorithmes (DFS, BFS, A*)
3. Afficher pour chaque algorithme :
   - L'exploration (cases parcourues marquées avec 'p')
   - La solution (chemin trouvé marqué avec '*')
   - Le chemin sous forme de coordonnées
   - Les statistiques (noeuds explorés, longueur du chemin, temps d'exécution)
4. Afficher un tableau comparatif des performances

## Caractéristiques du Labyrinthe

- **Taille** : 16x16
- **Symboles** :
  - `#` : Mur (obstacle)
  - `.` : Case libre
  - `S` : Point de départ (position 1,1)
  - `G` : Point d'arrivée (position 14,14)
  - `p` : Case explorée
  - `*` : Chemin solution

## Algorithmes Implémentés

### DFS (Depth-First Search)
- Utilise une pile (LIFO)
- Explore en profondeur
- Ne garantit pas le chemin optimal

### BFS (Breadth-First Search)
- Utilise une file (FIFO)
- Explore en largeur
- **Garantit le chemin le plus court**

### A* (A-Star)
- Utilise une file de priorité
- Fonction d'évaluation : f(n) = g(n) + h(n)
- Heuristique : Distance de Manhattan
- Optimal et efficace

## Résultats Attendus

Le programme affiche un tableau comparatif similaire à :

```
Algorithme           Noeuds          Longueur        Temps (ms)     
--------------------------------------------------------------------------------
DFS                  XX              XX              X.XXX
BFS                  XX              XX              X.XXX
A* (manhattan)       XX              XX              X.XXX
```

## Auteur

Projet réalisé dans le cadre du cours INF-5183 - Fondements de l'Intelligence Artificielle
Université du Québec en Outaouais (UQO)
Session : Hiver 2026

## Licence

Ce projet est réalisé à des fins éducatives.
