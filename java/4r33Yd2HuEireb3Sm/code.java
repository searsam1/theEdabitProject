public class IntegerDigits {
	public static int count(int n) {
	  int total = 0;
	  if (n < 0) {n *= -1;}
	  while (n >= 1) {n /= 10; total ++;}
	  return total > 0 ? total : 1;
	}
}