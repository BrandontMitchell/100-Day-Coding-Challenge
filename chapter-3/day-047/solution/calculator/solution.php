<?php
    ini_set('display_errors', 'On');
    error_reporting(E_ALL);

    if (isset($_GET["first"]) && isset($_GET["second"]) && isset($_GET["operation"])) {
         $first = (int) $_GET["first"];
         $second = (int) $_GET["second"];
         $operation = $_GET["operation"];
         if ($operation == "add") {
              echo ($first + $second);
         } else if ($operation == "subtract") {
              echo ($first - $second);
         } else if ($operation == "multiply") {
              echo ($first * $second);
         } else { // $operation == "divide"
              echo ($first / $second);
         }
    } else {
         echo "Something went wrong. Correct format: solution.php?first=5&second=3&operation=(add|subtract|multiply|divide)";
    }
?>
