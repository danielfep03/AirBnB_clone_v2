#!/usr/bin/python3
''' Module that starts a Flask web application '''

from flask import Flask, abort, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def main():
    ''' Main page Content '''
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    ''' Content Route hbnb '''
    return 'HBNB'


@app.route('/c/<route>')
def custom_route(route):
    route = 'C ' + route
    return route.replace('_', ' ')


@app.route('/python/')
@app.route('/python/<text>')
def python_route(text='is cool'):
    text = 'Python ' + text
    return text.replace('_', ' ')


@app.route('/number/<num>')
def number_route(num):
    if num.isnumeric():
        return num + ' is a number'
    return abort(404)


@app.route('/number_template/<n>')
def number_template(n):
    if n.isnumeric():
        return render_template('5-number.html', my_num=n)
    return abort(404)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
