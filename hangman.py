# define simple flask app
from flask import Flask,render_template,request
from functools import wraps
from model.hangman_lib import HangMan

app = Flask(__name__)

hangman = HangMan()

@app.route('/')
def hello_hangman():
    return render_template('index.html')

@app.route('/validate', methods=['POST'])
def validateWord():
    value = request.form['word']
    #result = hangman.validate(value)
    (body,partial) = hangman.validate(value)
    return render_template('index.html', body=body, partial=partial)

if __name__ == "__main__":
    app.run()
