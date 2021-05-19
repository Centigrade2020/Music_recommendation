from logging import debug
from flask import Flask, render_template, request
from ml import suggestions

app = Flask(__name__)


@app.route('/')
def home():

    return render_template('index.html')


@app.route('/suggesstions', methods=["POST"])
def suggest():
    name = request.form.get('name')
    age = request.form.get('age')
    gender = request.form.get('gender')
    sug = suggestions(age, gender)
    return render_template('suggest.html', suggest=sug,name=name)


if __name__ == "__main__":
    app.run(debug=True)
