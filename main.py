from maze import Maze
from dfs import DFS
from bfs import BFS
from astar import AStar


def print_separator():
    print("=" * 80)
    print()


def display_comparison_table(algorithms):
    print("=" * 80)
    print("TABLEAU COMPARATIF DES ALGORITHMES")
    print("=" * 80)
    print(f"{'Algorithme':<20} {'Noeuds':<15} {'Longueur':<15} {'Temps (ms)':<15}")
    print("-" * 80)
    
    for algo in algorithms:
        stats = algo.get_stats()
        print(f"{stats['algorithm']:<20} {stats['nodes_explored']:<15} "
              f"{stats['path_length']:<15} {stats['execution_time']:<15.3f}")
    
    print("=" * 80)
    print()


def main():
    print("=" * 80)
    print("DEVOIR I - ALGORITHMES DE RECHERCHE DANS UN LABYRINTHE")
    print("INF-5183 - Fondements de l'Intelligence Artificielle")
    print("=" * 80)
    print()
    
    seed = 42
    print(f"Génération du labyrinthe 16x16 avec seed = {seed}")
    maze = Maze(size=16, seed=seed)
    
    print("\nLabyrinthe généré:")
    maze.display()
    print_separator()
    
    print("EXÉCUTION DES ALGORITHMES DE RECHERCHE")
    print_separator()
    
    dfs = DFS(maze)
    print("1. DFS (Depth-First Search)")
    print("-" * 80)
    dfs_path = dfs.search()
    
    if dfs_path:
        dfs.display_exploration()
        dfs.display_solution()
        dfs.display_path()
        dfs.display_stats()
    else:
        print("Aucun chemin trouvé avec DFS")
    
    print_separator()
    
    bfs = BFS(maze)
    print("2. BFS (Breadth-First Search)")
    print("-" * 80)
    bfs_path = bfs.search()
    
    if bfs_path:
        bfs.display_exploration()
        bfs.display_solution()
        bfs.display_path()
        bfs.display_stats()
    else:
        print("Aucun chemin trouvé avec BFS")
    
    print_separator()
    
    astar = AStar(maze)
    print("3. A* (A-Star avec heuristique Manhattan)")
    print("-" * 80)
    astar_path = astar.search()
    
    if astar_path:
        astar.display_exploration()
        astar.display_solution()
        astar.display_path()
        astar.display_stats()
    else:
        print("Aucun chemin trouvé avec A*")
    
    print_separator()
    
    algorithms = [dfs, bfs, astar]
    display_comparison_table(algorithms)
    
    print("\nANALYSE DES RÉSULTATS:")
    print("-" * 80)
    print("• BFS garantit le chemin le plus court")
    print("• A* explore moins de noeuds grâce à l'heuristique")
    print("• DFS peut trouver un chemin plus long mais utilise moins de mémoire")
    print("=" * 80)


if __name__ == "__main__":
    main()
