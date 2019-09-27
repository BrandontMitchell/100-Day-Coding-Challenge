<?php
    ini_set('display_errors', 'On');
    error_reporting(E_ALL);

    if (isset($_POST["username"]) && isset($_POST["password"])) {

         // your code goes here...

    } else {
         echo "Please enter both username and password.";
    }
?>
