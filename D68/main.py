from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, LoginManager, login_required, current_user, logout_user
from User import User, db
from CreateUserForm import CreateUserForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).get(int(user_id))


@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        user = db.session.query(User).filter_by(email=email).first()
        if user:
            flash('Email already exists. Please login. ', 'error')
            return redirect(url_for('register'))

        new_user = User(name=name, email=email, password=generate_password_hash(
            password=password, method='pbkdf2:sha256', salt_length=8))
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("secrets", id=new_user.id))
    return render_template("register.html", is_logged=current_user.is_authenticated)


# Login with
# name - Ayushi
# email - a@gm.com
# pswd - 123456


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = db.session.query(User).filter_by(email=email).first()

        if not user:
            flash('User not found.', 'error')
            return redirect(url_for('login'))
        elif not check_password_hash(user.password, password):
            flash('Incorrect password', 'error')
            return redirect(url_for('login'))
        else:
            login_user(user)
            return redirect(url_for('secrets', id=user.id))
    return render_template("login.html", is_logged=current_user.is_authenticated)


@ app.route('/secrets/<int:id>', methods=['GET'])
@ login_required
def secrets(id):
    loggedIn_user = db.session.query(User).filter_by(id=id).first()
    name = loggedIn_user.name.strip().split(' ')[0]
    return render_template("secrets.html", name=name)


@ app.route('/logout')
@ login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@ app.route('/download')
@ login_required
def download():
    return send_from_directory(directory='static', path='files/cheat_sheet.pdf')


if __name__ == "__main__":
    app.run(debug=True)
