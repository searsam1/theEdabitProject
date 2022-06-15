public class Challenge {
	public static String sevenBoom(int[] arr) {
		for (int i : arr){
		  for (int n=0; n<String.valueOf(i).length(); n++){
			char c = String.valueOf(i).charAt(n);  
			if (c == '7'){
			  return "Boom!";
			}
		  }
		}
	  return "there is no 7 in the array";
	}
}
// Your First Program

class Challenge {
    public static void main(String[] args) {
        System.out.println("Hello, World!"); 
    }
}