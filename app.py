# Modules

from flask import Flask, render_template

# Config

app = Flask(__name__)
app.secret_key='hiddenpass'

# Routes

@app.route('/')
def index():
    return render_template("index.html")

# Running

if __name__ == '__main__':
    app.secret_key='hiddenpass'
    app.run(debug=True)