<?php
    ini_set('display_errors', 'On');
    error_reporting(E_ALL);

    if (isset($_POST["username"]) && isset($_POST["password"])) {
         $username_error = "";
         $password_error = "";
         $username = trim($_POST["username"]);
         $password = trim($_POST["password"]);

         if ($username == "") {
             $username_error = "empty";
         } else if ($username != "username") {
             $username_error = "true";
         }

         if ($password == "") {
            $password_error = "empty";
         } else if ($password != "password") {
            $password_error = "true";
         }

         $response = new \stdClass();
         $response->usernameerror = $username_error;
         $response->passworderror = $password_error;

         header('Content-type: application/json');
         print json_encode($response);

    } else {
         echo "Please enter both username and password.";
    }
?>
