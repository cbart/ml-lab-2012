# Model selection

fAsterisk <- function(n) {
    twoMod <- ((n %/% 1000) %% 2) == 0
    fourMod <- (n %% 4) == 0
    as.integer((twoMod & fourMod) | ((1 - twoMod) & (1 - fourMod)))
}

UniverseSize <- 10000

Universe <- (function(size, decisionFunction) {
    attribute <- 1:size
    decision <- decisionFunction(attribute)
    data.frame(attribute=attribute, decision=decision)
})(UniverseSize, fAsterisk)

Distribution <- rep(1/UniverseSize, UniverseSize)
