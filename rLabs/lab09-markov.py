class Strategy:
    def __init__(self, process, decisions):
        self._process = process # Process
        self._decisions = decisions # int (state) -> int (action)

    def states(self):
        return self._process.states().keys()

    def probability(self, state_1, state_2):
        return self._process.probability(self.dec(state_1), state_2)

    def payoff(self, state_1, state_2):
        return self._process.payoff(self.dec(state_1), state_2)

    def dec(self, state):
        return self._decisions[state]

    def set_dec(self, state, new_action):
        self._decisions[state] = new_action

    def __str__(self):
        return str(self._decisions)


class Process:
    def __init__(self, states, actions, payoffs):
        self._states = states  # int (state) -> list of int (possible actions)
        self._actions = actions  # int (action) -> int (state) -> double(probability)
        self._payoffs = payoffs  # int (action) -> int (state) -> double(payoff)

    def states(self):
        return self._states

    def actions(self, state):
        return self._states[state]

    def probability(self, action, state_2):
        return self._actions[action][state_2]

    def payoff(self, action, state_2):
        return self._payoffs[action][state_2]


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
            new_value[s] = sum(strategy.probability(s, next_s) * (strategy.payoff(s, next_s) + gamma * value[next_s]) for next_s in strategy.states())
            delta = max(delta, abs(v - new_value[s]))
        value = new_value
    return [value, i]


def improve(strategy, value, gamma):
    stable = True
    p = strategy._process
    for s in strategy.states():
        b = strategy.dec(s)
        current_b = b
        max_score = -100000.0
        for new_b in p.actions(s):
            new_b_score = sum(p.probability(new_b, next_s) * (p.payoff(new_b, next_s) + gamma * value[next_s]) for next_s in strategy.states())
            if new_b_score > max_score:
                current_b = new_b
                max_score = new_b_score
        if current_b != b:
            stable = False
        strategy.set_dec(s, current_b)
    return [strategy, stable]


def best(strategy, gamma, theta):
    stable = False
    while not stable:
        value = eval(strategy, gamma, theta)[0]
        stable = improve(strategy, value, gamma)[1]
    return strategy


slajd3 = Process({0: [0, 1], 1: [10, 11], 2: [20, 21]},
        {0: [0.5, 0.0, 0.5], 1: [0.0, 0.0, 1.0], 10: [0.7, 0.1, 0.2], 11: [0.0, 0.95, 0.05], 20: [0.4, 0.0, 0.6], 21: [0.3, 0.3, 0.4]},
        {0: [0, 0, 0], 1: [0, 0, 0], 10: [5, 0, 0], 11: [0, 0, 0], 20: [0, 0, 0], 21: [-1, 0, 0]})
nieoptymalna = Strategy(slajd3, [0, 11, 20])
optymalna = Strategy(slajd3, [1, 10, 21])
opt = Strategy(slajd3, [0, 10, 20])

print(eval(optymalna, 0.99, 0.001))

#for gamma in [0.9, 0.99, 0.999, 0.9999, 0.99999]:
#    for theta in [0.1, 0.01, 0.001, 0.0001, 0.00001]:
#        print("gamma = {0}, theta = {1}, result = {2[0]}, iter = {2[1]}".format(gamma, theta, eval(optymalna, gamma, theta)))

for gamma in [0.9, 0.99, 0.999, 0.9999, 0.99999]:
    for theta in [0.1, 0.01, 0.001, 0.0001, 0.00001]:
        print(best(nieoptymalna, gamma, theta))
