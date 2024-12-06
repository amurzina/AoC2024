def read_input(filename):
    with open(filename, 'r') as f:
        lines = []
        for line in f:
            # Remove any whitespace and newlines
            clean_line = ''.join(line.strip().split())
            if clean_line:  # Only add non-empty lines
                lines.append(list(clean_line))
        return lines

def find_start_position(grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == '^':
                return (x, y)
    return None

def is_within_bounds(x, y, grid):
    return 0 <= y < len(grid) and 0 <= x < len(grid[0])

def main():
    # Directions: Up, Right, Down, Left (clockwise order)
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # (x, y)
    current_direction = 0  # Start facing up

    grid = read_input('input06.txt')
    print(f"Grid size: {len(grid)}x{len(grid[0])}")
    
    start_pos = find_start_position(grid)
    print(f"Start position: {start_pos}")
    
    if not start_pos:
        print("No starting position found!")
        return

    visited = {start_pos}  # Set to keep track of visited positions
    current_pos = start_pos
    steps = 0

    while True:
        # Get current direction vector
        dx, dy = directions[current_direction]
        next_x, next_y = current_pos[0] + dx, current_pos[1] + dy

        # Check if there's an obstacle in front or we're out of bounds
        if not is_within_bounds(next_x, next_y, grid):
            print(f"Left mapped area at position {next_x}, {next_y}")
            break
        
        if grid[next_y][next_x] == '#':
            # Turn right (clockwise)
            current_direction = (current_direction + 1) % 4
            print(f"Hit obstacle at {next_x}, {next_y}, turning right to direction {current_direction}")
        else:
            # Move forward
            current_pos = (next_x, next_y)
            visited.add(current_pos)
            steps += 1
            if steps % 1000 == 0:
                print(f"Step {steps}, current position: {current_pos}")

    print(f"Number of distinct positions visited: {len(visited)}")

if __name__ == "__main__":
    main()
