public class NumericString {
	public static String add(String a, String b) {
		
	  	if (a == "" || a == null){
		  return "Invalid Operation";
		}
	  
	  	int intA = Integer.valueOf(a);
	  	int intB = Integer.valueOf(b);
	  	int res = intA + intB;
	  	String str = String.valueOf(res);
	  	return str;
	}
}