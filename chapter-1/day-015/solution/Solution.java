public class Solution {
     
     public static void main(String[] args) {
          
          for (int i = 0; i < args.length; i++) {
               String argument = args[i];
               for (int j = argument.length() - 1; j >= 0; j--) {
                    System.out.print(argument.charAt(j));
               }
               System.out.println();
          }
          
     }
     
}