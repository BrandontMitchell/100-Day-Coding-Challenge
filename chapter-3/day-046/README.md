# Day 046 - AJAX and JSON

Today's challenge, although not immensely intensive, is incredibly foundational for almost any meaningful project you can make in relation to web programming. We will be discussing how to use JavaScript to communicate with a public **application programming interface** (API). An API can mean a lot of things, and in the broadest sense, it's just an interface that simplifies communication between a **client** and **server**, making writing client-side code a lot easier. For us, it will act as a middle-man between our JavaScript code and a database of information. By following the rules of the API in how we talk to it, we will be able to get nicely-packaged data in return.

This means we will be creating out very first **web application**. Web applications are webpages that pull in additional data and information as the user progresses through them, making it feel similar to a desktop application.

You will be creating a random trivia generator. At the click of a button, the page will populate with a trivia question generated courtesy of the [Open Trivia Database](https://opentdb.com). This free to use user-contributed trivia question database will provide well-formatted data that we can use to populate the content on our webpage.

## Starter Code

This day includes three files in the starter-code folder: `starter.html`, `starter.css`, and `starter.js`. The `starter.html` file includes a few important pieces of information:

1. There is an `<li>` tag with the `id` of `category` that you will populate with the category of the question.

2. There is an `<li>` tag with the `id` of `type` that you will populate with the type of question.

3. There is an `<li>` tag with the `id` of `difficulty` that you will populate with the difficulty of the question.

4. There is a `<button>` with the `id` of `submit` that is used to submit an answer.

5. There is a `<button>` with the `id` of `reveal` that is used to reveal the correct answer.

6. There is an `<input>` tag with the `id` of `answer` that is used to hold the user-inputted answer.

7. There is a hidden `<p>` tag with the `id` of `correct-answer` that secretly hides the correct answer.

Other than this, you may safely ignore this file, as well as the `starter.css` file.

The `starter.js` function includes a good foundational structure for you to get started. It includes three global variables:

1. `API`: this is the base URL of the API that we will be using. 

2. `CATEGORIES`: this is an array of possible category codes to choose from. You can view the [website](https://opentdb.com) if you would like to customize this array with categories that you like.

3. `correctAnswer`: this String holds the correct answer for later comparison with submitted answers.

Although not required, you can follow the suggested structure of functions. That way, you know that you won't have to define any more functions than the ones provided. The `starter.js` file defines two helper functions:

1. `$`: this serves as an alias for `document.getElementById`

2. `checkStatus`: This function checks the status of an AJAX call. It is not necessary to understand this function.
  
## Getting Started
  
The first new thing that you'll notice is the use of the `<input>` tag. This tag is extremely useful, especially in conjunction with JavaScript, because it allows us to take in user-inputted text. You've probably seen many examples of `<input>` tags on other sites; user-input can look really fancy on different sites, but it's almost always the `<input>` tag behind the scenes. We'll be able to check the `value` attribute of the DOM element associated with that `<input>` tag to access what the user has typed in.

### Example
```
<input id="user-input" type="text" />
```

```
let input = document.getElementById("user-input");
// do something with input.value
```

The reason that we give it the `type` attribute of `text` is because there are several different types of `<input>` tags in HTML. If you're curious, you can view all the other different types [here](https://www.w3schools.com/html/html_form_input_types.asp). 

The first step is to set up a way to communicate with the API. We will be using **Asynchronous JavaScript and XML** (AJAX) which is just a specific style of using JavaScript to call out to a server for more information. The reason it's called **asynchronous** is because it allows the web page to dynamically update the webpage without making the user wait. Imagine using Google, but first having to wait for every webpage to fully load before you could start scrolling through your results. It would be impossible, which is why we have the concept of asynchronous requests.

There is a `fetch` function that we will be using to fetch information from a server. It's a lot of new syntax, but keep in mind that it's boilerplate code, so you don't have to memorize it; you just copy it down every time you need to use it.

### AJAX fetch Code Skeleton
```

function checkStatus(response) {    // boiler plate code
   ...
}

function callAjax() {
    let url = ..... // put url string of the API here
    fetch(url, {mode:'cors'})
       .then(checkStatus)
       .then(JSON.parse) // optional line of code that you include if the API returns JSON
       .then(handleResponse)
       .catch(console.log);
}

function handleResponse(response){
    //success: do something with the response
}
```

When we covered this in my web programming class, I remember it looked like the hardest programming concept I had ever seen at that point. `fetch` is a pretty confusing function, especially since it uses so many new concepts. The biggest thing to grasp here is that `fetch` does the work of communicating with our server. Because this is an unsure task (the server could be down, or internet could cut out) we have to use the boilerplate code in the `checkStatus` function to ensure we avoid any bad errors.

The reason it's chained with a bunch of `.then` statements is because it would look even uglier and scarier otherwise. `.then` is a JavaScript concept that takes the output of one function and passes it along to the next. Here's roughly what happens:

1. `fetch` communicates with the server, returning information about the succesfulness of our request, along with hopefully all of our desired information. This gets passed along to `checkStatus`.

2. `checkStatus` ensures that everything went smoothly, and then passes along the information.

3. (Optional) This step is required if the API returns JSON formatted data.

4. `handleResponse` will contain all the code that we write. Notice how this function has a single parameter: `response`, which contains all of the information from the server. This parameter will either be plain text, or an object if the server returned JSON formatted data.

Let's explain this JSON thing that we've been throwing around left and right.

**JavaScript Object Notation** (JSON) is a data format that represents data as a set of JavaScript objects. JavaScript objects are similar to Java, but you don't need a class to create a new object.

### Syntax
```
let myobj = {
  fieldName1: value1,
  ...
  fieldName: value
};
```

You can add properties to any object even after it is created:

```
myobj.field87 = "some value";
```

### Example
```
let person = {
    name: "Philip J. Fry",                           // string
    age: 23,                                         // number
    "weight": 172.5,                                 // number
    friends: ["Farnsworth", "Hermes", "Zoidberg"],   // array
    getBeloved: function() { return this.name + " loves Leela"; }
};
alert(person["age"]);                  // 23
alert(person.weight);                  // 172.5
alert(person.friends[2]));             // Zoidberg
alert(person.getBeloved());            // Philip J. Fry loves Leela
```

An object of can have functions (behavior) as well as state (fields). Hopefully this concept is ringing some bells from the end of the Java unit. DOM elements are an example of a JavaScript object that you have already worked with.

JSON is used just to store data, so you won't see functions being defined in JSON formatted data. Here's an example of what JSON looks like:

### JSON Example
```
{                          // no variable assignment
  "first_name": "Bart",    // strings and properties must be quoted
  "last_name": "Simpson",  // with double quotes
  "age" : 13,              // numbers can be here without quotes
  "cowabunga": true        // booleans can be here without quotes
}                          // no semicolon at the end
```

This is the nicely-formatted data that will be returned to us when we communicate with the Open Trivia Database. The `response` parameter in our `handleReponse` function will be able to be accessed just like a JavaScript object. Here's an example of what the formatted response from the trivia database looks like:

```
{
"response_code": 0,
"results": [
    {
      "category": "Science & Nature",
      "type": "multiple",
      "difficulty": "medium",
      "question": "A positron is an antiparticle of a what?",
      "correct_answer": "Electron",
      "incorrect_answers": [
        "Neutron",
        "Proton",
        "Photon"
      ]
    }
  ]
}
```

If you want to see it for yourself, you can actually navigate to [https://opentdb.com/api.php?amount=1](https://opentdb.com/api.php?amount=1). If you want it to appear nicely formatted like it is above then you'll have to install a [chrome extension](https://chrome.google.com/webstore/detail/json-formatter/bcjindcccaagfpapjjmafapmmgkkhgoa?hl=en).

As an example, if I wanted to access the question's difficulty, I would write `response.results[0].type` Note that Arrays are denoted by square brackets (`[]`) and objects are denoted with curly braces (`{}`). This should provide you with all the information you need to complete today's challenge. Good luck!



