package mlclass.io

/**
 * @author cbart@students.mimuw.edu.pl (Cezary Bartoszuk)
 */
class TypedCsv {
  def mapTypes[Attribute, Decision](data: List[List[String]], attribute: String => Attribute,
      decision: String => Decision): List[(List[Attribute], Decision)] = {
    data.map{row => (row.init map attribute, decision(row.last))}
  }
}