class Strategy:
    def __init__(self, process, decisions):
        self.process = process # Process
        self.decisions = decisions # int (state) -> int (action)
    def states(self):
        return self.process.states().keys()
    def p(self, state_1, state_2):
        action = self.decisions[state_1]
        return self.process.p(action, state_2)
    def r(self, state_1, state_2):
        action = self.decisions[state_1]
        return self.process.payoff(action, state_2)
    def dec(self, state):
        return self.decisions[state]

class Process:
    def __init__(self, states, actions, payoffs):
        self.states = states  # int (state) -> list of int (possible actions)
        self.actions = actions  # int (action) -> int (state) -> double(probability)
        self.payoffs = payoffs  # int (action) -> int (state) -> double(probability)
    def states(self):
        return self.states
    def actions(self, state):
        return self.states[state]
    def p(self, action, state_2):
        return self.actions[action][state_2]
    def payoff(self, action, state_2):
        return self.payoffs[action][state_2]

def eval(strategy, gamma, theta):
    delta = 0.0
    value = {s: 0.0 for s in strategy.states()}
    i = 0
    while i == 0 or delta > theta:
        i += 1
        delta = 0.
        new_value = {}
        for s in strategy.states():
            v = value[s]
            new_value[s] = sum(strategy.p(s, next_s) * (strategy.r(s, next_s) + gamma * value[next_s]) for next_s in strategy.states())
            delta = max(delta, abs(v - new_value[s]))
        value = new_value
    return [value, i]

def improve(strategy, 

for gamma in [0.9, 0.99, 0.999, 0.9999, 0.99999]:
    for theta in [0.1, 0.01, 0.001, 0.0001, 0.00001]:
        print("gamma = {0}, theta = {1}, result = {2[0]}, iter = {2[1]}".format(gamma, theta, eval(Strategy(), gamma, theta)))

#print(eval(Strategy(), 0.99, 0.0001))
