import heapq

maze = [
    [1, 1, 0, 1, 1, 1],
    [0, 1, 0, 1, 0, 1],
    [1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 1],
    [1, 1, 1, 0, 1, 0],
    [0, 0, 1, 1, 1, 1]
]


goals = [(0, 5), (2, 0), (5, 5)]


class MazeEnv:
    def __init__(self, maze):
        self.maze = maze
        self.rows = len(maze)
        self.cols = len(maze[0])

    def reachable_from(self, pos):
        row, col = pos
        neighbours = []
        for up_down, left_right in [(-1,0),(1,0),(0,-1),(0,1)]:
            next_row, next_col = row + up_down, col + left_right
            if 0 <= next_row < self.rows and 0 <= next_col < self.cols:
                if self.maze[next_row][next_col] == 1:
                    neighbours.append((next_row, next_col))
        return neighbours


class ExplorerAgent:
    def __init__(self, env, start, goals):
        self.env = env
        self.start = start
        self.goals = goals

    def manhattan(self, pos, target):
        return abs(pos[0] - target[0]) + abs(pos[1] - target[1])

    def nearest_goal(self, pos, remaining_goals):
        return min(remaining_goals, key=lambda goal: self.manhattan(pos, goal))

    def best_first_search(self, start, target):

        frontier = []
        heapq.heappush(frontier, (0, [start]))

        visited = []

        while frontier:
            _, path = heapq.heappop(frontier)
            here = path[-1]

            if here in visited:
                continue

            visited.append(here)
            print("visiting...", here)

            if here == target:
                return path

            for next_cell in self.env.reachable_from(here):
                if next_cell not in visited:
                    score = self.manhattan(next_cell, target)
                    heapq.heappush(frontier, (score, path + [next_cell]))

        return None

    def collect_all_goals(self):
        remaining_goals = list(self.goals)
        current = self.start
        full_path = [current]

        print("\nstarted maze navigation:")

        while remaining_goals:
            target = self.nearest_goal(current, remaining_goals)
            print(f"\ntowards goal: {target}")

            segment = self.best_first_search(current, target)

            if segment is None:
                print(f"unreachable {target}.")
                return


            full_path += segment[1:]
            remaining_goals.remove(target)
            current = target

        print("\nall goals reached")
        print("full path:", full_path)


env = MazeEnv(maze)
agent = ExplorerAgent(env, start=(0, 0), goals=goals)
agent.collect_all_goals()
