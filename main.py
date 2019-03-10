# !flask/bin/Python

from flask import Flask, render_template

app = Flask(__name__)

# ------- Main Page -------
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=8080)
