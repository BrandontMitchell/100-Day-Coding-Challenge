# Steps:
#test
# 1. Create an account at Twilio --> https://www.twilio.com/try-twilio
# 2. Verify email and phone number
# 3. Generate trial phone number --> +12068006648
# 4. pip install twilio
# https://www.twilio.com/docs/sms/quickstart/python
# https://ngrok.com/download
# https://www.twilio.com/console/phone-numbers/incoming
from flask import Flask, Response, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio import twiml
import requests
import random
import time

# Your Account Sid and Auth Token from twilio.com/console
account_sid = ''
auth_token = ''
app = Flask(__name__)

jokes = []
answers = []

@app.route("/")
def test():
    return Response("it works!"), 200

@app.route("/dad", methods=['GET', 'POST'])
def dad_joke():
    pass

@app.route("/meme", methods=['GET', 'POST'])
def meme():
    pass

# free function here!

if __name__ == '__main__':
    app.run(debug=True)