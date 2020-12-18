from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


# view function
@app.route('/user/<name>/<int:age>')
def index(name, age):
    return render_template('index.html', name=name, age=age)


@app.route('/add/<int:number1>/<int:number2>')
def add(number1, number2):
    total = number1 + number2
    return render_template('total.html', total=total)


@app.route('/n/<news_id>')
def detail_page(news_id):
    return 'News id: '+ news_id


@app.route('/game/snake1')
def snake():
    return render_template('snake.html')
