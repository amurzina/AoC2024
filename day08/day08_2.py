def read_input(filename):
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]

def find_antennas(grid):
    antennas = {}  # frequency -> list of (x, y) coordinates
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] != '.':
                freq = grid[y][x]
                if freq not in antennas:
                    antennas[freq] = []
                antennas[freq].append((x, y))
    return antennas

def is_collinear(p1, p2, p3):
    # Check if three points are collinear using cross product
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return abs((y2 - y1) * (x3 - x1) - (y3 - y1) * (x2 - x1)) < 1e-10

def find_antinodes(grid):
    antennas = find_antennas(grid)
    antinodes = set()
    height = len(grid)
    width = len(grid[0])
    
    # For each frequency
    for freq, positions in antennas.items():
        if len(positions) < 2:  # Skip frequencies with only one antenna
            continue
            
        # For each point in the grid
        for y in range(height):
            for x in range(width):
                point = (x, y)
                # For each pair of antennas of the same frequency
                for i in range(len(positions)):
                    for j in range(i + 1, len(positions)):
                        ant1 = positions[i]
                        ant2 = positions[j]
                        # If the point is collinear with any pair of antennas, it's an antinode
                        if is_collinear(point, ant1, ant2):
                            antinodes.add(point)

    return len(antinodes)

def main():
    grid = read_input('input08.txt')
    result = find_antinodes(grid)
    print(f"Number of unique antinode locations: {result}")

if __name__ == "__main__":
    main()
