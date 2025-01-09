from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email

app = Flask(__name__)
app.secret_key = "123"


class MyForm(FlaskForm):
    email = StringField(label='Email', validators=[
                        DataRequired(), Email(granular_message=True, allow_empty_local=True)])
    password = PasswordField(label='Password', validators=[
                             DataRequired(), Length(min=8)])
    submit = SubmitField(label='Log In')


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    loginForm = MyForm()
    if loginForm.validate_on_submit():
        print(loginForm.email.data, loginForm.password.data)
        if loginForm.email.data.strip() == 'admin@email.com' and loginForm.password.data == '12345678':
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=loginForm)


if __name__ == '__main__':
    app.run(debug=True)
