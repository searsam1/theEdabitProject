public class Program
{
    public static int HammingDistance(string str1, string str2)
    {
    }
}

TestsConsoleusing NUnit.Framework;



[TestFixture]

public class Tests

{

  [Test]

  [TestCase("abcde", "bcdef", Result=5)]

  [TestCase("abcde", "abcde", Result=0)]

  [TestCase("strong", "strung", Result=1)]

    public static int FixedTest(string str1, string str2)

    {

        return Program.HammingDistance(str1, str2);

    }

}