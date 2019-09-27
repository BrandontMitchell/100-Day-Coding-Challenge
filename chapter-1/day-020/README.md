# Day 020 - ArrayIntList

The purpose of this day is to learn how the `ArrayList` class works under the hood by implementing our own simplified version: `ArrayIntList`. For simplicity, this version only allows the user to store integers, but otherwise works the same. This day is really challenging, and so you can view it as more of an extra challenge if you feel lost. At the very least, look over and try to understand the solution for today's challenge.

Similiarly to when you implemented the `Point` class, today you will be implementing the `ArrayIntList` class. Here are the methods that you will need to implement:

* `size()`
  * returns an `int` representing how many elements are currently stored
* `get(int index)`
  * returns an `int` representing the value stored that the given index
* `set(int index, int value)`
  * sets the element at the given index to the given value
* `contains(int value)`
  * returns `true` if the given value appears anywhere in the `ArrayIntList` (`false` otherwise)
* `indexOf(int value)`
  * returns the index of the first occurrence of the given value
* `add(int value)`
  * appends the given value to the end of the `ArrayIntList`
* `add(int index, int value)`
  * inserts the given value at the given index, shifting over necessary elements to the right
* `remove(int index)`
  * removes the element stored at the given index, shifting over necessary elements to the left
* `clear()`
  * removes all elements from the `ArrayIntList`

## Starter Code

This day includes a single file in the starter-code folder titled `ArrayIntList.java`. This includes the
boilerplate structure of the `ArrayIntList` class.

It will be your job to implement the included methods. There are three helper methods defined for you:

```
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
```

The `toString` method will allow you to view the contents of the `ArrayIntList`. This will be useful for testing purposes. You don't use it explicitly; intead it allows you to just write:

```
System.out.println(name)
```

where name is the name of the `ArrayIntList`. This implicitly tells Java to go and execute the `toString` method.

`ensureCapacity` checks if the value passed in is greater than the size of the internal array. This would occur when someone tries to add an element and we've run out of space. In that case, it performs some internal modfication to make space that we will discuss later.

`checkIndex` checks if the given index is outside of the bounds of the internal array. This can be useful for making sure that the user provides valid indices when using the `set` and `get` methods.
  
## Getting Started

The reason that `ArrayIntList` works almost exactly like an array with some added features is because that's exactly what it is underneath the covers. `ArrayIntList` works by storing an array as a field and updating it accordingly. The reason you don't have to specify the initial size is because this it is arbitrarily chosen to start at 100. 

When the user tries to add a value and there is no more space left in the internal array, `ensureCapacity` will make another array of double the size, and all of the data is copied over to this new array. This ends up being the most efficient thing to do mathematically. 

`ArrayIntList` hides a lot of things from the users. For example, it has two fields: an integer `size` and an internal array `elementData` that is being used to store the data. However, the client has no idea that the internal array is there, and they don't care what size it is. What the client cares about is how many elements they currently have stored in the internal array. That's what the `size` field represents, not the current size of the internal array.

Many of the methods will be just a single line of code to implement. The harder methods are the ones that require you to modify the fields, since you need to remember to update the size accordingly, and not mess up the internal array. The hardest method to implement will be `add(int index, int value)`. In general, the more convenient the method is for the client, the harder it is for the implementer to write it.


