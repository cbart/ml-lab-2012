evalNetwork <- function (network, sigma, i) {
    h <- sigma(network$w * i - network$v0)
    sigma(sum(network$v * i - network$u))
}

net <- function (eta, i, t, beta, sigma) {
    function (network) {
        h <- sigma(network$w * i - network$u)
        o <- sigma(sum(network$v * h - network$v0))
        d.o <- o * (1 - o) * (t - o)
        d.h <- h * (1 - h) * network$v * d.o
        d.v <- eta * d.o * h
        d.v0 <- -eta * d.o
        d.w <- eta * d.h * i
        d.u <- -eta * d.h
        list(w=(network$w + d.w), u=(network$u + d.u), v=(network$v + d.v), v0=(network$v0 + d.v0))
    }
}

netWhole <- function (eta, iv, tv, beta, sigma) {
    size <- length(iv)
    learning <- list()
    for (index in 1:size) {
        learning[[index]] <- net(eta, iv[index], tv[index], beta, sigma)
    }
    function (network) {
        net <- network
        for (index in 1:size) {
            net <- learning[[index]](net)
        }
        net
    }
}


randomNetwork <- function(size) {
    w <- sample(seq(-5, 5, by=0.1), size, replace=FALSE)
    u <- sample(seq(-5, 5, by=0.1), size, replace=FALSE)
    v <- sample(seq(-10, 10, by=0.1), size, replace=FALSE)
    v0 <- sample(seq(-10, 10, by=0.1), 1)
    list(w=w, u=u, v=v, v0=v0)
}

newSigma <- function(beta) {
    function(x) {
        1 / (1 + exp(- beta * x))
    }
}
