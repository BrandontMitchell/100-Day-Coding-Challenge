import java.util.*;
import java.io.*;

public class Solution {

	public static void main(String[] args) throws FileNotFoundException {
		collapseSpaces();
		leetSpeak();
	}
     
     public static void collapseSpaces() throws FileNotFoundException {
          Scanner input = new Scanner(new File("messedup.txt"));
		PrintStream output = new PrintStream(new File("lincoln.txt"));
          
          while (input.hasNextLine()) {
          	String line = input.nextLine();
          	Scanner words = new Scanner(line);
     		while (words.hasNext()) {
     			output.print(words.next() + " ");
     		}
          	output.println();
          }
     }
     
     public static void leetSpeak() throws FileNotFoundException {
          Scanner input = new Scanner(new File("lincoln.txt"));
		PrintStream output = new PrintStream(new File("leet.txt"));
          
          while (input.hasNextLine()) {
          	String line = input.nextLine();
          	Scanner lineScanner = new Scanner(line);
          	while (lineScanner.hasNext()) {
          		String word = lineScanner.next();
          		word = word.replace("o", "0");
          		word = word.replace("l", "1");
          		word = word.replace("e", "3");
          		word = word.replace("a", "4");
          		word = word.replace("t", "7");
          		if (word.endsWith("s")) {
          			word = word.substring(0, word.length() - 1) + "Z";
          		}
          		output.print("(" + word + ") ");
          	}
          	output.println();
          }

     }
     
}