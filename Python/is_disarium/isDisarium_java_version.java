/*def is_disarium(n):
	
	i = 1
	arr = [] 
	for number in str(n):
		number = int(number) 
		number = number ** i 
		arr.append(number)
		i += 1 
	return sum(arr) == n
*/
public class DisariumNumber {
	public static boolean isDisarium(int n) {
		String stringN = new Integer(n).toString();
	  	
	  int sum = 0;	
	  for (int i=0; i<stringN.length(); i++){
		  	
			sum = sum + Integer.valueOf(stringN.charAt(i));
		}
	  	return true;
	}
}