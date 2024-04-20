#!/usr/bin/python3
"""
    a script that starts a Flask web application
"""


from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    lst = text.split('_')
    strg = " ". join(lst)
    return "C {}".format(strg)


@app.route("/python", defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    lst = text.split("_")
    strg = " ".join(lst)
    return "Python {}".format(strg)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
