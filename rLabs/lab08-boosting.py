from math import log, exp, fabs

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

def classifierF(data, prob, classifiers):
    e = 0.0
    h = None
    def f(x):
        return fabs(0.5 - x)
    for c in classifiers:
        ce = f(error(data, c, prob))
        if ce > e:
            e = ce
            h = c
    return h

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

def greaterThanOrEq(x):
    return lambda y: -1 if (y <= x) else 1
greaterThanOrEqClassifiers = [greaterThanOrEq(d[0]) for d in complexData]

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
    while (dPrev != dCur) and (i < 50):
        h.append(classifier(data, dCur, classifiers))
        print("h%d = %s" % (i, ", ".join(["%.0f" % h[-1](d[0]) for d in data])))
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
    return [a, h]

def classify(booster, arg):
    a = booster[0]
    h = booster[1]
    s = sum([ai * hi(arg) for (ai, hi) in zip(a, h)])
    if s < 0:
        return -1
    else:
        return 1

#booster = boosting(simpleData, constClassifiers)
#classified = [classify(booster, d[1]) for d in simpleData]
#print("Classified: %s" % classified)
#print("   Results: %s" % [d[1] for d in simpleData])

#booster = boosting(complexData, lessThanOrEqClassifiers)  # 40
#booster = boosting(complexData, equalClassifiers)  # 50
#booster = boosting(complexData, notEqualClassifiers)  # 50
lessThanOrEqClassifiers.extend(greaterThanOrEqClassifiers)  # 40
booster = boosting(complexData, lessThanOrEqClassifiers)
classified = [classify(booster, d[0]) for d in complexData]
print("Classified: %s" % classified)
print("   Results: %s" % [d[1] for d in complexData])
