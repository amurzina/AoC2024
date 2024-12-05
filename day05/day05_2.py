from collections import defaultdict, deque

def build_graph(rules):
    # Build a directed graph from the rules
    graph = defaultdict(set)
    indegree = defaultdict(int)
    for rule in rules:
        before, after = map(int, rule.strip().split('|'))
        graph[before].add(after)
        indegree[after] += 1
        # Make sure both nodes are in the graph
        if before not in indegree:
            indegree[before] = 0
    return graph, indegree

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

def topological_sort(graph, indegree, nodes):
    # Initialize queue with nodes that have no dependencies
    queue = deque([n for n in nodes if indegree[n] == 0])
    result = []
    
    # Process nodes
    while queue:
        node = queue.popleft()
        result.append(node)
        
        # Update indegrees of neighbors
        for neighbor in graph[node]:
            if neighbor in nodes:  # Only consider nodes in our update
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
    
    return result

def get_correct_order(graph, indegree, update):
    # Create subgraph for this update
    update_set = set(update)
    sub_indegree = defaultdict(int)
    
    # Calculate indegrees for the subgraph
    for node in update_set:
        for neighbor in graph[node]:
            if neighbor in update_set:
                sub_indegree[neighbor] += 1
        if node not in sub_indegree:
            sub_indegree[node] = 0
    
    # Get topologically sorted order
    return topological_sort(graph, sub_indegree, update_set)

def solve_puzzle(input_file):
    # Read and parse input
    with open(input_file, 'r') as f:
        content = f.read().strip().split('\n\n')
    
    rules = content[0].split('\n')
    updates = [list(map(int, update.split(','))) for update in content[1].split('\n')]
    
    # Build the graph from rules
    graph, indegree = build_graph(rules)
    
    # Process each update
    middle_sum = 0
    for update in updates:
        if not is_valid_order(graph, update):
            # Get correct order for invalid updates
            correct_order = get_correct_order(graph, indegree, update)
            # Add middle number to sum
            middle_idx = len(correct_order) // 2
            middle_sum += correct_order[middle_idx]
    
    return middle_sum

if __name__ == "__main__":
    result = solve_puzzle("input05.txt")
    print(f"The sum of middle page numbers from reordered incorrect updates is: {result}")
