source("lab05-neurons.r")

n <- randomNetwork(8)

eta <- 0.001

beta <- 0.01

sigma <- newSigma(beta)

iv <- c(0, 1, 2, 3)
tv <- c(1, 0, 0, 1)

learn <- netWhole(eta, iv, tv, beta, sigma)

for (i in 1:4) {
    learn <- net(eta, iv[i], tv[i], beta, sigma)
    myeta <- eta
    for (j in 1:10000000) {
        if (j %% 1000000 == 0) {
            myeta <- myeta / 1.5
            learn <- net(eta, iv[i], tv[i], beta, sigma)
        }
        n <- learn(n)
    }
}

p <- NULL
for (index in 1:length(iv)) {
    p <- c(p, evalNetwork(n, sigma, iv[index]))
}
