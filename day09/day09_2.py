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

def get_file_info(disk):
    # Get information about each file: start position, length, and spans of free space
    files = {}  # file_id -> (start_pos, length)
    current_file = None
    current_start = None
    current_length = 0
    
    # Find all files and their positions
    for pos, block in enumerate(disk):
        if block != '.':
            if current_file != block:
                if current_file is not None:
                    files[current_file] = (current_start, current_length)
                current_file = block
                current_start = pos
                current_length = 1
            else:
                current_length += 1
    
    # Add the last file if there is one
    if current_file is not None:
        files[current_file] = (current_start, current_length)
    
    return files

def find_free_space(disk, start_pos, required_length):
    # Find the leftmost span of free space that can fit the required length
    current_length = 0
    current_start = None
    
    for pos in range(start_pos):
        if disk[pos] == '.':
            if current_start is None:
                current_start = pos
            current_length += 1
            if current_length >= required_length:
                return current_start
        else:
            current_length = 0
            current_start = None
    
    return None

def compact_disk(disk):
    # Get information about all files
    files = get_file_info(disk)
    
    # Process files in order of decreasing ID
    for file_id in sorted(files.keys(), reverse=True):
        start_pos, length = files[file_id]
        
        # Find leftmost suitable free space
        new_pos = find_free_space(disk, start_pos, length)
        
        if new_pos is not None:
            # Move the entire file
            for i in range(length):
                disk[new_pos + i] = disk[start_pos + i]
                disk[start_pos + i] = '.'
    
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
    print("Expected checksum: 2858")
    return checksum == 2858

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
