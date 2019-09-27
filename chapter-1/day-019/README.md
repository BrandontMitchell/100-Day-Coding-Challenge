# Day 019 - ArrayList

The purpose of this day is to introduce your first [abstract data type](https://en.wikipedia.org/wiki/Abstract_data_type): `ArrayList`. `ArrayList` is basically like if you took everything that was wrong with arrays and fixed it. Arrays can be cumbersome to work with sometimes because they are of fixed size, and you need to know how much space you're going to need ahead of time. You also can't insert elements at specific indices. `ArrayList` fixes all of these problems.

For this challenge, you will be implementing a method called `minToFront`. This method takes an `ArrayList` of integers as a parameter and moves the minimum value in the list to the front, otherwise preserving the order of the elements. For example, if a variable called `list` stores the following values: {3, 8, 92, 4, 2, 17, 9} and you make this call: `minToFront(list);` it should store the following values after the call: {2, 3, 8, 92, 4, 17, 9}. You may assume that the ArrayList stores at least one value.

## Starter Code

This day includes a single file in the starter-code folder titled `Starter.java`. This includes simple testing code that will construct an ArrayList that stores the following values: {1, 2, 3, 4, 5}. It prints out the contents of the `ArrayList` before and after execution of the method.

All of the code you write will go inside the `minToFront` method.
  
## Getting Started

`ArrayList` is exactly like a regular array, except for the syntax and the fact that it is flexible. Flexible means that the size of the `ArrayList` will grow as you need it to. If you add elements to the `ArrayList` one at at time, there is not really a concept of running out of space. It offers as much space as you need to store elements. However, you can still get an `IndexOutOfBoundsException` by trying to access an element not within the valid range of stored values.

The easiest way to teach `ArrayList` syntax is to compare and contrast with arrays, since you already know array syntax.

| Array Syntax  | ArrayList Syntax        |
| ------------- | ----------------------- |
| String\[] a   | ArrayList\<String\> list  |
| a.length      | list.size()             |
| a[i]          | list.get(i)             |
| a[i] = value  | list.set(i, value)      |
  
### New Methods

* `list.add(value)`
  * appends the given value to the end of the list
* `list.add(i, value)`
  * insert the given value at the given index, shift everything else over
* `list.remove(i)`
  * remove the value at index i, shift everything over
  
While the reasoning for this won't be covered in this chapter, you must use the `Integer` and `Double` wrapper classes when declaring `ArrayList` to hold `int` and `double`.
  
| Array Syntax  | ArrayList Syntax         |
| ------------- | ------------------------ |
| int\[]        | ArrayList\<Integer\> list  |
| double\[]     | ArrayList\<Double\> list   |


