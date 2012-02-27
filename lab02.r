irisCrossValidation <- function(n, k) {
    indices <- sample(1 : n, size=n, replace=FALSE, prob=rep(1/n, n))
    empiricErrors <- rep(0, k)
    for (i in 1 : k) {
        testIndices <- indices[((((i - 1) * n) / k) + 1) : ((i * n) / k)]
        test <- iris[testIndices,]
        learning <- iris[-testIndices,]
        ir.learning.tr <- tree(Species~., learning)
        predicted <- predict(ir.learning.tr, test, type="class")
        testActual <- iris$Species[testIndices]
        empiricErrors <- mean(testActual != predicted)
    }
    mean(empiricErrors)
}
