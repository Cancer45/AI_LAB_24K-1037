import random

class Environment:
    def __init__(self):
        rand = random.randint(0, 1)
        if rand == 0:
            self.initial_state = 'heavy'
        else:
            self.initial_state = 'light'

    def getPercept(self):
        return self.initial_state

class ReflexTrafficAgent:
    def __init__(self):
        pass
    
    def act(self, percept):
        if percept == 'heavy':
            return 'extend green'
        elif percept == 'light':
            return 'normal green'

def runAgent(agent, environment):
    percept = environment.getPercept()
    action = agent.act(percept)
    print(f"percept: {percept}, action: {action}")

agent = ReflexTrafficAgent()
environment = Environment()

runAgent(agent, environment)

