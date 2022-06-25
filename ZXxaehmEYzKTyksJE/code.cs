using System.Linq;
public class Program {
	public static string SeriesResistance(double[] arr) {
		
	}
}

TestsConsoleusing System;

using NUnit.Framework;



[TestFixture]

public class Tests {

	[Test]

	[TestCase(new double[] {1, 5, 6, 3}, Result="15 ohms")]

	[TestCase(new double[] {0.2, 0.3, 0.4}, Result="0.9 ohm")]

	[TestCase(new double[] {10,12, 1, 10}, Result="33 ohms")]

	[TestCase(new double[] {10,13, 3.8, 20, 10}, Result="56.8 ohms")]

	[TestCase(new double[] {0.5, 0.5}, Result="1 ohm")]

	[TestCase(new double[] {16, 30, 22.8, 4}, Result="72.8 ohms")]

	[TestCase(new double[] {20, 15, 32.5, 2}, Result="69.5 ohms")]

	[TestCase(new double[] {52, 22, 20, 30}, Result="124 ohms")]

	[TestCase(new double[] {10, 12, 32, 4.9, 5, 6, 71}, Result="140.9 ohms")]

	

	public static string SeriesResistance(double[] arr) {

		Console.WriteLine($"Input: {0}", arr);

		return Program.SeriesResistance(arr);

	}

}