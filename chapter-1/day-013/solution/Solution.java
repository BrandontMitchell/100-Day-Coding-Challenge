import java.io.*;
import java.util.*;

public class Solution {

	public static void main(String[] args) throws FileNotFoundException {
		Scanner console = new Scanner(System.in);
          
          Scanner input = new Scanner(new File("madlib.txt"));
		PrintStream output = new PrintStream("output.txt");
          
		create(console, input, output);
	}
	
	public static void create(Scanner console, Scanner input, PrintStream output) {
		while (input.hasNextLine()) {
			String line = input.nextLine();
			Scanner lineScanner = new Scanner(line);
			while (lineScanner.hasNext()) {
				String word = lineScanner.next();
				if (word.startsWith("<") && word.endsWith(">")) {
					word = word.replace("<", "");
                         word = word.replace(">", "");
					word = word.replace("-", " ");
					System.out.print("Please type a(n) " + word + ": ");
					String replacement = console.nextLine();
					output.print(replacement + " ");
				} else {
					output.print(word + " ");
				}
			}
			output.println();
		}
          System.out.println();
		System.out.println("Your mad-lib has been created!");
          System.out.println("Check the directory this program is located in");
          System.out.println("for a file named output.txt");
		System.out.println();
	}
}