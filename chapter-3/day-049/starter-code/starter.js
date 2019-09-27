"use strict";

/*
 * Implements the fetching and interactivity for the trivia webpage, allowing a user to
 * see random trivia questions and test their knowledge against the answers.
 */

(function () {
	let currentCategory;

	/*
	 * Sets up the page, fetching the list of categories for the trivia webpage, as well
	 * as setting up functionality for switching between answers/questions when clicking the "Next"
	 * button.
	 */
	window.onload = function () {
		$("view-all").onclick = fetchCategories;
		$("next").onclick = toggleQA;
	};

	/*
	 * Fetches a new question/answer trivia tidbit for the current category, displaying the
	 * question as a result. If no category is currently selected, makes a request
	 * that is category-independent. Logs an error if the request is unsuccessful.
	 */
	function showTrivia() {
		let url = "solution.php?mode=category";
		if (currentCategory) {
			url += "&name=" + currentCategory;
		}
		fetch(url)
			.then(checkStatus)
			.then(JSON.parse)
			.then(displayQuestion)
			.catch(console.log);
	}

	/*
	 * Displays the categories on the page based on the responseData.
	 * @param {object} responseData - parsed JSON representing categories for the trivia
	 * available.
	 */
	function displayCategories(responseData) {
		let categories = responseData["categories"];
		let ul = $("categories");
		ul.innerHTML = "";
		$("categories-heading").classList.remove("hidden");
		for (let category in categories) {
			let li = document.createElement("li");
			li.innerText = category;
			ul.appendChild(li);
			li.onclick = selectCategory;
		}
		$("category-view").classList.remove("hidden");
		$("categories").classList.remove("hidden");
	}

	/*
	 * Displays the question in the question area based on the question from the response.
	 * Hides any visible answer text.
	 * @param {object} response - JSON object containing question and answer information for
	 * a trivia tidbit.
	 */
	function displayQuestion(response) {
		$("current-question").innerText = response.question;
		$("current-answer").innerText = response.answer;
		$("current-answer").classList.add("hidden");
		$("question-area").classList.remove("hidden");
	}

	/*
	 * Fetches the list of categories for the trivia page, displaying them based on the result.
	 * Logs an error if the request was unsuccesful.
	 */
	function fetchCategories() {
		fetch("trivia.php?mode=categories")
			.then(checkStatus)
			.then(JSON.parse)
			.then(displayCategories)
			.catch(console.log);
	}

	/*
	 * Updates the current category based on the text of the element this function
	 * was attached to, hiding the "Next" button and resetting the current question/answer
	 * display.
	 */
	function selectCategory() {
		currentCategory = this.innerText;
		let selected = qsa(".selected-category");
		for (let i = 0; i < selected.length; i++) {
			selected[i].classList.remove("selected-category");
		}
		this.classList.add("selected-category");
		$("next").classList.remove("hidden");
		$("current-question").innerText = "";
		$("current-answer").innerText = "";
	}

	/*
	 * Toggles the question/answer currently shown. If the answer to the current question is
	 * not displayed, displays it. Otherwise, fetches a new question/answer for the
	 * current category. Only the question for the new trivia tidbit is then displayed.
	 */
	function toggleQA() {
		let currentAns = $("current-answer");
		if (currentAns.classList.contains("hidden")) {
			currentAns.classList.remove("hidden");
			$("next").innerText = "Next Question";
		} else {
			showTrivia();
			$("next").innerText = "Show Answer";
		}
	}

	/* ==============================  Helper Functions ============================== */
	/*
	 * Helper function to return the response's result text if successful, otherwise
	 * returns the rejected Promise result with an error status and corresponding text
	 * @param {object} response - response to check for success/error
	 * @return {object} - valid result text if response was successful, otherwise rejected
	 *                    Promise result
	 */
	function checkStatus(response) {
		if (response.status >= 200 && response.status < 300 || response.status == 0) {
			return response.text();
		} else {
			return Promise.reject(new Error(response.status + ": " + response.statusText));
		}
	}

	/**
	 * Returns the element that has the ID attribute with the specified value.
	 * @param {string} id - element ID.
	 * @return {object} DOM object associated with id.
	 */
	function $(id) {
		return document.getElementById(id);
	}

	/**
	 * Returns an array of elements matching the given query (an alias for querySelectorAll).
	 * @param {string} el - query matching returned DOM elements.
	 * @return {object[]} array of DOM objects matching the given query.
	 */
	function qsa(query) {
		return document.querySelectorAll(query);
	}

})();
