source("lab03.r")

# BiasVarianceTradeOff
GeneralizationError <- (function (sampleSize, universeSize, distribution, universe) {
    learningSampleIndices <- sample(1:universeSize, size=sampleSize, replace=FALSE, prob=distribution)
    learningSample <- universe[learningSampleIndices, ]
    testSampleIndices <- 1:universeSize
    testSample <- universe[testSampleIndices, ]
    testSampleActualDecisions <- universe$decision[testSampleIndices]
    generalizationError <- rep(0, 10)
    print("[Bias variance trade-off] Computing generalization error:")
    for (k in 1:10) {
        classifier <- kknn(decision~., learningSample, testSample, k=k)
        testSamplePredictedDecisions <- predict(classifier, testSample, type="class")
        generalizationError[k] <- mean(testSampleActualDecisions != testSamplePredictedDecisions)
        print(sprintf("%d-NN, generalization error: %f", k, generalizationError[k]))
    }
    generalizationError
})(1000, UniverseSize, Distribution, Universe)
