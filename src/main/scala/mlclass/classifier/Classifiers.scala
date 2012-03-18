package mlclass.classifier

/**
 * @author cbart@students.mimuw.edu.pl (Cezary Bartoszuk)
 */
object Classifiers {
  type Sample[Attribute, Decision] = (List[Attribute], Decision)
  type Training[Attribute, Decision] = List[Sample[Attribute, Decision]]
}