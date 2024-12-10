def try_combinations(test_value, numbers):
    from itertools import product
    operators = ['+', '*']
    # Generate all possible combinations of operators
    for ops in product(operators, repeat=len(numbers)-1):
        result = numbers[0]
        for i, op in enumerate(ops):
            if op == '+':
                result += numbers[i+1]
            else:  # op == '*'
                result *= numbers[i+1]
        if result == test_value:
            return True
    return False

def solve_puzzle(filename):
    total = 0
    with open(filename, 'r') as file:
        for line in file:
            # Parse each line
            test_part, numbers_part = line.strip().split(':')
            test_value = int(test_part)
            numbers = [int(x) for x in numbers_part.strip().split()]
            
            # Check if this equation can be solved
            if try_combinations(test_value, numbers):
                total += test_value
    
    return total

if __name__ == "__main__":
    result = solve_puzzle('input07.txt')
    print(f"The total calibration result is: {result}")
