import random

class Environment:
    def __init__(self, state='onyes'):
        self.state = state
    
    def getPercept(self):
        return self.state

    def lightChange(self, change):
        self.state = change

class ModelSmartAgent:
    def __init__ (self):
        self.model = {}

    def updateModel(self, percept):
        self.model['prev'] = self.model.get('curr')
        self.model['curr'] = percept

    def predictAction(self):
        if self.model['curr'] == 'offyes':
            return 'turn lights on'

        elif self.model['curr'] == 'onno':
            return 'turn light off'

        else:
            return 'do nothing'
    
    def act(self, percept):
        self.updateModel(percept)
        return self.predictAction()

def runAgent(agent, environment, steps):
    for step in range(steps):
        percept = environment.getPercept()
        action = agent.act(percept)
        print(f"step {step + 1}: percept - {percept}, action - {action}")

        if percept == 'onno':
            environment.lightChange('offno')
        if percept == 'offyes':
            environment.lightChange('onyes')

states = ['offno', 'offyes', 'onno', 'onyes']
agent = ModelSmartAgent()
environment = Environment(states[random.randint(0, 3)])

runAgent(agent, environment, 8)

