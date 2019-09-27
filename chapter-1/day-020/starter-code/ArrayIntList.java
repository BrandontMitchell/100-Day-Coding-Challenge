public class ArrayIntList {

	private int[] elementData;  // all the numbers in the list
	private int size;           // how many numbers a client thinks there are
	
	public static final int DEFAULT_CAPACITY = 100;
	
	public ArrayIntList() {
     
	}
	
	public int size() {
     
	}
	
	public int get(int index) {
     
	}
	
	public void set(int index, int value) {
     
	}
	
	public boolean contains(int value) {
     
	}
	
	public int indexOf(int value) {
		
	}
	
	public void add(int value) {
		
	}
	
	public void add(int index, int value) {
		
	}
	
	public void remove(int index) {
		
	}
	
	public void clear() {
		
	}
	
	public String toString() {
		if (size == 0) {
			return "[]";
		} else {
			String result = "[" + elementData[0];
			for (int i = 1; i < size; i++) {
				result += ", " + elementData[i];
			}
			result += "]";
			return result;
		}
	}
	
	private void checkCapacity(int capacity) {
		if (capacity > elementData.length) {
			throw new IllegalStateException("would exceed list capacity");
		}
	}
	
	private void checkIndex(int index) {
		if (index < 0 || index >= size) {
			throw new IndexOutOfBoundsException("index: " + index);
		}
	}
}
