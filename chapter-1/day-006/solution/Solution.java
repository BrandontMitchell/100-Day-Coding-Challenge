// Example Solution

import java.awt.*;

public class Solution {
	public static void main(String[] args) {
		DrawingPanel panel = new DrawingPanel(400, 200);
		Graphics g = panel.getGraphics();
		
		panel.setBackground(Color.LIGHT_GRAY);
		drawCar(g, 10, 30, 100);
		drawCar(g, 150, 10, 50);
		
		// note that this for loop starts at 0!  This is not something that is required, but
		// oftentimes for loops with the loop variable initialized to 0 can make coordinate / pixel
		// math a little bit simpler!
		for (int i = 0; i < 50; i++) {
			panel.sleep(10);
			panel.clear();
			drawCar(g, i * 5 + 10, 130, 40);
		}
	}
	
	// Draws a car with a black body, a blue window, and red wheels at the given loction.
	// Graphics g: the Graphics object to use when drawing
	// int x: the x-coordinate of the top-left corner of the drawn car
	// int y: the y-coordinate of the top-left corner of the drawn car
	// int size: the size of the drawn car (must be a multiple of 10)
	public static void drawCar(Graphics g, int x, int y, int size) {
		// remember: we needed to both scale the size of each element of the figure (the body of the
		//             van, the window, both wheels) as well as the distance from the corner of the
		//             van! See the inked drawings on the course website for intuition about how we
		//             worked out this coordinate / pixel math.
		
		// body of car
		g.setColor(Color.BLACK);
		g.fillRect(x, y, size, size / 2);
		
		// window
		g.setColor(Color.CYAN);
		g.fillRect(x + size * 7 / 10, y + size / 10, size * 3 / 10, size / 5);
		
		// wheels
		g.setColor(Color.RED);
		g.fillOval(x + size / 10, y + size * 4 / 10, size / 5, size / 5);
		g.fillOval(x + size * 7 / 10, y + size * 4 / 10, size / 5, size / 5);
	}
}