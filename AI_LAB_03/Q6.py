class Environment:
    def __init__(self):
        self.grid = [
            [['a', 'safe'], ['b', 'safe'], ['c', 'fire']],
            [['d', 'safe'], ['e', 'fire'], ['f', 'safe']],
            [['g', 'safe'], ['h', 'safe'], ['j', 'fail']]
        ]


class Agent:
    def __init__(self, env: Environment):
        self.env = env

    def runAgent(self):  
        for row in self.env.grid:
            for cell in row:
                if cell[1] == 'safe':
                    print("no fire in room", cell[0])
                else:
                    cell[1] = 'safe'
                    print("fire detected and extinguished in room", cell[0])

        for row in self.env.grid:
            for cell in row:
                print(f"current status of room {cell[0]}: {cell[1]}")


env = Environment()
agent = Agent(env)

agent.runAgent()
