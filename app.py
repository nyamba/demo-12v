from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/user/<name>/<age>')
def index(name, age):
    return render_template('index.html', user=name, age=age)


@app.route('/add/<int:number1>/<int:number2>')
def add(number1, number2):
    total = number1 + number2
    return render_template('total.html', total=total)


@app.route('/snake')
def snake():
    return render_template('snake.html')
