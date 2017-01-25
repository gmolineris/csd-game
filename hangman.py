# define simple flask app
from flask import Flask,render_template,request
from functools import wraps
from model.hangman_lib import HangMan

app = Flask(__name__)
hangman = HangMan()

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/forward', methods=['POST'])
def forward():
    value = request.form['text']
    result = hangman.validate(value)
    
    return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run()
