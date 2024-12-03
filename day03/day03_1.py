import re

def process_memory(text):
    # Find all valid mul(X,Y) instructions where X and Y are 1-3 digit numbers
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    matches = re.finditer(pattern, text)
    
    total = 0
    for match in matches:
        x, y = map(int, match.groups())
        result = x * y
        total += result
    
    return total

def main():
    with open('input03.txt', 'r') as file:
        memory = file.read()
    
    result = process_memory(memory)
    print(f"Sum of all multiplication results: {result}")

if __name__ == "__main__":
    main()
