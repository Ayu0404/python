from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from User import User, db
from CreateUserForm import CreateUserForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db.init_app(app)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        new_user = User(name=request.form.get('name'), email=request.form.get(
            'email'), password=request.form.get('password'))
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("secrets", id=new_user.id))
    return render_template("register.html")


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/secrets/<int:id>', methods=['GET'])
def secrets(id):
    loggedIn_user = db.session.query(User).filter_by(id=id).first()
    name = loggedIn_user.name.strip().split(' ')[0]
    return render_template("secrets.html", name=name)


@app.route('/logout')
def logout():
    pass


@app.route('/download')
def download():
    return send_from_directory(directory='static', path='files/cheat_sheet.pdf')


if __name__ == "__main__":
    app.run(debug=True)
