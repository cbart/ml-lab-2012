package mlclass.run

import mlclass.io.{TypedCsv, CsvParsers}
import scalaz.Success


/**
 * @author cbart@students.mimuw.edu.pl (Cezary Bartoszuk)
 */
object RunNormalize {
  val csvParsers = new CsvParsers
  val typedCsv = new TypedCsv

  def main(args: Array[String]) {
    val Success(csv) = csvParsers.parseFile(args(0)).map(m => typedCsv.mapTypes(m.init, double, double))
    val measures = for ((t :: Nil, f) <- csv) yield (f - t)
    val maxMeasure = measures.max
    val normalizedMeasures = measures.map(_ - maxMeasure)
    normalizedMeasures foreach { m =>
      println("%1.8f".format(math.exp(m)))
    }
  }

  val double: String => Double = _.toDouble
}