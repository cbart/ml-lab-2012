source("lab03-modelSelection.r")

# Validation
(function (sampleSize, universeSize, distribution, universe, loopSteps, testSize, credibility) {
    print("[Validation]")
    learningSampleIndices <- sample(1:universeSize, size=sampleSize, replace=FALSE, prob=distribution)
    learningSample <- universe[learningSampleIndices, ]

    fullTestSampleIndices <- 1:universeSize
    fullTestSample <- universe[fullTestSampleIndices, ]
    fullTestSampleActualDecisions <- universe$decision[fullTestSampleIndices]
    classifier <- kknn(decision~., learningSample, learningSample, k=1)
    fullTestSamplePredictedDecisions <- predict(classifier, fullTestSample, type="class")
    generalizationError <- mean(fullTestSampleActualDecisions != fullTestSamplePredictedDecisions)
    print(sprintf("Generalization error: %f", generalizationError))
    empiricErrors <- rep(0, loopSteps)
    for (ii in 1:loopSteps) {
        testSampleIndices <- sample(1:universeSize, size=testSize, replace=FALSE, prob=distribution)
        testSample <- universe[testSampleIndices, ]
        testSampleActualDecisions <- universe$decision[testSampleIndices]
        testSamplePredictedDecisions <- predict(classifier, testSample, type="class")
        empiricErrors[ii] <- mean(testSampleActualDecisions != testSamplePredictedDecisions)
        print(sprintf("[%d] Empiric error: %f", ii, empiricErrors[ii]))
    }
    print(sprintf("Mean difference between generalization error and empiric error: %f",
        mean(rep(generalizationError, loopSteps) - empiricErrors)))
    sortedEmpiricErrors <- sort(empiricErrors)
    bound <- sortedEmpiricErrors[round(loopSteps * (1.0 - credibility))]
    epsilon <- generalizationError - bound
    print(sprintf("E(fU) < ET(fU) + %f with credibility of %f", epsilon, credibility))
    hoeffdingEpsilon <- sqrt(-log(1 - credibility)/(2 * testSize))
    print(sprintf("Epsilon given by Hoeffding inequality: %f", hoeffdingEpsilon))
})(1000, UniverseSize, Distribution, Universe, 10000, 1000, 0.95)
