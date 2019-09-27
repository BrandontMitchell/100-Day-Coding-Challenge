import java.util.*;
import java.io.*;

public class Starter {

	public static void main(String[] args) throws FileNotFoundException {
		collapseSpaces();
		leetSpeak();
	}
     
     public static void collapseSpaces() throws FileNotFoundException {
          Scanner input = new Scanner(new File("messedup.txt"));
		PrintStream output = new PrintStream(new File("lincoln.txt"));
          
          // your code goes here...
     }
     
     public static void leetSpeak() throws FileNotFoundException {
          Scanner input = new Scanner(new File("lincoln.txt"));
		PrintStream output = new PrintStream(new File("leet.txt"));
          
          // your code goes here...
     }
     
}