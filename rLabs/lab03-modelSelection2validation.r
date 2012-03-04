source("lab03-modelSelection.r")

# Validation
(function (sampleSize, universeSize, distribution, universe, loopSteps, testSize) {
    print("[Validation]")
    learningSampleIndices <- sample(1:universeSize, size=sampleSize, replace=FALSE, prob=distribution)
    learningSample <- universe[learningSampleIndices, ]

    fullTestSampleIndices <- 1:universeSize
    fullTestSample <- universe[fullTestSampleIndices, ]
    fullTestSampleActualDecisions <- universe$decision[fullTestSampleIndices]
    classifier <- kknn(decision~., learningSample, universe[1:100, ], k=1)
    fullTestSamplePredictedDecisions <- predict(classifier, fullTestSample, type="class")
    generalizationError <- mean(fullTestSampleActualDecisions != fullTestSamplePredictedDecisions)
    print(sprintf("Generalization error: %f", generalizationError))
    errorsDiff <- rep(0, loopSteps)
    for (ii in 1:loopSteps) {
        testSampleIndices <- sample(1:universeSize, size=testSize, replace=FALSE, prob=distribution)
        testSample <- universe[testSampleIndices, ]
        testSampleActualDecisions <- universe$decision[testSampleIndices]
        testSamplePredictedDecisions <- predict(classifier, testSample, type="class")
        empiricError <- mean(testSampleActualDecisions != testSamplePredictedDecisions)
        errorsDiff[ii] <- generalizationError - empiricError
        print(sprintf("[%d] Empiric error: %f", ii, empiricError))
    }
    print(sprintf("Mean difference between generalization error and empiric error: %f", mean(errorsDiff)))
})(1000, UniverseSize, Distribution, Universe, 10000, 1000)
