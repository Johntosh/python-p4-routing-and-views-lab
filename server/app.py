#!/usr/bin/env python3

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:param>')
def print_string(param):
    print(param)  # Print the string in the console
    return f'<h1>{param}</h1>'  # Display the string in the browser

@app.route('/count/<int:param>')
def count(param):
    output = '<br>'.join(str(i) for i in range(param))  # Display numbers on separate lines
    return f'<h1>Counting to {param}</h1><pre>{output}</pre>'

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2 if num2 != 0 else 'Cannot divide by zero'
    elif operation == '%':
        result = num1 % num2
    else:
        return 'Invalid operation'
    
    return f'<h1>Result: {result}</h1>'

if __name__ == '__main__':
    app.run(debug=True)

