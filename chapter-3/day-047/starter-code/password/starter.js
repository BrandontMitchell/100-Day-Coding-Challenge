"use strict";

(function() {

     window.onload = function() {
          $("login-btn").onclick = login;
          let input = $("password");
     };

     function login() {
          let data = new FormData();
          let username = $("username").value;
          let password = $("password").value;
          data.append("username", username);
          data.append("password", password);
          let url = "solution.php"
          fetch(url, {method: "POST", body: data, mode:'cors', credentials:'include'})
               .then(checkStatus)
               .then(JSON.parse)
               .then(handleResponse)
               .catch(console.log);
     }

     function handleResponse(response) {
          if (response.usernameerror == "true") {
               $("email-error").innerText = "*Incorrect username.";
          } else if (response.usernameerror == "empty") {
               $("email-error").innerText = "*Required field";
          }  else {
               $("email-error").innerText = "";
          }

          if (response.passworderror == "true") {
               $("password-error").innerText = "*Incorrect Password.";
          } else if (response.passworderror == "empty") {
               $("password-error").innerText = "*Required field";
          } else {
               $("password-error").innerText = "";
          }

          if (response.usernameerror == "" && response.passworderror == "") {
               alert("success");
          }
     }

     function checkStatus(response) {
        if (response.status >= 200 && response.status < 300) {
             return response.text();
        } else {
             return Promise.reject(new Error(response.status + ": " + response.statusText));
        }
     }

     function $(id) {
          return document.getElementById(id);
     }

})();
