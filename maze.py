import random
from typing import List, Tuple, Optional


class Maze:
    def __init__(self, size: int = 16, seed: Optional[int] = None):
        self.size = size
        self.seed = seed
        if seed is not None:
            random.seed(seed)
        
        self.grid = []
        self.start = (1, 1)
        self.goal = (size - 2, size - 2)
        self.generate()
    
    def generate(self):
        self.grid = [['#' for _ in range(self.size)] for _ in range(self.size)]
        
        for i in range(1, self.size - 1):
            for j in range(1, self.size - 1):
                self.grid[i][j] = '.'
        
        self._carve_path(self.start, self.goal)
        
        for i in range(1, self.size - 1):
            for j in range(1, self.size - 1):
                if (i, j) != self.start and (i, j) != self.goal:
                    if random.random() < 0.3:
                        temp = self.grid[i][j]
                        self.grid[i][j] = '#'
                        if not self._has_path():
                            self.grid[i][j] = temp
        
        self.grid[self.start[0]][self.start[1]] = 'S'
        self.grid[self.goal[0]][self.goal[1]] = 'G'
    
    def _carve_path(self, start: Tuple[int, int], goal: Tuple[int, int]):
        current = start
        while current != goal:
            row, col = current
            goal_row, goal_col = goal
            
            if row < goal_row:
                current = (row + 1, col)
            elif col < goal_col:
                current = (row, col + 1)
            elif row > goal_row:
                current = (row - 1, col)
            elif col > goal_col:
                current = (row, col - 1)
            
            if self.grid[current[0]][current[1]] == '#':
                self.grid[current[0]][current[1]] = '.'
    
    def _has_path(self) -> bool:
        visited = set()
        stack = [self.start]
        
        while stack:
            current = stack.pop()
            if current == self.goal:
                return True
            
            if current in visited:
                continue
            
            visited.add(current)
            row, col = current
            
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_row, new_col = row + dr, col + dc
                if (0 <= new_row < self.size and 
                    0 <= new_col < self.size and 
                    self.grid[new_row][new_col] != '#' and
                    (new_row, new_col) not in visited):
                    stack.append((new_row, new_col))
        
        return False
    
    def get_neighbors(self, pos: Tuple[int, int]) -> List[Tuple[int, int]]:
        row, col = pos
        neighbors = []
        
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_row, new_col = row + dr, col + dc
            if (0 <= new_row < self.size and 
                0 <= new_col < self.size and 
                self.grid[new_row][new_col] != '#'):
                neighbors.append((new_row, new_col))
        
        return neighbors
    
    def display(self, explored: set = None, path: List[Tuple[int, int]] = None):
        display_grid = [row[:] for row in self.grid]
        
        if explored:
            for pos in explored:
                if display_grid[pos[0]][pos[1]] == '.':
                    display_grid[pos[0]][pos[1]] = 'p'
        
        if path:
            for pos in path:
                if display_grid[pos[0]][pos[1]] not in ['S', 'G']:
                    display_grid[pos[0]][pos[1]] = '*'
        
        for row in display_grid:
            print(' '.join(row))
        print()
    
    def get_grid_copy(self) -> List[List[str]]:
        return [row[:] for row in self.grid]
