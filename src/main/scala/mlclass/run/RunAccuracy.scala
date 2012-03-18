package mlclass.run

import mlclass.classifier.bayes.Naive._
import mlclass.classifier.bayes.Naive
import mlclass.classifier.Measures


/**
 * @author cbart@students.mimuw.edu.pl (Cezary Bartoszuk)
 */
object RunAccuracy {
  import RunBayes._

  def main(args: Array[String]) {
    val trainingSetForTest = typedTrainingSet.map{case (a, b) => a}
    val facts = typedTrainingSet.map{case (a, b) => b}
    val classifier = Naive(typedTrainingSet, 0.0001)

    println("Classifying...")

    val bayesDecision = trainingSetForTest.par.map{ sample =>
      val decision = classifier.classify(sample)
      decision(true) - decision(false)
    }

    println("Normalizing...")

    val max = bayesDecision.max
    val min = bayesDecision.min
    val step = (max - min) / 1000

    val normalized = {
      bayesDecision
    }.seq

    println("Measuring...")

    val accThreshold = (min to max by step).par.map {threshold =>
      val measures = new Measures(normalized, facts, threshold)
      val acc = measures.accuracy
      (acc, threshold)
    }.maxBy(_._1)

    println("Max accurracy: %f".format(accThreshold._1))
    println("With log threshold: %f".format(accThreshold._2))
    println("Where max: %f".format(max))
    println("And min: %f".format(min))
  }
}