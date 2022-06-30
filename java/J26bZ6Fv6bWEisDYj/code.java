import java.lang.Math;
public class SideLengths {
  public static double[] otherSides(int n) {
		double[] res = new double[2];
		res[0] = n*2;
		res[1] = Math.sqrt(3) * n;
	return res;
  }
}