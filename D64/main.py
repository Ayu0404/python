from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from MovieForm import MovieForm, EditMovieRating
from Movie import Movie, db
import requests

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies-collection.db"
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)
db.init_app(app)


def create_db():
    with app.app_context():
        db.create_all()


@app.route("/")
def home():
    movies = db.session.query(Movie).all()
    return render_template("index.html", movies=movies)


@app.route("/add", methods=['GET', 'POST'])
def add():
    form = MovieForm()
    if form.validate_on_submit():
        new_row = Movie(title=form.title.data, year=form.year.data, description=form.description.data,
                        rating=form.rating.data, ranking=form.ranking.data, review=form.review.data, image_url=form.image_url.data)
        db.session.add(new_row)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html", form=form)


@app.route("/edit<int:movie_id>", methods=['GET', 'POST'])
def edit(movie_id):
    movie = Movie.query.filter_by(id=movie_id).first()
    edit_form = EditMovieRating()
    if request.method == 'POST':
        movie.rating = edit_form.rating.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", movie=movie, form=edit_form)


@app.route("/delete")
def delete():
    id = request.args.get('movie_id')
    movie = Movie.query.filter_by(id=id).first()
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
