package mlclass.classifier
package bayes

/**
 * @author cbart@students.mimuw.edu.pl (Cezary Bartoszuk)
 */
object Naive {
  import Classifiers._

  def apply[Attribute, Decision](training: Training[Attribute, Decision], epsilon: Double):
      Naive[Attribute, Decision] = {
    val dec = logℙ(training.map(decision))
    val attr: Map[Decision, Map[Int, Map[Attribute, Double]]] = training
        .groupBy(decision)
        .mapValues(_.map(attributes))
        .mapValues {attrs =>
      (for ((sample, i) <- attrs.transpose.zipWithIndex) yield (i, logℙ(sample))).toMap
    }
    new Naive[Attribute, Decision](dec, attr, epsilon)
  }

  private[this] def logℙ[Observation](experimentResult: List[Observation]):
      Map[Observation, Double] = {
    val resultSize = experimentResult.size.toDouble
    experimentResult.groupBy(identity).mapValues(v => math.log(v.size.toDouble / resultSize))
  }

  private def decision[Attribute, Decision](sample: Sample[Attribute, Decision]) = {
    val (_, decision) = sample
    decision
  }

  private def attributes[Attribute, Decision](sample: Sample[Attribute, Decision]) = {
    val (attributes, _) = sample
    attributes
  }
}


final class Naive[Attribute, Decision] private (dec: Map[Decision, Double],
    attr: Decision => Int => Map[Attribute, Double], epsilon: Double)
    extends Classifier[Attribute, Decision] {
  val logEpsilon = math.log(epsilon)
  override def classify(sample: List[Attribute]): Map[Decision, Double] = {
    val indexedSample = sample.zipWithIndex
    for ((decision, pDecision) <- dec) yield {
      val pAttrs = for ((value, i) <- indexedSample) yield attr(decision)(i).getOrElse(value, logEpsilon)
      (decision, (pDecision :: pAttrs).sum)
    }
  }
}