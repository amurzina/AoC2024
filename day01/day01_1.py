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

def calculate_total_distance(left_list, right_list):
    # Sort both lists
    left_list = sorted(left_list)
    right_list = sorted(right_list)
    
    total_distance = 0
    
    # Calculate distance between corresponding numbers
    for left, right in zip(left_list, right_list):
        distance = abs(left - right)
        total_distance += distance
    
    return total_distance

def main():
    # Read input from file
    left_list, right_list = read_input('input01.txt')
    
    # Calculate and print the result
    result = calculate_total_distance(left_list, right_list)
    print(f"The total distance between the lists is: {result}")

if __name__ == "__main__":
    main()
