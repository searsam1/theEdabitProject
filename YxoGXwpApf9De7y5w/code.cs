public class Program {
	public static int CountDs(string str)
	{
		
	}
}

TestsConsoleusing NUnit.Framework;



public class Tests

{

	  [Test]

	  [TestCase("My friend Dylan got distracted at school", Result=4)]

	  [TestCase("Debris was scattered all over the place.", Result=2)]

	  [TestCase("The rodents hibernated in their den.", Result=3)]

	  

	  public static int FixedTest(string str)

		{

			 return Program.CountDs(str);

		}

}