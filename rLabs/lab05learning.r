source("lab05-neurons.r")

n <- randomNetwork(8)

eta <- 0.75

beta <- 0.5

sigma <- newSigma(beta)

iv <- c(0, 1, 2, 3)
tv <- c(1, 0, 0, 1)

learn <- netWhole(eta, iv, tv, beta, sigma)

myeta <- eta
for (j in 1:200000) {
    if (j %% 1000 == 0) {
        myeta <- myeta / 1.0
        learn <- netWhole(eta, iv, tv, beta, sigma)
    }
    n <- learn(n)
}

p <- NULL
for (index in 1:length(iv)) {
    p <- c(p, evalNetwork(n, sigma, iv[index]))
}
