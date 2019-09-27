import java.awt.*;

public class Starter {

	public static void main(String[] args) {
		DrawingPanel panel = new DrawingPanel(400, 200);
		Graphics g = panel.getGraphics();
		
          // note: feel free to play around with the numbers in this for loop
		for (int i = 0; i < 50; i++) {
			panel.sleep(10);
			panel.clear();
			draw(g, i * 5 + 10, 130, 40);
		}
	}
	
	public static void draw(Graphics g, int x, int y, int size) {
		
          // your code goes here...
          
	}
}