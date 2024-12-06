def read_input(filename):
    with open(filename) as f:
        return [line.strip() for line in f]

def find_start(grid):
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c == '^':
                return x, y
    return -1, -1

def get_next(x, y, grid, block=None):
    h, w = len(grid), len(grid[0])
    # Try up, down, left, right in order
    for nx, ny in [(x,y-1), (x,y+1), (x-1,y), (x+1,y)]:
        if (0 <= ny < h and 0 <= nx < w and 
            grid[ny][nx] != '#' and 
            (block is None or (nx,ny) != block)):
            return nx, ny
    return None

def find_cycle(grid, start, block=None):
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

def solve(grid):
    start = find_start(grid)
    if start == (-1, -1):
        return 0
        
    # Find natural cycle
    natural_cycle = find_cycle(grid, start)
    natural_path = set()
    
    # Build path to natural cycle
    x, y = start
    while (x, y) not in natural_cycle:
        natural_path.add((x, y))
        next_pos = get_next(x, y, grid)
        if next_pos is None:
            break
        x, y = next_pos
    
    count = 0
    h, w = len(grid), len(grid[0])
    
    # Try each possible obstruction
    for y in range(h):
        for x in range(w):
            if grid[y][x] == '.' and (x,y) != start:
                # Only try positions in the path to or in the natural cycle
                if (x,y) in natural_path or (x,y) in natural_cycle:
                    new_cycle = find_cycle(grid, start, (x,y))
                    if new_cycle and set(new_cycle) != set(natural_cycle):
                        count += 1
    
    return count

def main():
    grid = read_input('input06.txt')
    result = solve(grid)
    print(f"Number of possible obstruction positions: {result}")

if __name__ == '__main__':
    main() 