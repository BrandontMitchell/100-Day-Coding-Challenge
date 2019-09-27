"use strict";

(function() {

     const API = "https://opentdb.com/api.php?amount=1";
     let correctAnswer;

     window.onload = function() {
          getQuestion();
          $("submit").onclick = checkAnswer;
          $("reveal").onclick = showAnswer;
     };

     function getQuestion() {
          
	     // your code goes here...
	     
     }

     function handleResponse(response) {
          response = response.results[0];

          // your code goes here...
	     
     }

     function checkAnswer() {

           // your code goes here...
           
     }

     function showAnswer() {

          // your code goes here...

     }

     /**
	 * Returns the DOM element with the id attribute of the given value
	 * @param {string} id - element ID
	 * @return {object} DOM object associated with the given id
	 */
	function $(id) {
		return document.getElementById(id);
	}

     /**
      * Function to check the status of an Ajax call, boiler plate code to include,
      * based on: https://developers.google.com/web/updates/2015/03/introduction-to-fetch
      * @param {string} response - the response text from the url call
      * @return did we succeed or not, so we know whether or not to continue with the handling of
      * this promise
      */
	function checkStatus(response) {
		if (response.status >= 200 && response.status < 300) {
			return response.text();
		} else {
			return Promise.reject(new Error(response.status + ": " + response.statusText));
		}
	}
})();
