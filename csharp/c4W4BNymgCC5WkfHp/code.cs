public class Program
    {
        public static string NameShuffle(string str)
        {
            return "";
        }
    }

TestsConsoleusing NUnit.Framework;



[TestFixture]

public class Tests

{

    [Test]

    [TestCase("Donald Trump", Result="Trump Donald")]

  [TestCase("Rosie O'Donnel", Result="O'Donnel Rosie")]

  [TestCase("Seymour Butts", Result="Butts Seymour")]

  [TestCase("Ebony Greene", Result="Greene Ebony")]

  [TestCase("Ken Kennedy", Result="Kennedy Ken")]

  [TestCase("Allison Gonzalez", Result="Gonzalez Allison")]

  [TestCase("Albert Frazier", Result="Frazier Albert")]

  [TestCase("Eloise Hopkins", Result="Hopkins Eloise")]

  [TestCase("Donnie Welch", Result="Welch Donnie")]

  [TestCase("Vernon Thomas", Result="Thomas Vernon")]

    public static string FixedTest(string str)

    {

        return Program.NameShuffle(str);

    }

}