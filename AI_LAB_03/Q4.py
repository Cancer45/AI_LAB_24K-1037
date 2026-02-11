import random

class UtilityBasedAgent:
    def __init__(self):
        pass

    def calculateUtility(self, percept):
        return percept['rating'] - percept['distance']

    def selectAction(self, perceptA, perceptB):
        util_a = self.calculateUtility(perceptA)
        util_b = self.calculateUtility(perceptB)

        if util_a > util_b:
            return 'A'
        else:
            return 'B'

    def act(self, perceptA, perceptB):
        action = self.selectAction(perceptA, perceptB)
        return action

class Environment:
    def __init__(self):
        rand_rating = random.randint(0, 5)
        rand_dist = random.randint(0, 5) # in km
        self.state = {'rating': rand_rating, 'distance': rand_dist}

    def getPercept(self):
        return self.state

def runAgent(agent, environmentA, environmentB):
    perceptA = environmentA.getPercept()
    perceptB = environmentB.getPercept()
    action = agent.act(perceptA, perceptB)

    print("selected restaurant:", action)

agent = UtilityBasedAgent()
environmentA = Environment()
environmentB = Environment()
runAgent(agent, environmentA, environmentB)
