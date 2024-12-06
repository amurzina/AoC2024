from typing import List, Tuple, Set

def read_input(filename: str) -> List[str]:
    with open(filename, 'r') as f:
        return [line.strip() for line in f.readlines()]

def find_start(grid: List[str]) -> Tuple[int, int]:
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == '^':
                return (x, y)
    return (-1, -1)

def get_next(x: int, y: int, grid: List[str], block: Tuple[int, int] = None) -> Tuple[int, int]:
    h, w = len(grid), len(grid[0])
    # Try up, down, left, right in order
    for nx, ny in [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]:
        if (0 <= ny < h and 0 <= nx < w and 
            grid[ny][nx] != '#' and 
            (block is None or (nx, ny) != block)):
            return nx, ny
    return None

def find_cycle(grid: List[str], start: Tuple[int, int], block: Tuple[int, int] = None) -> List[Tuple[int, int]]:
    x, y = start
    path = []
    seen = set()
    
    while True:
        pos = (x, y)
        path.append(pos)
        
        if pos in seen:
            cycle_start = path.index(pos)
            return path[cycle_start:]
        
        seen.add(pos)
        next_pos = get_next(x, y, grid, block)
        
        if next_pos is None:
            return []
            
        x, y = next_pos
    
    return []

def get_path_to_cycle(grid: List[str], start: Tuple[int, int], cycle: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    path = []
    x, y = start
    cycle_set = set(cycle)
    
    while (x, y) not in cycle_set:
        path.append((x, y))
        next_pos = get_next(x, y, grid)
        if next_pos is None:
            break
        x, y = next_pos
    
    return path

def solve(grid: List[str]) -> int:
    start = find_start(grid)
    if start == (-1, -1):
        return 0
        
    # Find natural cycle
    natural_cycle = find_cycle(grid, start)
    if not natural_cycle:
        return 0
        
    # Get path to natural cycle
    path_to_cycle = get_path_to_cycle(grid, start, natural_cycle)
    
    count = 0
    h, w = len(grid), len(grid[0])
    
    # Try each possible obstruction
    for y in range(h):
        for x in range(w):
            if grid[y][x] == '.' and (x, y) != start:
                # Only try positions in the path to or in the natural cycle
                if (x, y) in path_to_cycle or (x, y) in natural_cycle:
                    # Try placing obstruction
                    new_cycle = find_cycle(grid, start, (x, y))
                    # Check if it creates a different cycle
                    if new_cycle and set(new_cycle) != set(natural_cycle):
                        # Verify the new cycle is caused by the obstruction
                        if (x, y) in path_to_cycle or any(pos in natural_cycle for pos in new_cycle):
                            count += 1
    
    return count

def main():
    grid = read_input('input06.txt')
    result = solve(grid)
    print(f"Number of possible obstruction positions: {result}")

if __name__ == "__main__":
    main() 