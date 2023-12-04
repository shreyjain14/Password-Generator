from generator import generate_password
from strengthChecker import checkStrength
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', name=None)


@app.route('/', methods=['POST'])
def read_form():
    data = request.form.get
    score = 0
    pw, password, strength = generate_password(
        int(data('length')),
        data('uppercase'),
        data('lowercase'),
        data('symbols'),
        data('numbers'))

    return render_template('index.html', pw=pw, password=password, scoreStrength=strength)


if __name__ == '__main__':
    app.run()
