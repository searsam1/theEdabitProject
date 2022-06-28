public class Program
{
	public static string FizzBuzz(int n)
	{
	  if (n % 15 == 0){
		return "FizzBuzz";
	  }
	  if (n % 3 == 0){
		return "Fizz";
	  }
	  if (n % 5 == 0){
		return "Buzz";
	  }
	  return n.ToString();
	}
}

TestsConsoleusing NUnit.Framework;

using System;



[TestFixture]

public class Tests

{

		[Test]

		[TestCase(3, Result="Fizz")] 

		[TestCase(5, Result="Buzz")]

		[TestCase(15, Result="FizzBuzz")]

		[TestCase(98, Result="98")]

		[TestCase(10, Result="Buzz")]

		[TestCase(4, Result="4")]

		public static string FizzBuzz(int n)

		{

			Console.WriteLine($"Input: {n}");

			return Program.FizzBuzz(n);

		}

}