source("lab03-modelSelection2validation.r")

CrossValidation <- function (sample) train.kknn(decision~., sample, kmax=1)

validation(CrossValidation, 1000, UniverseSize, Distribution, Universe, 10000, 1000, 0.95)
