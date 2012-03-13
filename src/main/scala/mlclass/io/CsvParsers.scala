package mlclass.io

import scala.util.parsing.combinator.RegexParsers
import scala.util.parsing.input.{StreamReader, Reader}
import scalaz.Validation
import java.io.{File, FileInputStream, InputStreamReader, BufferedReader}


/**
 * @author cbart@students.mimuw.edu.pl (Cezary Bartoszuk)
 */
class CsvParsers extends RegexParsers {
  override val skipWhitespace = false
  private[this] val comma: Parser[String] = ","

  private[this] val dQuote: Parser[String] = "\""

  private[this] val escDQuote: Parser[String] = "\"\"" ^^ { case _ => "\"" }

  private[this] val br: Parser[String] = "\r\n" | "\n"

  private[this] val text: Parser[String] = "[^\",\r\n]".r

  private[this] val space: Parser[String] = "[ \t]+".r

  private[this] val nonEscaped: Parser[String] = (text*) ^^ (_.mkString)

  private[this] val escaped: Parser[String] =
    ((space?) ~> dQuote ~> ((text | comma | br | escDQuote)*) <~ dQuote <~ (space?)) ^^ (_.mkString)

  private[this] val field: Parser[String] = escaped | nonEscaped

  private[this] val record: Parser[List[String]] = repsep(field, comma)

  private val file: Parser[List[List[String]]] = repsep(record, br) <~ (br?)

  def parse(s: Reader[Char]): Validation[String, List[List[String]]] = parseAll(file, s) match {
    case Success(res, _) => scalaz.Success(res)
    case Failure(msg, next) => scalaz.Failure("%s\n%s".format(msg, next.pos.longString))
  }

  def parseClasspath(filename: String): Validation[String, List[List[String]]] = parse {
    val stream = getClass.getResourceAsStream(filename)
    StreamReader(new BufferedReader(new InputStreamReader(stream)))
  }

  def parseFile(filename: String): Validation[String, List[List[String]]] = parse {
    val stream = new FileInputStream(new File(filename))
    StreamReader(new BufferedReader(new InputStreamReader(stream)))
  }
}