def read_input(filename):
    left_list = []
    right_list = []
    
    with open(filename, 'r') as file:
        for line in file:
            # Split each line into two numbers
            left, right = line.strip().split()
            left_list.append(int(left))
            right_list.append(int(right))
    
    return left_list, right_list

def calculate_similarity_score(left_list, right_list):
    # Create a dictionary to store counts of numbers in right list
    right_counts = {}
    for num in right_list:
        right_counts[num] = right_counts.get(num, 0) + 1
    
    total_score = 0
    
    # For each number in left list, multiply by its count in right list
    for num in left_list:
        # Get count from right list (0 if number doesn't exist)
        count = right_counts.get(num, 0)
        total_score += num * count
    
    return total_score

def main():
    # Read input from file
    left_list, right_list = read_input('input01.txt')
    
    # Calculate and print the result
    result = calculate_similarity_score(left_list, right_list)
    print(f"The similarity score between the lists is: {result}")

if __name__ == "__main__":
    main()
