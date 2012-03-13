source("lab05-neurons.r")

n <- randomNetwork(8)

eta <- 0.01

beta <- 0.0001

sigma <- newSigma(beta)

i <- c(0, 1, 2, 3)
t <- c(1, 0, 0, 1)

learn <- net(eta, 0, t, beta, sigma)

for (i in 1:10000) {
    n <- learn(n)
}

o <- evalNetwork(n, sigma, 0)
