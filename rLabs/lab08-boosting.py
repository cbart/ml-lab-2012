from math import log, exp

simpleData = [[0, -1], [1, 1], [1, 1]]
complexData = [[0, 1], [1, -1], [2, 1], [3, -1],
        [4, -1], [5, -1], [6, 1], [7, -1], [8, 1],
        [9, -1], [10, -1], [11, -1], [12, -1], [13, -1],
        [14, -1], [15, -1], [16, -1], [17, -1], [18, 1],
        [19, -1], [20, 1], [21, -1], [22, -1], [23, -1],
        [24, 1], [25, -1], [26, 1]]

def firstClassifier(data):
    plus = len([1 for i in data if i[1] == 1])
    minus = len([1 for i in data if i[1] == -1])
    if plus >= minus:
        return 1
    else:
        return -1

def error(data, h, dec):
    errors = [d for (i, d) in zip(data, dec) if i[1] != h]
    return sum(errors)

def alpha(e):
    return 0.5 * log((1.0 - e)/e)

def classifier(data, dec):
    plus = sum([d for (p, d) in zip(data, dec) if p[1] == 1])
    minus = sum([d for (p, d) in zip(data, dec) if p[1] == -1])
    if plus >= minus:
        return 1
    else:
        return -1

def boosting(data):
    dPrev = [0 for i in data]
    dCur = [1.0/len(data) for i in data]
    h = [firstClassifier(data)]
    print("h1 = %d" % h[-1])
    e = []
    a = []
    i = 1
    while dPrev != dCur:
        print("d%d = %s" % (i, ", ".join(["%.2f" % f for f in dCur])))
        dPrev = dCur
        e.append(error(data, h[-1], dCur))
        print("e%d = %.2f" % (i, e[-1]))
        a.append(alpha(e[-1]))
        print("a%d = %.2f" % (i, a[-1]))
        i = i + 1
        dCur = [(d * exp((-1.) * a[-1] * h[-1] * p[1])) for (d, p) in zip(dPrev, data)]
        dCurSum = sum(dCur)
        dCur = [d / dCurSum for d in dCur]
        h.append(classifier(data, dCur))
boosting(simpleData)
