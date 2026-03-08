# Algorithmes de Recherche - Labyrinthe

Implémentation de DFS, BFS et A* pour trouver un chemin dans un labyrinthe 16x16.

## Utilisation

```bash
python main.py
```

Le programme génère un labyrinthe et compare les performances des trois algorithmes.

## Structure

```
├── maze.py          # Génération du labyrinthe
├── dfs.py           # DFS
├── bfs.py           # BFS
├── astar.py         # A* avec heuristique Manhattan
└── main.py          # Programme principal
```

## Algorithmes

- **DFS** : Recherche en profondeur (pile)
- **BFS** : Recherche en largeur (file) - chemin optimal
- **A*** : Recherche informée avec f(n) = g(n) + h(n)

## Symboles

- `#` : Mur
- `.` : Case libre
- `S` : Départ (1,1)
- `G` : Arrivée (14,14)
- `p` : Case explorée
- `*` : Chemin trouvé

---

INF-5183 - UQO - Hiver 2026
