public class Solution {

     public static final int SIZE = 6;
     
     public static void main(String[] args) {
          section1();
          section2();
          section3();
          section4();
          section5();
     }
     
     public static void section1() {
          for (int line = 1; line <= SIZE; line++) {                                                     
               for (int spaces = 1; spaces <= -1 * line + (SIZE + 14); spaces++) {
                    System.out.print(" ");
               }
               for (int slashes = 1; slashes <= 2 * line - 1; slashes++) {
                    System.out.print("/");
               }
               for (int equals = 1; equals <= SIZE; equals++) {
                    System.out.print("=");
               }
               System.out.println();
          }
     }
     
     public static void section2() {
          for (int line = 1; line <= 3; line++) {
               for (int spaces = 1; spaces <= -1 * line + 14; spaces++) {
                    System.out.print(" ");
               }
               for (int slashes = 1; slashes <= SIZE; slashes++) {
                    System.out.print("/");
               }
               
               for (int pound = 1; pound <= 2 * line - 1; pound++) {
                    System.out.print("#");
               }
               for (int slashes = 1; slashes <= SIZE; slashes++) {
                    System.out.print("/");
               }
               for (int equals = 1; equals <= SIZE; equals++) {
                    System.out.print("=");
               }
               System.out.println();
          }
     }
     
     public static void section3() {
          for (int line = 1; line <= 6; line++) {
               for (int spaces = 1; spaces <= -1 * line + 11; spaces++) {
                    System.out.print(" ");
               }
               for (int slashes = 1; slashes <= SIZE; slashes++) {
                    System.out.print("/");
               }
               for (int pound = 1; pound <= 6; pound++) {
                    System.out.print("#");
               }
               for (int pound = 1; pound <= 2 * line - 1; pound++) {
                    System.out.print(" ");
               }
               for (int slashes = 1; slashes <= SIZE; slashes++) {
                    System.out.print("/");
               }
               for (int equals = 1; equals <= SIZE; equals++) {
                    System.out.print("=");
               }
               System.out.println();
          }
     }
     
     public static void section4() {
          for (int line = 1; line <= 3; line++) {
               for (int spaces = 1; spaces <= -1 * line + 5; spaces++) {
                    System.out.print(" ");
               }
               for (int slashes = 1; slashes <= SIZE; slashes++) {
                    System.out.print("/");
               }
               for (int pound = 1; pound <= 6; pound++) {
                    System.out.print("#");
               }
               for (int equals = 1; equals <= 2 * line + (2 * SIZE + 11); equals++) {
                    System.out.print("=");
               }
               System.out.println();
          }
     }
     
     public static void section5() {
          for (int line = 1; line <= SIZE / 2; line++) {
               for (int spaces = 1; spaces <= line; spaces++) {
                    System.out.print(" ");
               }
               for (int slashes = 1; slashes <= -2 * line + (SIZE + 2); slashes++) {
                    System.out.print("/");
               }
               for (int pound = 1; pound <= 2 * SIZE + 24; pound++) {
                    System.out.print("#");
               }
               System.out.println();
          }
     }
}