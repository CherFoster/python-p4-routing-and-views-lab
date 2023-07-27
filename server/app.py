#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:data>')
def print_string(data):
    print(data)
    return data

@app.route('/count/<int:num>')
def count(num):
    numbers = ''
    for i in range(num):
        numbers += f'{i}\n'
    return numbers

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2

    if result is not None:
        return str(result)
    else:
        return "Invalid operation or parameters."


if __name__ == '__main__':
    app.run(port=5555, debug=True)
