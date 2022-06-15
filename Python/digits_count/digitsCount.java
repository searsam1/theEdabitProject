public class LongDigits {
	public static int digitsCount(long n) {
		n = Math.abs(n);
	  	int total = 1;
	  	while(n > 10){
		  total += 1;
		  n /= 10;
		}
	  return total;
	}
}