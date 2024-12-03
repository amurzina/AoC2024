def read_input(filename):
    reports = []
    with open(filename, 'r') as file:
        for line in file:
            # Convert each line into a list of integers
            levels = [int(x) for x in line.strip().split()]
            reports.append(levels)
    return reports

def is_safe_report(levels):
    if len(levels) < 2:
        return True
    
    # Check first difference to determine if sequence should be increasing or decreasing
    first_diff = levels[1] - levels[0]
    if first_diff == 0:  # No change is not allowed
        return False
    
    increasing = first_diff > 0
    
    # Check each pair of adjacent numbers
    for i in range(len(levels) - 1):
        diff = levels[i + 1] - levels[i]
        
        # Check if difference is between 1 and 3 (inclusive)
        if abs(diff) < 1 or abs(diff) > 3:
            return False
        
        # Check if direction is consistent
        if (increasing and diff <= 0) or (not increasing and diff >= 0):
            return False
    
    return True

def count_safe_reports(reports):
    safe_count = 0
    for report in reports:
        if is_safe_report(report):
            safe_count += 1
    return safe_count

def main():
    # Read input from file
    reports = read_input('input02.txt')
    
    # Count and print the number of safe reports
    result = count_safe_reports(reports)
    print(f"Number of safe reports: {result}")

if __name__ == "__main__":
    main()