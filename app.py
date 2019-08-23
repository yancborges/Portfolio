# Modules

from flask import Flask, render_template

# Config

app = Flask(__name__)
app.secret_key='hiddenpass'

# Routes

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/works')
def works():
	return render_template("works.html")

@app.route('/academics')
def academics():
	return render_template("academics.html")

@app.route('/notcode')
def notcode():
	return render_template("notcode.html")

@app.route('/skills')
def skills():
	return render_template("skills.html")

# Running

if __name__ == '__main__':
    app.secret_key='hiddenpass'
    app.run(debug=True)