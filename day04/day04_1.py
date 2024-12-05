def find_xmas_occurrences(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    
    # Define all possible directions (horizontal, vertical, diagonal)
    directions = [
        (0, 1),   # right
        (1, 0),   # down
        (1, 1),   # diagonal down-right
        (-1, 1),  # diagonal up-right
        (0, -1),  # left
        (-1, 0),  # up
        (-1, -1), # diagonal up-left
        (1, -1)   # diagonal down-left
    ]
    
    def check_word(row, col, dx, dy):
        if not (0 <= row + 3*dx < rows and 0 <= col + 3*dy < cols):
            return False
        word = ''
        for i in range(4):
            word += grid[row + i*dx][col + i*dy]
        return word == 'XMAS'
    
    # Check each starting position
    for i in range(rows):
        for j in range(cols):
            # Try each direction
            for dx, dy in directions:
                if check_word(i, j, dx, dy):
                    count += 1
    
    return count

def main():
    # Read input from file
    with open('input04.txt', 'r') as file:
        grid = [line.strip() for line in file]
    
    # Find total occurrences of XMAS
    result = find_xmas_occurrences(grid)
    print(f"Total occurrences of XMAS: {result}")

if __name__ == "__main__":
    main()
