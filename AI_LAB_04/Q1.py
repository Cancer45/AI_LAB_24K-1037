class Building:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.map = {}

        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid[row][col] == 0:
                    continue
                reachable = []
                for up_down, left_right in [(-1,0),(1,0),(0,-1),(0,1)]:
                    next_row, next_col = row + up_down, col + left_right
                    if 0 <= next_row < self.rows and 0 <= next_col < self.cols:
                        if self.grid[next_row][next_col] == 1:
                            reachable.append((next_row, next_col))
                self.map[(row, col)] = reachable


class Agent:
    def __init__(self, building, start, goal):
        self.building = building
        self.start = start
        self.goal = goal

    def find_goal(self):
        visited = []
        queue = [] 

        visited.append(self.start)
        queue.append([self.start])

        print("\nsearching")

        while queue:
            path = queue.pop(0)
            here = path[-1]
            print(here, end=" ")

            if here == self.goal:
                print("\ngoal found")
                print("shortest path:", path)
                print("until goal:", len(path) - 1)
                return

            for next_cell in self.building.map.get(here, []):
                if next_cell not in visited:
                    visited.append(next_cell)
                    queue.append(path + [next_cell])

        print("\nno valid route")


building = Building([
    [1, 1, 0, 1],
    [0, 1, 1, 1],
    [1, 1, 0, 1],
    [1, 0, 1, 1]
])

agent = Agent(building, start=(0, 0), goal=(3, 3))
agent.find_goal()
