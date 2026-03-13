import heapq
def heuristic(x, goal):
    return abs(goal - x)

def getNeighbors(x):
    return [x + 2, x + 3, 2 * x]

def beamSearch(start, goal, beam_width):
    beam = [(0, [start])]

    i = 0
    while beam:
        candidates = []
        for cost, path in beam:
            current_node = path[-1]
            # check if goal
            if current_node == goal:
                return cost, path
            # generate neighbors
            neighbors = getNeighbors(current_node)
            # update candidates
            for neighbor in neighbors:
                candidates.append((cost + heuristic(neighbor, goal) + 1, path + [neighbor])) # all edges are assumed to have standard cost 1
            print(f"level {i}: ", neighbors)
            i += 1
        beam = heapq.nsmallest(beam_width, candidates, key=lambda x: x[0])
    return None, []

ret = beamSearch(1, 20, 2)
print(f"path: {ret[1]}\ncost: {ret[0]}")
