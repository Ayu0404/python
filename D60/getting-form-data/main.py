from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/welcome", methods=['POST'])
def getData():
    fullName = request.form.get("fullName")
    email = request.form.get("email")
    phNum = request.form.get("phoneNum")
    message = request.form.get("message")
    print(fullName, email, phNum, message)

    return render_template('welcome.html', name=fullName, email=email, phNum=phNum, message=message)
