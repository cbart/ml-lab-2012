factorial <- function(n, acc=1) if (n == 0) acc else factorial(n - 1, acc * n)

factorial_imp <- function(n) {
    fac <- 1
    i <- 1
    while (i <= n) {
        fac <- fac * i
        i <- i + 1
    }
    fac
}

discrete <- function(x) {
    y[x <= -0.5] <- "A"
    y[-0.5 < x & x <= 0.5] <- "B"
    y[0.5 < x] <- "C"
    y
}

sinuses <- function(n) discrete(sin(1:n))
