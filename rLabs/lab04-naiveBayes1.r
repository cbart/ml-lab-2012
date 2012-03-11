PCancer = 0.008
PNoCancer = 1 - PCancer
PPlusCancer = 0.98
PPlusNoCancer = 0.03
PPlus = (PPlusCancer * PCancer) + (PPlusNoCancer * PNoCancer)
PCancerPlus = (PPlusCancer * PCancer) / PPlus

PPlusSqCancer = PPlusCancer * PPlusCancer
PPlusSqNoCancer = PPlusNoCancer * PPlusNoCancer
PPlusSq = (PPlusSqCancer * PCancer) + (PPlusSqNoCancer * PNoCancer)
PCancerPlusSq = (PPlusSqCancer * PCancer) / PPlusSq
