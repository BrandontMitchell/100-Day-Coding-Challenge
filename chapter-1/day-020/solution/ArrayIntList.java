public class ArrayIntList {

	private int[] elementData;  // all the numbers in the list
	private int size;           // how many numbers a client thinks there are
	
	public static final int DEFAULT_CAPACITY = 100;
	
	public ArrayIntList() {
		this(DEFAULT_CAPACITY);
	}
	
	public ArrayIntList(int initialCapacity) {
		elementData = new int[initialCapacity];
		size = 0;
	}
	
	public int size() {
		return size;
	}
	
	public int get(int index) {
		checkIndex(index);
		return elementData[index];
	}
	
	public void set(int index, int value) {
		checkIndex(index);
		elementData[index] = value;
	}
	
	public boolean contains(int value) {
		return (indexOf(value) >= 0);
	}
	
	public int indexOf(int value) {
		for (int i = 0; i < size; i++) {
			if (elementData[i] == value) {
				return i;
			}
		}
		return -1;
	}
	
	public void add(int value) {
		add(size, value);
	}
	
	public void add(int index, int value) {
		if (index < 0 || index > size) {
			throw new IndexOutOfBoundsException("index: " + index);
		}
		ensureCapacity(size + 1);
		for (int i = size; i > index; i--) {
			elementData[i] = elementData[i - 1];
		}
		elementData[index] = value;
		size++;
	}
	
	public void remove(int index) {
		checkIndex(index);
		for (int i = index; i < size - 1; i++) {
			elementData[i] = elementData[i + 1];
		}
		size--;
	}
	
	public void clear() {
		size = 0;
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
	
	public void ensureCapacity(int capacity) {
		if (capacity > elementData.length) {
			capacity = Math.max(capacity, elementData.length * 2);
			int[] newList = new int[capacity];
			for (int i = 0; i < size; i++) {
				newList[i] = elementData[i];
			}
			elementData = newList;
		}
	}
	
	private void checkIndex(int index) {
		if (index < 0 || index >= size) {
			throw new IndexOutOfBoundsException("index: " + index);
		}
	}
}
