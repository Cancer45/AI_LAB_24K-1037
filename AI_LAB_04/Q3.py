graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': [],
    'F': ['H'],
    'G': [],
    'H': []
}


class TreasureHunter:
    def __init__(self, graph, start, goal):
        self.graph = graph
        self.start = start
        self.goal = goal

    def search(self):
        depth = 0
        while True:
            print(f"\ndepth limit = {depth}:")
            path = []
            found = self._dls(self.start, depth, path)
            if found:
                return
            depth += 1

    def _dls(self, node, depth_remaining, path):
        path.append(node)
        print("visiting:", node)

        if node == self.goal:
            print("goal found!")
            print("path:", path)
            return True

        if depth_remaining == 0:
            path.pop()
            return False

        for neighbour in self.graph[node]:
            found = self._dls(neighbour, depth_remaining - 1, path)
            if found:
                return True

        path.pop()
        return False


hunter = TreasureHunter(graph, start='A', goal='G')
hunter.search()
