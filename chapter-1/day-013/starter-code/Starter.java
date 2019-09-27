import java.io.*;
import java.util.*;

public class Starter {

	public static void main(String[] args) throws FileNotFoundException {
		Scanner console = new Scanner(System.in);
          
          Scanner input = new Scanner(new File("madlib.txt"));
		PrintStream output = new PrintStream("output.txt");
          
		create(console, input, output);
          
          // uncomment the lines of code below once you're finished!
          
//        System.out.println();
// 		System.out.println("Your mad-lib has been created!");
//        System.out.println("Check the directory this program is located in");
//        System.out.println("for a file named output.txt");
// 		System.out.println();
	}
	
	public static void create(Scanner console, Scanner input, PrintStream output) {
		
          // your code goes here...
          
	}
}