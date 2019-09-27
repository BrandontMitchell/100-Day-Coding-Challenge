import java.util.*;

public class Solution {
	
	public static void main(String[] args) {
		Scanner console = new Scanner(System.in);
		
		intro();
		
		double deposits = getTotal(console, "deposit");
		double withdrawals = getTotal(console, "withdrawal");
		
		reportResults(deposits, withdrawals);
		printMessage(deposits - withdrawals);
	}
	
	public static void intro() {
		System.out.println("Please enter your deposits and withdrawals");
		System.out.println("to calculate your net monthly income.");
		System.out.println();
	}
	
	public static double getTotal(Scanner console, String type) {
		System.out.print("How many " + type + "s? ");
		int count = console.nextInt();
		
		double total = 0;
		for (int i = 0; i < count; i++) {
			System.out.print("    Next " + type + " amount? $");
			total += console.nextDouble();
		}
		System.out.println();
		
		return total;
	}
	
	public static void reportResults(double deposits, double withdrawals) {
		System.out.println("Total deposits    = $" + round(deposits));
		System.out.println("Total withdrawals = $" + round(withdrawals));
		System.out.println();
		
		double difference = Math.abs(deposits - withdrawals);
		if (deposits <= withdrawals) {
			System.out.println("You withdrew $" + round(difference) + " more than you deposited this month.");
		} else {
			System.out.println("You deposited $" + round(difference) + " more than you withdrew this month.");
		}
	}
	
	public static void printMessage(double diff) {
		if (diff <= -500) {
			System.out.println("You withdrew a lot of money this month!");
		} else if (diff <= 0) {
			System.out.println("You withdrew a decent amount of money this month.");
		} else if (diff <= 500) {
			System.out.println("You deposited a decent amount of money this month.");
		} else {   // diff > 500
			System.out.println("You deposited a lot of money this month!");
		}
	}
	
	// rounds the given value to two decimal places and returns the result.
	public static double round(double num) {
		return Math.round(num * 100.0) / 100.0;
	}
}