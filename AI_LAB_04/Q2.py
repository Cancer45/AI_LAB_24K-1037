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


class Drone:
    def __init__(self, graph, start, goal):
        self.graph = graph
        self.start = start
        self.goal = goal

    def search(self, depth_limit):
        print(f"\nsearching... limit = {depth_limit}:")
        path = []
        found = self._dls(self.start, depth_limit, path)
        if not found:
            print("goal not found")

    def _dls(self, node, depth_remaining, path):
        path.append(node)
        print("Visiting:", node)

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


drone = Drone(graph, start='A', goal='H')
drone.search(depth_limit=2)
drone.search(depth_limit=3)
