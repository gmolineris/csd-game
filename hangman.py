# define simple flask app
from flask import Flask,render_template,request
from functools import wraps
from model.hangman_lib import Digit

app = Flask(__name__)
digit = Digit()

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/forward', methods=['POST'])
def forward():
    value = request.form['text']
    result = digit.validate(value)
    
    return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run()
