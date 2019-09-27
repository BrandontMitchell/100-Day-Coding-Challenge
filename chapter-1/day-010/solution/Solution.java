import java.util.*;

public class Solution {
    public static final int MAX = 100;
    
    public static void main(String[] args) {
        Scanner console = new Scanner(System.in);
        Random randy = new Random();

        int games = 0;
        int totalGuesses = 0;
        int best = Integer.MAX_VALUE;
        String answer = "y";
               
        while (answer.equals("y")) {
            int guesses = game(console, randy);
            totalGuesses += guesses;
            games++;
            best = Math.min(best, guesses);
            
            System.out.print("Play again? (y/n) ");
            answer = console.next();
            while (!(answer.equals("y") || answer.equals("n"))) {
               System.out.println("Oops. Please type either 'y' or 'n'");
               System.out.print("Play again? (y/n) ");
               answer = console.next();
            }
       }
        
        printStats(games, totalGuesses, best);
    }
    
    public static int game(Scanner console, Random randy) {
        int correctAnswer = randy.nextInt(MAX) + 1;
        int guesses = 0;

        System.out.println();
        System.out.println("I'm thinking of a number between 1 and " + MAX + "...");
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

        System.out.println("You guessed it in " + guesses + " tries!");
        
        return guesses;
    }
    
    public static void printStats(int games, int guesses, int best) {
        System.out.println();
        System.out.println("Statistics:");
        System.out.println("Games   = " + games);
        System.out.println("Guesses = " + guesses);
        System.out.println("Best Game     = " + best);
    }
}