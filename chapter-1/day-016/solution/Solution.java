import java.io.*;
import java.util.*;

public class Solution {

	public static final int MAX_SCORE = 101;
	
	public static void main(String[] args) throws FileNotFoundException {
		Scanner input = new Scanner(new File("data.txt"));
		
		int[] count = new int[MAX_SCORE + 1];
		while (input.hasNextInt()) {
			int score = input.nextInt();
			count[score]++;
		}
		
		for (int i = 0; i < count.length; i++) {
			System.out.print(i + ": ");
			for (int j = 1; j <= count[i]; j++) {
				System.out.print("*");
			}
			System.out.println();
		}
	}
}