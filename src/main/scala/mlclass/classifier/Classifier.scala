package mlclass.classifier

/**
 * @author cbart@students.mimuw.edu.pl (Cezary Bartoszuk)
 */
trait Classifier[Attribute, Decision] {
  def classify(sample: List[Attribute]): Map[Decision, Double]
}