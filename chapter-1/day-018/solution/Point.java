public class Point {
	
	private int x;
	private int y;
	
	public Point(int x, int y) {
		this.x = x;
		this.y = y;
	}
	
	public Point() {
		this.x = 0;
		this.y = 0;
	}
	
	public void translate(int dx, int dy) {
		x += dx;
		y += dy;
	}
	
	public double distanceFromOrigin() {
		return Math.sqrt(Math.pow(x, 2) + Math.pow(y, 2));
	}
	
	public String toString() {
		return "(" + x + ", " + y + ")";
	}
	
	public double distanceFrom(Point otherPoint) {
		double xTerm = Math.pow(x - otherPoint.x, 2);
		double yTerm = Math.pow(y - otherPoint.y, 2);
		return Math.sqrt(xTerm + yTerm);
	}
	
	public int getX() {
		return x;
	}
	
	public int getY() {
		return y;
	}
	
	public void setLocation(int x, int y) {
		this.x = x;
		this.y = y;
	}
}