package mlclass

import spock.lang.Specification

/**
 * @author cbart@students.mimuw.edu.pl (Cezary Bartoszuk)
 */
class ExampleTest extends Specification {
  def "length of Spock's and his friends' names"() {
    expect: name.size() == length
    where:
      name     | length
      "Spock"  | 5
      "Kirk"   | 4
      "Scotty" | 6
    }
}
