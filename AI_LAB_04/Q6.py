import heapq
import random
import time

graph = {
    'S': {'A': 4, 'B': 2},
    'A': {'C': 5, 'D': 10, 'B': 1},
    'B': {'E': 12, 'A': 1},
    'C': {'G': 3},
    'D': {'G': 2},
    'E': {'D': 4, 'G': 8},
    'G': {}
}


heuristic = {
    'S': 8,
    'A': 6,
    'B': 7,
    'C': 3,
    'D': 2,
    'E': 5,
    'G': 0
}


class RouteEnv:
    def __init__(self, graph):
        self.graph = graph
        self.all_edges = self._list_edges()

    def _list_edges(self):
        edges = []
        for node, neighbours in self.graph.items():
            for neighbour in neighbours:
                edges.append((node, neighbour))
        return edges

    def random_cost_change(self):
        node, neighbour = random.choice(self.all_edges)
        old_cost = self.graph[node][neighbour]
        change = random.choice([-3, -2, 2, 3, 4])
        new_cost = max(1, old_cost + change)  
        self.graph[node][neighbour] = new_cost
        print(f"\n   edge {node}–{neighbour} changed: {old_cost} -> {new_cost}")


class NavigatorAgent:
    def __init__(self, env, start, goal):
        self.env = env
        self.start = start
        self.goal = goal

    def search(self):


        frontier = []
        heapq.heappush(frontier, (0, 0, [self.start]))

        visited = []

        print("\nsearching")

        while frontier:
            f_score, cost_so_far, path = heapq.heappop(frontier)
            here = path[-1]

            if here in visited:
                continue

            visited.append(here)
            print(f"visiting: {here}  (cost(till now): {cost_so_far}, f score: {f_score})")

            if here == self.goal:
                print("\ngoal found")
                print("path:", path)
                print("total cost:", cost_so_far)
                return path, cost_so_far

            for neighbour, edge_cost in self.env.graph[here].items():
                if neighbour not in visited:
                    new_cost = cost_so_far + edge_cost
                    f = new_cost + heuristic[neighbour]
                    heapq.heappush(frontier, (f, new_cost, path + [neighbour]))

        print("no valid route")
        return None, None

    def run_with_changes(self, num_changes=3):
        print("initial seach")
        path, cost = self.search()

        for i in range(num_changes):
            time.sleep(0.5)
            print(f"\ncost change {i + 1}")
            self.env.random_cost_change()
            path, cost = self.search()


env = RouteEnv(graph)
agent = NavigatorAgent(env, start='S', goal='G')
agent.run_with_changes(num_changes=3)
