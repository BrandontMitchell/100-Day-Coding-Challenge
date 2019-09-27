public class Starter {
     
	public static void main(String[] args) {
		Scanner console = new Scanner(System.in);
		intro();
		double sum = getTotal(console);
		
		// your code goes here...
	}
	
	public static void intro() {
	
		// your code goes here...
		
	}
	
	public static double getTotal() {
	
		// your code goes here...
		
	}
	
     
        // rounds the given value to two decimal places and returns the result.
	public static double round(double num) {
		return Math.round(num * 100.0) / 100.0;
	}
     
}
