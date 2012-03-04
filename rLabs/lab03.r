e <- 0.3
d <- 0.9
d <- 0.99

d <- 0.95
e <- 0.1
e <- 0.07
e <- 0.05

t <- function(e, d) {
    log(1 - d) / (-2 * e * e)
}

# Zadanie z kartki

f_star <- function(n) {
    two_mod <- ((n %/% 1000) %% 2) == 0
    four_mod <- (n %% 4) == 0
    as.integer((two_mod & four_mod) | ((1 - two_mod) & (1 - four_mod)))
}

N <- 10000

a <- 1:N
d <- f_star(a)

U <- data.frame(a=a, d=d)

prob <- rep(1/N, N)

zad1.indices <- sample(1:N, size=1000, replace=FALSE, prob=prob)
zad1.learn <- U[zad1.indices, ]
zad1.valid <- U[1:N, ]

actual <- U$d[-zad1.indices]

genErr <- rep(0, 20)
for (k in 1:20) {
    zad1.kknn <- kknn(d~., zad1.learn, zad1.valid, k=k)
    predicted <- predict(zad1.kknn, zad1.valid, type="class")
    genErr[k] <- mean(actual != predicted)
    print(k)
    print(genErr[k])
}
