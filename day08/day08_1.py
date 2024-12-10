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

def distance(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5

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
        # For each pair of antennas with the same frequency
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                ant1 = positions[i]
                ant2 = positions[j]
                
                # Vector from ant1 to ant2
                dx = ant2[0] - ant1[0]
                dy = ant2[1] - ant1[1]
                dist = (dx*dx + dy*dy)**0.5
                if dist == 0:
                    continue
                
                # Unit vector
                ux = dx/dist
                uy = dy/dist
                
                # Check both sides of the antenna pair
                for sign in [-1, 1]:
                    # From ant1 (making ant1 twice as far)
                    x = round(ant2[0] + sign * dist * ux)
                    y = round(ant2[1] + sign * dist * uy)
                    if 0 <= x < width and 0 <= y < height:
                        point = (x, y)
                        if is_collinear(ant1, ant2, point):
                            d1 = distance(point, ant1)
                            d2 = distance(point, ant2)
                            if abs(d1/d2 - 2.0) < 1e-10:
                                antinodes.add(point)
                    
                    # From ant2 (making ant2 twice as far)
                    x = round(ant1[0] + sign * dist * ux)
                    y = round(ant1[1] + sign * dist * uy)
                    if 0 <= x < width and 0 <= y < height:
                        point = (x, y)
                        if is_collinear(ant1, ant2, point):
                            d1 = distance(point, ant1)
                            d2 = distance(point, ant2)
                            if abs(d2/d1 - 2.0) < 1e-10:
                                antinodes.add(point)

    return len(antinodes)

def main():
    grid = read_input('input08.txt')
    result = find_antinodes(grid)
    print(f"Number of unique antinode locations: {result}")

if __name__ == "__main__":
    main()
