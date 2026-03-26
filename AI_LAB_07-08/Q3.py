class Node:
    def __init__(self, name, value, children):
        self.name = name
        self.val = value
        self.children = children

# define minimax function
MAX_LEVEL = 3
visited = 0
def minimax(node, depth,  max_player, alpha=float('-inf'), beta=float('inf'), level=0, prune=False, update=False):
    global visited
    visited += 1

    if depth == 0 or level == MAX_LEVEL:  # level used to determine if leaf
        print(f"{node.name}(minimax_val): {node.val}")
        return node.val
    
    pruned=False
    if max_player:
        max_eval = float('-inf')
        for child in node.children:
            if pruned:
                print(f"{child.name} ", end="")
                continue
            eval = minimax(child, depth - 1, False, alpha, beta, level+1, prune, update)
            max_eval = max(eval, max_eval)
            if prune:
                alpha = max(alpha, eval)
                if beta <= alpha:
                    pruned=True
                    print("pruned: ", end="")
        print()           
        if update: node.val = max_eval
        print(f"{node.name}(minimax_val): {node.val}")
        return max_eval
    else:
       min_eval = float('+inf')
       for child in node.children:
            if pruned:
                print(f"{child.name} ", end="")
                continue
            eval = minimax(child, depth - 1, True, alpha, beta, level+1, prune, update)
            min_eval = min(eval, min_eval)
            if prune:
                beta = min(beta, eval)
                if beta <= alpha:
                    pruned=True
                    print("pruned: ", end="")
       print()           
       if update: node.val = min_eval
       print(f"{node.name}(minimax_val): {node.val}")
       return min_eval

# build tree
term_vals = [4, 7, 2, 5, 1, 5, 3, 6] # term_vals[5] changed from 8 to 5
terminals = []

for i in range(0, 8):
    terminals.append(Node(f"term({i})", term_vals[i], []))

n3 = Node("n3", 0, [terminals[0], terminals[1]])
n4 = Node("n4", 0, [terminals[2], terminals[3]])
n5 = Node("n5", 0, [terminals[4], terminals[5]])
n6 = Node("n6", 0, [terminals[6], terminals[7]])

n1 = Node("n1", 0, [n3, n4])
n2 = Node("n2", 0, [n5, n6])
root = Node("root", 0, [n1, n2])

# compute minimax values for all nodes
visited = 0
minimax(root, float('inf'), True, update=True)
print(f"visited(no prune): {visited}")

print("\noptimal path:")
print(root.name)
node = root
while node.children:
    node = next(c for c in node.children if c.val == node.val)
    print(node.name)

print() # print newline

# prune
visited = 0
minimax(root, float('inf'), True, prune=True)
print(f"visited(prune): {visited}")
if visited == 15:
    print("no nodes pruned")
else:
    print(f"pruned {15 - visited} nodes")
