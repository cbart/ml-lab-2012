package mlclass.classifier

/**
 * @author cbart@students.mimuw.edu.pl (Cezary Bartoszuk)
 */
class Measures(classification: Seq[Double], test: Seq[Boolean], threshold: Double) {
  private val decision = classification.par.map(_ >= threshold)

  private val compared = decision.zip(test)

  private val truePos = compared.count{case (a, b) => a && b}.toDouble

  private val trueNeg = compared.count{case (a, b) => !a && !b}.toDouble

  private val falsePos = compared.count{case (a, b) => a && !b}.toDouble

  private val falseNeg = compared.count{case (a, b) => !a && !b}.toDouble

  lazy val truePositiveRate = truePos / (truePos + falseNeg)

  lazy val falsePositiveRate = falsePos / (falsePos + trueNeg)

  lazy val accuracy = (truePos + trueNeg) / (truePos + trueNeg + falsePos + falseNeg)
}