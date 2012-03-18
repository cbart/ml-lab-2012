package mlclass.run

import mlclass.classifier.bayes.Naive
import scala.collection.mutable
import mlclass.classifier.Measures


/**
 * @author cbart@students.mimuw.edu.pl (Cezary Bartoszuk)
 */
object RunAuc {
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

    val normalized = {
      val max = bayesDecision.max
      bayesDecision.par.map{score => math.exp(score - max)}
    }.seq

    println("Measuring...")

    val roc = mutable.PriorityQueue.empty[(Double, Double)](second)
    (0.0 to 1.0 by 0.000001).par.foreach{ threshold =>
      println(threshold)
      val measures = new Measures(normalized, facts, threshold)
      val tpr = measures.truePositiveRate
      val fpr = measures.falsePositiveRate
      roc.synchronized {
        roc.enqueue((tpr, fpr))
      }
    }

    println("Computing AUC...")

    var lastPosition: Double = 0.0
    var auc: Double = 0.0
    while (roc.nonEmpty) {
      val (tpr, fpr) = roc.dequeue()
      auc += tpr * (fpr - lastPosition)
      lastPosition = fpr
    }
    println(auc)
  }

  val doubleOrdering = implicitly[Ordering[Double]]

  val second: Ordering[(Double, Double)] = new Ordering[(Double, Double)] {
    def compare(x: (Double, Double), y: (Double, Double)): Int = {
      doubleOrdering.compare(x._2, y._2)
    }
  }
}