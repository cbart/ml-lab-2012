import random
import math

def unif():
    return random.uniform(0.0, 1.0)
    #return random.gauss(0.5, 0.1)

def randomPoint():
    return [unif(), unif()]

def randomNet(n):
    return [randomPoint() for i in xrange(n)]

def dist(p1, p2):
    return math.sqrt(sum([math.pow(x1 - x2, 2.0) for x1, x2 in zip(p1, p2)]))

def argMin(net, p):
    return min((dist(e, p), e) for e in net)[1]

def indexMin(net, p):
    return net.index(argMin(net, p))

T = 1000
N = 1000

def h0(t):
    return 0.9 * (1.0 - (1.0 * t) / T)

def sigma(t):
    return (N / 4.0) * math.pow(1.0 - (1.0 * t)  /T, 2.0)

#def sigma(t):
#    return (N / 4.0) * math.exp(-1.0*t/T)

def h(t, ri, rc):
    return h0(t) * math.exp(-math.pow(ri - rc, 2.0) / math.pow(sigma(t), 2.0))

def learningStep(t, net):
    point = randomPoint()
    rc = indexMin(net, point)
    netIdx = zip(net, xrange(len(net)))
    def diff(p1, p2):
        return [p1[0] - p2[0], p1[1] - p2[1]]
    def plus(p1, p2):
        return [p1[0] + p2[0], p1[1] + p2[1]]
    def mul(p1, x):
        return [p1[0] * x, p1[1] * x]
    return [plus(n, mul(diff(point, n), h(t, ri, rc))) for n, ri in netIdx]

net = randomNet(N)
for t in xrange(1, T):
    net = learningStep(t, net)

import matplotlib.pyplot as plt
plt.plot(*zip(*net))
plt.ylabel('some numbers')
plt.show()
