#!/usr/bin/python3
"""This is 0-hello_route module containing script that
starts a Flask web application.
"""
from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/')
def hello_hbnb():
    """Prints the hello message for the base url"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def just_hbnb():
    """Prints only HBNB for the route hbnb"""
    return 'HBNB'


@app.route('/c/<text>')
def c_is_fun(text):
    """Returns C followed by the text for the route /c/<text>"""
    return 'C %s' % text.replace('_', ' ')


@app.route('/python/')
@app.route('/python/<text>')
def python_is_cool(text='is cool'):
    """Returns Python followed by the text for the route /python/(<text>"""
    return 'Python %s' % text.replace('_', ' ')


@app.route('/number/<int:n>')
def display_number(n):
    """Returns the number if it's an int for the route /number/<n>"""
    return '%d is a number' % n


@app.route('/number_template/<int:n>')
def display_number_template(n):
    """Returns the number with a template if it's an int for the
    route /number_template/<n>
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def display_odd_or_even(n):
    """Returns an html saying even or odd if n is an int for the
    route /number_odd_or_even/<n>
    """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
