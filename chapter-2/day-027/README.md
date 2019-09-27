# Day 027 - Using Twilio for SMS 

The purpose of this day is to have fun communicating via SMS (and with the help of `twilio`!). We will utilize twilios server to handle post and get requests, to create a dad joke generator!
### Using flask server
* Create a default route:
    * `@app.route("/")` is our wrapper for instantiating a api endpoint. The "/" is our default, meaning they just need to connect to our server to access this function.
    * `@app.route("/get", methods=["GET"])` will instantiate a get request, meaning we will need to feed or `return` it back some data. Flask only allows for certain objects to be returned, so be careful!
    * To create a message response:
    We will assign `resp = MessagingResponse()`, and now we need to access its content with `.message(data)` so we can return that response with the appropriate type for twilio to handle



### Your Task:

1. Create an account at Twilio --> https://www.twilio.com/try-twilio

2. Verify email and phone #

3. Generate trial phone number (remember so u can text this!)

4. (if you get lost): 
    * https://www.twilio.com/docs/sms/quickstart/python
    * https://ngrok.com/download
    * https://www.twilio.com/console/phone-numbers/incoming

2. Install all dependencies:
    ```
    pip install twilio
    pip install flask

    https://pip.pypa.io/en/stable/installing/
    ^ if you do not have pip installed on machine
    ```

3. create 3 functions:
* One that sends a dad joke when the user enters "dad"
* Two others!


Good luck and happy coding!