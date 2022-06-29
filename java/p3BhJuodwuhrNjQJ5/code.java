import java.util.Arrays;

public class Pythagorean {	
	public static boolean isTriplet(int a, int b, int c) {
		int[] arr = {a,b,c};
	 	Arrays.sort(arr);
	  	a = arr[0]; b = arr[1]; c = arr[2];
	  	return (a*a) + (b*b) == (c*c);
	}
}