class GoalStudyAgent:
    def __init__(self):
        self.goal = 'study'

    def formulateGoal(self, percept):
        if percept == 'tostudy':
            self.goal = 'study'
        else:
            self.goal = 'no action needed'

    def act(self, percept):
        self.formulateGoal(percept)
        if self.goal == 'study':
            return 'study now'
        else:
            return 'studied'

class Environment:
    def __init__(self, state='tostudy'):
        self.state = state

    def getPercept(self):
        return self.state

    def study(self):
        print("studying AI\nstudying Maths\nstudying physics")
        self.state = 'studied'

def runAgent(agent, environment, steps):
    for step in range(steps):
        percept = environment.getPercept()
        action = agent.act(percept)
        print(f"step {step + 1}: percept - {percept}, action - {action}")
        if percept == 'tostudy':
            environment.study()

agent = GoalStudyAgent()
environment = Environment()

runAgent(agent, environment, 1)
        
