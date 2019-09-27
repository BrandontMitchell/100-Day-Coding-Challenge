"use strict";

(function() {

     let board = ["", "", "", "", "", "", "", "", ""];
     const POSITIONS = ["top-left", "top-middle", "top-right", "middle-left", "middle-middle", "middle-right", "bottom-left", "bottom-middle", "bottom-right"];
     let currPlayer = "X";

     window.onload = function() {
          // initBoard();
     };

     // returns true if there are no moves left
     function isFull(boardCopy) {
          let count = 0;
          for (let i = 0; i < boardCopy.length; i++) {
               if (boardCopy[i] == "") {
                    return false;
               }
          }
          return true;
     }

     // switches the currPlayer global variable
     function switchPlayer() {
          if (currPlayer == "X") {
               currPlayer = "O";
          } else { // player == "O"
               currPlayer = "X";
          }
     }

     // returns true if the given player is in a winning board state
     function winning(boardCopy, player) {
          if ( (boardCopy[0] == player && boardCopy[1] == player && boardCopy[2] == player) ||
               (boardCopy[3] == player && boardCopy[4] == player && boardCopy[5] == player) ||
               (boardCopy[6] == player && boardCopy[7] == player && boardCopy[8] == player) ||
               (boardCopy[0] == player && boardCopy[3] == player && boardCopy[6] == player) ||
               (boardCopy[1] == player && boardCopy[4] == player && boardCopy[7] == player) ||
               (boardCopy[2] == player && boardCopy[5] == player && boardCopy[8] == player) ||
               (boardCopy[0] == player && boardCopy[4] == player && boardCopy[8] == player) ||
               (boardCopy[2] == player && boardCopy[4] == player && boardCopy[6] == player) ) {
               return true;
          }
          return false;
     }

     // returns the DOM element of the given id
     function $(id) {
          return document.getElementById(id);
     }

})();
