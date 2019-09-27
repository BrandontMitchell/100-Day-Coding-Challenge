# Day 034 - Web apis with flask!

The purpose of this day is to introduce yet another beautifully written python module, flask. Flask is an all purpose, yet small and maintained web service module. You can build an entire, massive website with almost flask alone!

### Setup
1. We already saw a little bit of flask in our sms tweet project. Here we will understand what means what
2. Look over the template/welcome.html file. This will be taught later in the challenge!
3. Notice `<form action="/location" method="GET">
        <input name="location" value="seattle"/>`, these are where we enter our method type, endpoint, and the name to return with its value
4. Remember we initialize an api endpoint or `route` with:
    * `@app.route(..., methods=[...])`
    * To handle our requests, we get `request.args.get('variablename_in_html_file')` and return that variable
5. Visit `localhost` in the search bar and you will see that value u returned in ur default route and the html output!
6. Modify the code so that you handle different requests (i.e. --> `localhost/heres-your-endpoint`)


### Your Task:

1. After you finish reading through this guide, visit the documentation to get an understanding how to use things

2. Install all dependencies:
    ```
    pip install flask
    https://pip.pypa.io/en/stable/installing/
    ^ if you do not have pip installed on machine
    ```

3. Follow the code comments


Good luck and happy coding!