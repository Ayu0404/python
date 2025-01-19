from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books-collection.db"
db.init_app(app)

# Creating table
class Book(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True, nullable=False)
    author: Mapped[str]= mapped_column(unique=False,nullable=False)
    rating: Mapped[str]= mapped_column(unique=False,nullable=False)

# with app.app_context():
#     db.create_all()

# Read
@app.route('/')
def home():
    all_books=db.session.query(Book).all()
    return render_template('index.html',books=all_books)

# Create
@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method=='POST':
        newBook=Book(title=request.form.get("title"), author=request.form.get("author"),rating=request.form.get("rating"))
        db.session.add(newBook)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')

# Update
@app.route("/edit/<int:book_id>",methods=['GET', 'POST'])
def edit(book_id):
    the_book=Book.query.filter_by(id=book_id).first()
    print(the_book)
    if request.method=='POST':
        the_book.rating=request.form.get('rating')
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html',book=the_book)


# Delete
@app.route("/delete")
def delete():
    book_id = request.args.get('book_id')
    book_to_delete = Book.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
