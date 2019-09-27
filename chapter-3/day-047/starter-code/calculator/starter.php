<?php
    ini_set('display_errors', 'On');
    error_reporting(E_ALL);

    if (isset($_GET["first"]) && isset($_GET["second"]) && isset($_GET["operation"])) {

         // your code goes here... 

    } else {
         echo "Something went wrong. Correct format: password.php?first=5&second=3&operation=(add|subtract|multiply|divide)";
    }
?>
