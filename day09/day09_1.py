def parse_disk_map(disk_map_str):
    # Convert string to list of integers
    numbers = [int(c) for c in disk_map_str.strip()]
    
    # Initialize disk state with files and spaces
    disk = []
    file_id = 0
    
    # Process pairs of numbers (file length, space length)
    for i in range(0, len(numbers), 2):
        # Add file blocks with current ID
        file_length = numbers[i]
        for _ in range(file_length):
            disk.append(file_id)
            
        # Add space blocks if there are any (last number might be a file length)
        if i + 1 < len(numbers):
            space_length = numbers[i + 1]
            for _ in range(space_length):
                disk.append('.')
                
        file_id += 1
    
    return disk

def disk_to_string(disk):
    return ''.join(str(x) if x != '.' else '.' for x in disk)

def find_rightmost_file(disk, start_pos=None):
    if start_pos is None:
        start_pos = len(disk) - 1
    for i in range(start_pos, -1, -1):
        if disk[i] != '.':
            return i
    return -1

def find_leftmost_space(disk, end_pos=None):
    for i in range(len(disk) if end_pos is None else end_pos):
        if disk[i] == '.':
            return i
    return -1

def compact_disk(disk):
    length = len(disk)
    last_moved_pos = length
    
    while True:
        # Find rightmost file block before the last moved position
        file_pos = find_rightmost_file(disk, last_moved_pos - 1)
        if file_pos == -1:
            break
            
        # Find leftmost free space
        space_pos = find_leftmost_space(disk, file_pos)
        if space_pos == -1:
            break
            
        # If the file is already to the left of the space, we're done
        if file_pos < space_pos:
            break
            
        # Move the file block
        disk[space_pos] = disk[file_pos]
        disk[file_pos] = '.'
        last_moved_pos = file_pos
            
    return disk

def calculate_checksum(disk):
    checksum = 0
    for pos, block in enumerate(disk):
        if block != '.':  # If it's a file block
            checksum += pos * block
    return checksum

def solve(input_file):
    # Read input
    with open(input_file) as f:
        disk_map = f.read().strip()
    
    # Parse disk map into initial state
    disk = parse_disk_map(disk_map)
    
    # Compact the disk
    compacted_disk = compact_disk(disk)
    
    # Calculate checksum
    result = calculate_checksum(compacted_disk)
    
    return result

def test_example():
    example = "2333133121414131402"
    print("\nTesting with example input:", example)
    
    disk = parse_disk_map(example)
    print("Initial state:", disk_to_string(disk))
    
    compacted = compact_disk(disk.copy())
    print("After compaction:", disk_to_string(compacted))
    
    checksum = calculate_checksum(compacted)
    print("Checksum:", checksum)
    print("Expected checksum: 1928")
    return checksum == 1928

if __name__ == "__main__":
    try:
        # First test the example
        if test_example():
            print("\nExample test passed, processing actual input...")
            result = solve("input09.txt")
            print(f"The filesystem checksum is: {result}")
        else:
            print("\nExample test failed, please fix the implementation")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
