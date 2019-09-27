import java.util.*;

public class Solution {
	
	public static void main(String[] args) {
		Scanner console = new Scanner(System.in);
		
          intro();
		double sum = getTotal(console);
		
		System.out.println("Total     = " + round(sum));
	}
     
     public static void intro() {
		System.out.println("Please enter any numbers");
		System.out.println("to calculate the overall sum.");
		System.out.println();
	}
	
	public static double getTotal(Scanner console) {
		System.out.print("How many numbers? ");
		int count = console.nextInt();
		
		double total = 0;
		for (int i = 0; i < count; i++) {
			System.out.print("    Next number? ");
			total += console.nextDouble();
		}
		System.out.println();
		
		return total;
	}
	
	// rounds the given value to two decimal places and returns the result.
	public static double round(double num) {
		return Math.round(num * 100.0) / 100.0;
	}
}