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
          let url = API;
          fetch(url, {mode:'cors'})
               .then(checkStatus)
               .then(JSON.parse)
               .then(getQuestionHelper)
               .catch(console.log);
     }

     function getQuestionHelper(response) {
          response = response.results[0];
          $("category").innerHTML = $("category").innerHTML + " " + response.category;
          if (response.type == "multiple") {
               $("type").innerHTML = $("type").innerHTML + " Multiple Choice";
          } else if (response.type == "boolean") {
               $("type").innerHTML = $("type").innerHTML + " True/False";
          }
          let difficulty = response.difficulty;
          difficulty = difficulty.charAt(0).toUpperCase() + difficulty.slice(1);
          $("difficulty").innerHTML = $("difficulty").innerHTML + " " + difficulty;
          $("question").innerHTML = $("question").innerHTML + " " + response.question;
          correctAnswer = response.correct_answer;
     }

     function checkAnswer() {
           if ($("answer").value.toLowerCase().trim() == correctAnswer.toLowerCase()) {
                alert("You got it right!");
           } else { // incorrect answer
                alert("Oops! Try again.");
           }
     }

     function showAnswer() {
          $("correct-answer").innerHTML = $("correct-answer").innerHTML + " " + correctAnswer;
          $("correct-answer").classList.remove("hidden");
          $("submit").disabled = true;
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
