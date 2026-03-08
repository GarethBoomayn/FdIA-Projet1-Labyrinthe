import time
import heapq
from typing import List, Tuple, Set, Optional, Dict
from maze import Maze


class AStar:
    def __init__(self, maze: Maze):
        self.maze = maze
        self.explored = set()
        self.path = []
        self.execution_time = 0
    
    def manhattan_distance(self, pos1: Tuple[int, int], pos2: Tuple[int, int]) -> int:
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
    
    def search(self) -> Optional[List[Tuple[int, int]]]:
        start_time = time.time()
        
        start = self.maze.start
        goal = self.maze.goal
        
        g_score: Dict[Tuple[int, int], float] = {start: 0}
        f_score: Dict[Tuple[int, int], float] = {start: self.manhattan_distance(start, goal)}
        
        came_from: Dict[Tuple[int, int], Tuple[int, int]] = {}
        
        open_set = [(f_score[start], start)]
        self.explored = set()
        
        while open_set:
            _, current = heapq.heappop(open_set)
            
            if current in self.explored:
                continue
            
            self.explored.add(current)
            
            if current == goal:
                self.path = self._reconstruct_path(came_from, current)
                self.execution_time = (time.time() - start_time) * 1000
                return self.path
            
            neighbors = self.maze.get_neighbors(current)
            for neighbor in neighbors:
                if neighbor in self.explored:
                    continue
                
                tentative_g_score = g_score[current] + 1
                
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + self.manhattan_distance(neighbor, goal)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))
        
        self.execution_time = (time.time() - start_time) * 1000
        return None
    
    def _reconstruct_path(self, came_from: Dict[Tuple[int, int], Tuple[int, int]], 
                         current: Tuple[int, int]) -> List[Tuple[int, int]]:
        path = [current]
        while current in came_from:
            current = came_from[current]
            path.append(current)
        path.reverse()
        return path
    
    def get_stats(self) -> dict:
        return {
            'algorithm': 'A* (manhattan)',
            'nodes_explored': len(self.explored),
            'path_length': len(self.path) if self.path else 0,
            'execution_time': self.execution_time
        }
    
    def display_exploration(self):
        print("=== A* - Exploration ===")
        self.maze.display(explored=self.explored)
    
    def display_solution(self):
        print("=== A* - Solution ===")
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
