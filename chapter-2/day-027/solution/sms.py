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

jokes = ["Did you know theres no official training for a garbage collector?", 'I burnt my Hawaiian pizza today.', 'A doctor gave a man 6 months to live', 'How do you tuna fish?', 'What does a 6 foot 5 inch butcher weigh?']
answers = ['They just pick it up as they go', 'I shouldve cooked it on aloha temperature...', 'the man couldnt pay his bill so the doctor gave him another 6 months', 'You raise or lower the scales', 'Meat']

@app.route("/")
def test():
    return Response("it works!"), 200

@app.route("/dad", methods=['GET', 'POST'])
def dad_joke():
    resp = MessagingResponse()
    i = random.randint(0, 4)
    msg = jokes[i] + "--> " + answers[i]
    resp.message(msg)
    return str(resp)

@app.route("/meme", methods=['GET', 'POST'])
def meme():
    resp = MessagingResponse()
    img_list = ['./memes/0.jpeg', './memes/1.jpeg', './memes/2.jpeg', './memes/3.jpeg', './memes/4.jpeg', './memes/5.jpeg']
    i = random.randint(0, 4)
    img = img_list[i]
    resp.message(img)
    return str(resp)


if __name__ == '__main__':
    app.run(debug=True)