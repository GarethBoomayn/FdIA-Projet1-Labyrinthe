import time
from typing import List, Tuple, Set, Optional
from maze import Maze


class DFS:
    def __init__(self, maze: Maze):
        self.maze = maze
        self.explored = set()
        self.path = []
        self.execution_time = 0
    
    def search(self) -> Optional[List[Tuple[int, int]]]:
        start_time = time.time()
        
        stack = [(self.maze.start, [self.maze.start])]
        self.explored = set()
        
        while stack:
            current, path = stack.pop()
            
            if current in self.explored:
                continue
            
            self.explored.add(current)
            
            if current == self.maze.goal:
                self.path = path
                self.execution_time = (time.time() - start_time) * 1000
                return path
            
            neighbors = self.maze.get_neighbors(current)
            for neighbor in reversed(neighbors):
                if neighbor not in self.explored:
                    stack.append((neighbor, path + [neighbor]))
        
        self.execution_time = (time.time() - start_time) * 1000
        return None
    
    def get_stats(self) -> dict:
        return {
            'algorithm': 'DFS',
            'nodes_explored': len(self.explored),
            'path_length': len(self.path) if self.path else 0,
            'execution_time': self.execution_time
        }
    
    def display_exploration(self):
        print("=== DFS - Exploration ===")
        self.maze.display(explored=self.explored)
    
    def display_solution(self):
        print("=== DFS - Solution ===")
        self.maze.display(path=self.path)
    
    def display_path(self):
        if self.path:
            path_str = " -> ".join([f"{'S' if p == self.maze.start else 'G' if p == self.maze.goal else ''}{p}" for p in self.path])
            print(f"Chemin: {path_str}")
        else:
            print("Aucun chemin trouvé")
    
    def display_stats(self):
        stats = self.get_stats()
        print(f"Noeuds explorés: {stats['nodes_explored']}")
        print(f"Longueur du chemin: {stats['path_length']}")
        print(f"Temps d'exécution: {stats['execution_time']:.3f} ms")
        print()
