/*
 * Implements the UI of a nonogram puzzle game, allowing a user
 * to play the game by filling, crossing, or clearing tiles of a
 * classic Nonogram number puzzle.
 */
(function () {
	"use strict";

	/*
	 * Sets up the various event listeners on the page, including
	 * click and dragging behavior for each puzzle grid square and
	 * the functionality for clearing a puzzle state.
	 */
	window.onload = function () {
	};

	/**
	 * Returns the element that has the ID attribute with the specified value.
	 * @param {string} id - element ID
	 * @return {object} DOM object associated with id.
	 */
	function $(id) {
		return document.getElementById(id);
	}

	/**
	 * Returns the array of elements that match the given CSS selector.
	 * @param {string} query - CSS query selector
	 * @return {object[]} array of DOM objects matching the query.
	 */
	function $$(query) {
		return document.querySelectorAll(query);
	}
})();
