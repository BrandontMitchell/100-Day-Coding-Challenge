public class Solution {
	
     public static void main(String[] args) {
		
		Point p1 = new Point(3, 5);
		System.out.println("Point p1: " + p1);
		
		Point p2 = new Point(-500, 4);
		System.out.println("Point p2: " + p2);
		
		Point p3 = new Point();
		System.out.println("Point p3: " + p3);
		
		System.out.println("After translate:");
		p1.translate(-1, -2);
		p2.translate(-500, 15);
		
		System.out.println("Point p1: " + p1);
		System.out.println("Point p2: " + p2);
		
		System.out.println("Point p1's distance from origin: " + p1.distanceFromOrigin());
		System.out.println("Point p2's distance from origin: " + p2.distanceFromOrigin());
		
		System.out.println("Distance from p1 to p2: " + p1.distanceFrom(p2));
		System.out.println("Distance form p2 to p1: " + p2.distanceFrom(p1));
		
		System.out.println("The sum of p1's coordinates is " + (p1.getX() + p1.getY());
          
		p3.setLocation(100, 100);
		System.out.println("Point p3 after setLocation: " + p3);
	}
}