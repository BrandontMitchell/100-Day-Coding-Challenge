import java.awt.*;

public class Starter {

	public static void main(String[] args) {
		DrawingPanel panel = new DrawingPanel(400, 200);
		Graphics g = panel.getGraphics();
		
		drawCar(g, 10, 30);
		drawCar(g, 150, 10);
	}
	
	// draws a car with a black body, a blue window, and red wheels at the given loction.
	// Graphics g: the Graphics object to use when drawing
	// int x: the x-coordinate of the top-left corner of the drawn car
	// int y: the y-coordinate of the top-left corner of the drawn car
	public static void drawCar(Graphics g, int x, int y) {
		
          // your code goes here...
	}
}