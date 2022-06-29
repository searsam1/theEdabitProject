using System;
using System.Linq;
public class Program {
	public static double ParallelResistance(double[] arr) {
        double sum = 0.0;
        foreach (double item in arr) {
            sum += (1.0/item);
        }
	  return Math.Round(1.0 / sum, 1);
	}
}