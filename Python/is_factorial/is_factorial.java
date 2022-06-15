public class Program {
	public static boolean isFactorial(int n) {
		for (int i=1; i<n; i++){
			if(n % i != 0){
			  return false;
			}

		  	n = n / i;
			  
		}
	  return true;
	}
}