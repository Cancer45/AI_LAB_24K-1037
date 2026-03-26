class Node:
    def __init__(self, name, value, children):
        self.name = name
        self.val = value
        self.children = children

# define minimax function
MAX_LEVEL = 3
def minimax(node, depth,  max_player, level=0):
    if depth == 0 or level == MAX_LEVEL:  # level used to determine if leaf
        print(f"{node.name}(minimax_val): {node.val}")
        return node.val
    
    if max_player:
        max_eval = float('-inf')
        for child in node.children:
            eval = minimax(child, depth - 1, False, level+1)
            max_eval = max(eval, max_eval)
        # update
        node.val = max_eval
        print(f"{node.name}(minimax_val): {node.val}")
        return max_eval
    else:
       min_eval = float('+inf')
       for child in node.children:
            eval = minimax(child, depth - 1, True, level+1)
            min_eval = min(eval, min_eval)
       # update
       node.val = min_eval
       print(f"{node.name}(minimax_val): {node.val}")
       return min_eval

# build tree
term_vals = [4, 7, 2, 5, 1, 8, 3, 6]
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
minimax(root, float('inf'), True, 0)

print() # print newline

# add depth-limiting 2
minimax(root, 2, True, 0)
