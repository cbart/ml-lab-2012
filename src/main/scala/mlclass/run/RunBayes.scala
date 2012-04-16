package mlclass.run

import mlclass.io.{TypedCsv, CsvParsers}
import mlclass.classifier.bayes.Naive._
import mlclass.classifier.bayes.Naive


object RunBayes {
  val decision: String => Boolean = {
    case "T" => true
    case "F" => false
    case dec => throw new Exception("""Unknown decision found: "%s".""".format(dec))
  }

  val attribute: String => Int = _.toInt

  val trainingSet = (new CsvParsers).parseClasspath("/train.csv")
      .fold((s: String) => throw new Exception(s), identity)

  val typedTrainingSet = (new TypedCsv).mapTypes(trainingSet.tail, attribute, decision)

  lazy val testSet = (new CsvParsers).parseClasspath("/test.csv")
      .fold((s: String) => throw new Exception(s), identity)

  lazy val typedTestSet = testSet.tail.map(testSample => testSample.map(_.toInt))

  def main(args: Array[String]) {
    val classifier = Naive(typedTrainingSet, args(0).toDouble)
    val results = typedTestSet.map(classifier.classify _)
    results.foreach(wages => println("%s,%s".format(wages(true), wages(false))))
  }
}
