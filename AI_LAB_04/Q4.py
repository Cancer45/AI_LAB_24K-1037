import heapq

graph = {
    'S': {'A': 4, 'B': 2},
    'A': {'C': 5, 'D': 10},
    'B': {'E': 3},
    'C': {'G': 4},
    'D': {'G': 1},
    'E': {'D': 4},
    'G': {}
}


class DeliveryAgent:
    def __init__(self, graph, start, goal):
        self.graph = graph
        self.start = start
        self.goal = goal

    def find_route(self):

        frontier = []
        heapq.heappush(frontier, (0, [self.start]))

        visited = []

        print("\nsearching...")

        while frontier:
            cost, path = heapq.heappop(frontier)
            here = path[-1]

            if here in visited:
                continue

            visited.append(here)
            print(f"visiting: {here}  (cost(till now): {cost})")

            if here == self.goal:
                print("\goal found!")
                print("path:", path)
                print("total cost:", cost)
                return

            for neighbour, edge_cost in self.graph[here].items():
                if neighbour not in visited:
                    heapq.heappush(frontier, (cost + edge_cost, path + [neighbour]))

        print("no valid route")


agent = DeliveryAgent(graph, start='S', goal='G')
agent.find_route()
