import java.util.*;

public class Solution {
    
    public static void main(String[] args) {
        Scanner console = new Scanner(System.in);
        Random randy = new Random();
        int guesses = game(console, randy);
        
        System.out.println("It took you " + guesses + " guess(es)");
    }
    
    public static int game(Scanner console, Random randy) {
        int correctAnswer = randy.nextInt(100) + 1;
        int guesses = 0;

        System.out.println();
        System.out.println("I'm thinking of a number between 1 and " + 100 + "...");
        System.out.print("Next guess? ");
        int guess = console.nextInt();
        guesses++;
        
        while (guess != correctAnswer) {
            if (guess < correctAnswer) {
                System.out.println("Nope. It's higher.");
            } else {
                System.out.println("Nope. It's lower.");
            }
            
            System.out.print("Next guess? ");
            guess = console.nextInt();
            guesses++;
        }
        
        return guesses;
    }
    
}