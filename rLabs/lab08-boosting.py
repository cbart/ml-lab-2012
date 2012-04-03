from math import log, exp

simpleData = [[0, -1], [1, 1], [1, 1]]
complexData = [[0, 1], [1, -1], [2, 1], [3, -1],
        [4, -1], [5, -1], [6, 1], [7, -1], [8, 1],
        [9, -1], [10, -1], [11, -1], [12, -1], [13, -1],
        [14, -1], [15, -1], [16, -1], [17, -1], [18, 1],
        [19, -1], [20, 1], [21, -1], [22, -1], [23, -1],
        [24, 1], [25, -1], [26, 1]]

def error(data, h, prob):
    errors = [p for (i, p) in zip(data, prob) if i[1] != h(i[0])]
    return sum(errors)

def alpha(e):
    return 0.5 * log((1.0 - e)/e)

def classifier(data, prob, classifiers):
    e = 100
    h = None
    for c in classifiers:
        ce = error(data, c, prob)
        if ce < e:
            e = ce
            h = c
    return h

constClassifiers = [lambda x: 1, lambda x: -1]

def lessThanOrEq(x):
    return lambda y: 1 if (y <= x) else -1
lessThanOrEqClassifiers = [lessThanOrEq(d[0]) for d in complexData]

def equal(x):
    return lambda y: 1 if (x == y) else -1
equalClassifiers = [equal(d[0]) for d in complexData]

def notEqual(x):
    return lambda y: 1 if (x != y) else -1
notEqualClassifiers = [notEqual(d[0]) for d in complexData]

def boosting(data, classifiers):
    dPrev = [0 for i in data]
    dCur = [1.0/len(data) for i in data]
    h = []
    e = []
    a = []
    i = 1
    while (dPrev != dCur) and (i < 1000):
        h.append(classifier(data, dCur, classifiers))
        print("h%d = %s" % (i, ", ".join(["%.2f" % h[-1](d[0]) for d in data])))
        print("d%d = %s" % (i, ", ".join(["%.2f" % f for f in dCur])))
        dPrev = dCur
        e.append(error(data, h[-1], dCur))
        print("e%d = %.2f" % (i, e[-1]))
        a.append(alpha(e[-1]))
        print("a%d = %.2f" % (i, a[-1]))
        i = i + 1
        dCur = [(d * exp((-1.) * a[-1] * h[-1](p[0]) * p[1])) for (d, p) in zip(dPrev, data)]
        dCurSum = sum(dCur)
        dCur = [d / dCurSum for d in dCur]

boosting(simpleData, constClassifiers)

boosting(complexData, lessThanOrEqClassifiers)
