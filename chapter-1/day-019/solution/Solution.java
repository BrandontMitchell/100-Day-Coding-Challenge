import java.util.*;

public class Solution {

     public static void main(String[] args) {
          ArrayList<Integer> list = new ArrayList<Integer>();
          list.add(5);
          list.add(4);
          list.add(3);
          list.add(2);
          list.add(1);
          System.out.println("List before: " + list);
          minToFront(list);
          System.out.println("List after:  " + list);
     }
     
     public static void minToFront(ArrayList<Integer> numbers) {
          int minValue = numbers.get(0);
          int minIndex = 0;
          for (int i = 1; i < numbers.size(); i++) {
               if (minValue > numbers.get(i)) {
                    minValue = numbers.get(i);
                    minIndex = i;
               }
          }
          numbers.remove(minIndex);
          numbers.add(0, minValue);
     }
     
}