import re

def process_memory(text):
    # Pattern for all types of instructions
    mul_pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    do_pattern = r'do\(\)'
    dont_pattern = r'don\'t\(\)'
    
    # Find all instructions with their positions
    instructions = []
    
    # Find multiplication instructions
    for match in re.finditer(mul_pattern, text):
        instructions.append(('mul', match.start(), match.groups()))
    
    # Find do() instructions
    for match in re.finditer(do_pattern, text):
        instructions.append(('do', match.start(), None))
    
    # Find don't() instructions
    for match in re.finditer(dont_pattern, text):
        instructions.append(('dont', match.start(), None))
    
    # Sort instructions by their position in text
    instructions.sort(key=lambda x: x[1])
    
    total = 0
    enabled = True  # Multiplications are enabled at the start
    
    # Process instructions in order
    for inst_type, _, args in instructions:
        if inst_type == 'do':
            enabled = True
        elif inst_type == 'dont':
            enabled = False
        elif inst_type == 'mul' and enabled:
            x, y = map(int, args)
            total += x * y
    
    return total

def main():
    with open('input03.txt', 'r') as file:
        memory = file.read()
    
    result = process_memory(memory)
    print(f"Sum of enabled multiplication results: {result}")

if __name__ == "__main__":
    main()
