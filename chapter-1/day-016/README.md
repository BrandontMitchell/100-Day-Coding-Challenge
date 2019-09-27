# Day 016 - Arrays Cont'd

The purpose of this day is to continue to practice and get more comfortable with array syntax. Arrays are an incredibly important programming concept, and end up being foundational to a lot of other more complex concepts.

For this challenge, you will be analyzing data to generate a [histogram](https://www.mathsisfun.com/data/histograms.html). The solution for today's challenge will be relatively short, but produce a cool result and really test your understanding of array syntax.

Here's what your output should look like:

```
0: 
1: 
2: 
3: 
4: 
5: 
6: 
7: 
8: *
9: 
10: 
11: 
12: 
13: 
14: 
15: 
16: 
17: 
18: 
19: 
20: *
21: 
22: 
23: 
24: *
25: *
26: *
27: 
28: *
29: 
30: *
31: 
32: **
33: 
34: 
35: 
36: **
37: **
38: **
39: 
40: **
41: *
42: **
43: *
44: **
45: **
46: **
47: 
48: ***
49: *
50: *
51: **
52: ****
53: *
54: 
55: 
56: 
57: **
58: **
59: **
60: **
61: *
62: *****
63: ***
64: *****
65: *
66: **
67: *****
68: ******
69: **
70: *******
71: ******
72: *******
73: ************
74: *********
75: ***********
76: ******
77: ***************
78: ************
79: ****************
80: ******************
81: *********
82: **********
83: ******************
84: ************************
85: *************
86: *******************
87: ****************
88: *****************************
89: *********************
90: **************
91: ******************
92: *******************
93: ****************
94: *********
95: ********
96: *******
97: *********
98: ********
99: *******
100: ***
101: 
```

This was an example my professor used with actual test scores in front of the entire class. 

## Starter Code

This day includes a single Java file in the starter-code folder titled `Starter.java`. The other file `data.txt` contains test scores. Each test score is between 0 and 101 and appears on it's own line. You can open up and view the data file if this is unclear, but do not modify it's contents.

Your job will be to read through the input file and use an array to store information about how many people got each score. From this information, you will be able to generate your histogram.
  
## Getting Started

There are no extra concepts being covered today, but we will provide some development strategies in terms of how to approach the problem.

1. Create an array with size big enough to hold one index for each test score.

2. Process the `data.txt` file, incrementing the respective index in the array with one count of the current test score. In other words, if you see a 42, in the input file, then you should increment the value in index 42.

3. Traverse through the array with a for loop, and for each index: print out the current index followed by a colon, and then print out ***n*** stars where ***n*** is the value stored at that index. (Think back to ASCII art). 




