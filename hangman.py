# define simple flask app
from flask import Flask,render_template,request
from functools import wraps

app = Flask(__name__)

@app.route('/')
def hello_hangman():
    return render_template('index.html')



if __name__ == "__main__":
    app.run()
