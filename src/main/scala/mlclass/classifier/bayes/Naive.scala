package mlclass.classifier.bayes

/**
 * @author cbart@students.mimuw.edu.pl (Cezary Bartoszuk)
 */
object Naive {
  type Sample[Attribute, Decision] = (List[Attribute], Decision)
  type Training[Attribute, Decision] = List[Sample[Attribute, Decision]]

  def apply[Attribute, Decision](training: Training[Attribute, Decision]):
      Naive[Attribute, Decision] = {
    val dec = ℙ(training.map(decision))
    val attr = training
        .groupBy(decision)
        .mapValues(_.map(attributes))
        .mapValues {attrs =>
      attrs.transpose.map(ℙ)
    }
    new Naive[Attribute, Decision](dec, attr)
  }

  private[this] def ℙ[Observation](experimentResult: List[Observation]):
      Map[Observation, Double] = {
    val resultSize = experimentResult.size.toDouble
    experimentResult.groupBy(identity).mapValues(_.size.toDouble / resultSize)
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
    attr: Decision => Int => Map[Attribute, Double]) {
  def classify(sample: List[Attribute]): Map[Decision, Double] = {
    for ((decision, pdecision) <- dec) yield {
      val Attrs = for ((value, i) <- sample.zipWithIndex) yield attr(decision)(i).getOrElse(value, 0.01)
      (decision, (pdecision :: Attrs).map(math.log).sum)
    }
  }
}