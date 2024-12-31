from flask import Flask, render_template
import datetime as dt
import requests

app = Flask(__name__)

gender_endpoint = "https://api.genderize.io/?name="
age_endpoint = "https://api.agify.io/?name="


@app.route("/")
def home():
    now = dt.datetime.today()
    return render_template("index.html", year=now.year)


def get_gender(name):
    data = requests.get(gender_endpoint+name).json()
    return data['gender']


def get_age(name):
    data = requests.get(age_endpoint+name).json()
    return data['age']


@app.route("/guess/<string:name>")
def guess_user_demographics(name):
    age = get_age(name)
    gender = get_gender(name)

    return render_template('demographics.html', name=name, age=age, gender=gender)
