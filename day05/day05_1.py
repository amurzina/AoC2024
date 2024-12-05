def build_graph(rules):
    # Build a directed graph from the rules
    graph = {}
    for rule in rules:
        before, after = map(int, rule.strip().split('|'))
        if before not in graph:
            graph[before] = set()
        if after not in graph:
            graph[after] = set()
        graph[before].add(after)
    return graph

def has_cycle(graph, node, visited, path_visited):
    visited.add(node)
    path_visited.add(node)
    
    for neighbor in graph.get(node, set()):
        if neighbor not in visited:
            if has_cycle(graph, neighbor, visited, path_visited):
                return True
        elif neighbor in path_visited:
            return True
    
    path_visited.remove(node)
    return False

def is_valid_order(graph, update):
    # Create a subgraph with only the pages in this update
    update_set = set(update)
    subgraph = {page: {next_page for next_page in graph.get(page, set()) 
                      if next_page in update_set}
                for page in update_set}
    
    # Check if the order respects all rules
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            # If there's a path from j to i in the graph, the order is wrong
            if has_path(subgraph, update[j], update[i], update_set):
                return False
    return True

def has_path(graph, start, end, valid_nodes):
    if start == end:
        return True
    visited = set()
    stack = [start]
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, set()):
                if neighbor in valid_nodes:
                    if neighbor == end:
                        return True
                    stack.append(neighbor)
    return False

def solve_puzzle(input_file):
    # Read and parse input
    with open(input_file, 'r') as f:
        content = f.read().strip().split('\n\n')
    
    rules = content[0].split('\n')
    updates = [list(map(int, update.split(','))) for update in content[1].split('\n')]
    
    # Build the graph from rules
    graph = build_graph(rules)
    
    # Process each update
    middle_sum = 0
    for update in updates:
        if is_valid_order(graph, update):
            # Find middle page number
            middle_idx = len(update) // 2
            middle_sum += update[middle_idx]
    
    return middle_sum

if __name__ == "__main__":
    result = solve_puzzle("input05.txt")
    print(f"The sum of middle page numbers from correctly ordered updates is: {result}")
