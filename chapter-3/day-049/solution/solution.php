<?php

# This API requires a GET parameter 'mode' that is one of two values:
# ====================
#   - mode=categories
#     |  returns a JSON object mapping trivia categories on the system with the
#     |  number of questions in each category
# ====================
#   - mode=category&name=categoryname
#     | returns a question/answer JSON object with a question/answer
#     | for a random trivia tidbit matching the specified categoryname.
#     | If categoryname does not correspond to one of the available categories on
#     | the server, returns a 400 response.

if (isset($_GET["mode"])) {
    $mode = strtolower($_GET["mode"]);
    $result;

    if ($mode == "categories") {
        $result = getCategories();
    } else if ($mode == "category") {
        $result = getCategory();
    }

    if ($result) {
        header("Content-type: application/json");
        print ($result);
    } else {
        header("HTTP/1.1 400 Error");
        die("Invalid mode passed. Please pass mode as 'categories' or 'category'.");
    }

} else {
    header("HTTP/1.1 400 Error");
    die("Missing mode query parameter.");
}

# Returns a JSON object containing all categories in the trivia folder path
# mapping each category name to the number of files of trivia data for that category.
function getCategories() {
    $triviafiles = "../starter/trivia/";
    $categories = array_diff(scandir($triviafiles) , array('..', '.'));
    $result["categories"] = [];
    foreach ($categories as $category) {
        $filecount = count(glob($triviafiles . $category . "/*.txt"));
        $result["categories"][$category] = $filecount;
    }
    return json_encode($result);
}

# Returns a JSON object for a trivia category containing a random question/answer.
# If name is passed as a query parameter with a value, returns a question/answer
# for a random trivia file with the category name. If the name does not correspond to
# the category name passed, outputs an 400 error. If no name query parameter is passed,
# returns a random question/answer from any of the trivia categories on the server.
function getCategory() {
    $triviafiles = "../starter/trivia/";
    
    if (!isset($_GET["name"])) {
        $categories = scandir($triviafiles);
        $categoryName = $categories[array_rand($categories) ];
    } else {
        $categoryName = strtolower($_GET["name"]);
    }

    $trivia = glob($triviafiles . $categoryName . "/*.txt");
    if (count($trivia) == 0) {
        header("HTTP/1.1 400 Error");
        die("No trivia found for the requested category.");
    }

    $index = array_rand($trivia);
    $randomTrivia = $trivia[$index];
    $qfile = file_get_contents($randomTrivia);

    $lines = explode("\n", $qfile);
    $question = $lines[0];
    $answer = $lines[1];
    return json_encode(array(
        "question" => $question,
        "answer" => $answer
    ));
}
?>
