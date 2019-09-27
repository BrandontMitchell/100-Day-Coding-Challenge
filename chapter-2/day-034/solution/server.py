#import flask yada yada

from flask import Flask, render_template, request
import random, math


app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/location', methods=["GET"])
def location_get():
    loc = request.args.get('location')
    print(loc)
    return "Your location is: " + str(loc) + " (this is handled through a get request!!)"

@app.route('/picknumber')
def number_post():
    return str(random.randint(0,2000))

@app.route('/pi')
def return_pi():
    return str(math.pi)

if __name__ == '__main__':
    app.run(debug=True)