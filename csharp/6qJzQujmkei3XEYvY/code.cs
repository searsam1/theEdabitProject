using System;
using System.Linq;
public class Program {
	public static double ParallelResistance(double[] arr) {
		
	}
}

TestsConsoleusing System;

using NUnit.Framework;



[TestFixture]

public class Tests {

	[Test]

	[TestCase(new double[] {6, 3}, Result=2)]

	[TestCase(new double[] {6, 3, 6}, Result=1.5)]

	[TestCase(new double[] {10, 10}, Result=5)]

	[TestCase(new double[] {10, 20, 10}, Result=4)]

	[TestCase(new double[] {60, 30, 20}, Result=10)]

	[TestCase(new double[] {16, 4}, Result=3.2)]

	[TestCase(new double[] {20, 5}, Result=4)]

	[TestCase(new double[] {500, 500, 500}, Result=166.7)]

	[TestCase(new double[] {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, Result=0.3)]

	

	public static double ParallelResistance(double[] arr) {

		Console.WriteLine($"Input: {0}", arr);

		return Program.ParallelResistance(arr);

	}

}



// Author: Joshua Señoron