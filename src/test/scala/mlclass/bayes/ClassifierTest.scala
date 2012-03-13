package mlclass.bayes

import mlclass.io.{TypedCsv, CsvParsers}
import mlclass.classifier.bayes.Naive
import org.junit.{Ignore, Test}


/**
 * @author cbart@students.mimuw.edu.pl (Cezary Bartoszuk)
 */
class ClassifierTest {
  val decision: String => Boolean = {
    case "T" => true
    case "F" => false
    case dec => throw new Exception("""Unknown decision found: "%s".""".format(dec))
  }

  val attribute: String => Int = _.toInt

  val trainingSet = (new CsvParsers).parseClasspath("/train.csv")
      .fold((s: String) => throw new Exception(s), identity)

  val typedTrainingSet = (new TypedCsv).mapTypes(trainingSet.tail, attribute, decision)

  val testSet = (new CsvParsers).parseClasspath("/test.csv")
      .fold((s: String) => throw new Exception(s), identity)

  val typedTestSet = testSet.tail.map(testSample => testSample.map(_.toInt))

  val classifier = Naive(typedTrainingSet, 0.01)

  @Ignore @Test def shouldClassify() {
    val classified = typedTestSet.par.map(classifier.classify _)
    println(classified)
  }
}