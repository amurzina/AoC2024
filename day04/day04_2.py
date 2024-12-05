def find_xmas_patterns(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    
    def get_diagonal_word(row, col, dr, dc):
        # Get the 3-letter word in the diagonal direction
        if not (0 <= row - dr < rows and 0 <= col - dc < cols and 
                0 <= row + dr < rows and 0 <= col + dc < cols):
            return None
        return grid[row - dr][col - dc] + grid[row][col] + grid[row + dr][col + dc]
    
    # For each potential center point
    for i in range(rows):
        for j in range(cols):
            # Must be centered on 'A'
            if grid[i][j] != 'A':
                continue
            
            # Get words in both diagonal directions
            diagonal1 = get_diagonal_word(i, j, 1, 1)   # top-left to bottom-right
            diagonal2 = get_diagonal_word(i, j, 1, -1)  # top-right to bottom-left
            
            # Skip if either diagonal is invalid
            if not diagonal1 or not diagonal2:
                continue
            
            # Check if both diagonals form valid MAS patterns (forward or backward)
            valid_mas = {'MAS', 'SAM'}
            if ((diagonal1 in valid_mas or diagonal1[::-1] in valid_mas) and
                (diagonal2 in valid_mas or diagonal2[::-1] in valid_mas)):
                count += 1
    
    return count

def main():
    # Read input from file
    with open('input04.txt', 'r') as file:
        grid = [line.strip() for line in file]
    
    # Find total occurrences of X-MAS patterns
    result = find_xmas_patterns(grid)
    print(f"Total occurrences of X-MAS patterns: {result}")

if __name__ == "__main__":
    main()
