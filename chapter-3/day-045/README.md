# Day 045 - DOM Manipulation

The purpose of this day is to continue to get practice with JavaScript and DOM manipulation. You will be creating a two-player tic-tac-toe game. It will use many of the same concepts as the previous day's challenge. The two players will take turns using the mouse to click on the grid indicating their move. When the game is finished, an alert message will popup indicating who won the game, or announce that it was a draw if neither player won.

## Starter Code

This day includes three files in the starter-code folder. These include `starter.html`, `starter.css` and `starter.js`.

There are two important pieces of information about the `starter.html` file to note. 

1. All of the empty spaces in the grid have the class name `box`.

2. The boxes each of their own unique `id`. They are named `(top|middle|bottom)-(left|middle|right)`.

Other than this, you can safely ignore this file, as well as `starter.css`.

There are some helpful functions and global variables defined for you in the `starter.js` file that give you a good foundational start. Although it's not required that you use these functions, it will save you a lot of time and typing.

There are three global variables that have been declared for you:

1. `board`: An array keeping track of the current state of the game. Each value in the array will either be an empty string, and `X` or an `O`. This is later used to check if a player is winning the game. Index 0 corresponds to the `top-left` of the board, index 1 corresponds to the `top-middle` position in the board, and so on.

2. `POSITIONS`: This constant is an array containing the `id` of each square in the grid. This can be helpful in mapping the indices of the `board` array to the `id` of the boxes, or vice-versa.

3. `currPlayer`: This String keeps track of who the current player is. It is initially `X`, and then alternates between `O` and `X` on each subsequent turn.

There are four helper functions defined for you in the `starter.js` file.

1. `isFull` returns `true` of the board has no empty spaces left.

2. `switchPlayer` toggles the value of the `currPlayer` global variable between `X` and `O`.

3. `winning` returns `true` if the given player is in a winning board state.

4. `$` as always serves as shorthand for `document.getElementById`

Your job will be to implement the `initBoard` function which is in charge of giving functionality to the rematch button, as well as the responsiveness of each of the squares.
  
## Getting Started
  
There is no new information for today, but there are some useful tips we will provide. In order to populate the squares with either `X` or `O`, you will be using:

```
box.firstElementChild.innerHTML
```

where `box` is the DOM element representing the desired square.

Here's a suggested development strategy:

1. Make each of the boxes show an `alert` when you click on them.

2. Modify the `onclick` event handler of each of the boxes to alternate between `X` and `O`.

3. Add functionality to the rematch button. It should clear all of the tiles.

4. Set it up so the game alerts you when a player has won. Hint: check the state of the board after each move with the `winning` function.

5. Make it so that you can't keep playing after the game has ended, unless you click rematch. Hint: use an if statement.




