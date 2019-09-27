import java.awt.*;

public class Solution {

	public static void main(String[] args) {
		DrawingPanel panel = new DrawingPanel(400, 200);
		Graphics g = panel.getGraphics();
		
		panel.setBackground(Color.LIGHT_GRAY);
		drawCar(g, 10, 30);
		drawCar(g, 150, 10);
	}
	
	// draws a car with a black body, a blue window, and red wheels at the given loction.
	// Graphics g: the Graphics object to use when drawing
	// int x: the x-coordinate of the top-left corner of the drawn car
	// int y: the y-coordinate of the top-left corner of the drawn car
	public static void drawCar(Graphics g, int x, int y) {
		// body of car
		g.setColor(Color.BLACK);
		g.fillRect(x, y, 100, 50);
		
		// window
		g.setColor(Color.CYAN);
		g.fillRect(x + 70, y + 10, 30, 20);
		
		// wheels
		g.setColor(Color.RED);
		g.fillOval(x + 10, y + 40, 20, 20);
		g.fillOval(x + 70, y + 40, 20, 20);
	}
}