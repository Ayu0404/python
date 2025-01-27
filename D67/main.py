from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from CreatePostForm import CreatePostForm
from BlogPost import BlogPost, db
import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db.init_app(app)


def all_posts():
    return db.session.query(BlogPost).all()


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=all_posts())


@app.route("/post/<int:index>")
def show_post(index):
    posts = all_posts()
    requested_post = None
    for blog_post in posts:
        if blog_post.id == index:
            requested_post = blog_post
    print(requested_post)
    return render_template("post.html", post=requested_post)


def create_new_post(form):
    month = datetime.datetime.now().strftime("%B")
    day = datetime.datetime.now().day
    year = datetime.datetime.now().year

    new_post = BlogPost(title=form.title.data, subtitle=form.subtitle.data, date=f'{month} {day}, {year}',
                        author=form.author.data, img_url=form.img_url.data, body=form.body.data)
    return new_post


@app.route("/new-post", methods=["POST"])
def new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        db.session.add(create_new_post(form))
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template('make-post.html', form=form)


@app.route("/edit_post/<int:post_id>", methods=['Get', 'POST'])
def edit_post(post_id):
    current_post = db.session.query(BlogPost).filter_by(id=post_id).first()
    edit_form = CreatePostForm(title=current_post.title,
                               subtitle=current_post.subtitle, date=current_post.date, author=current_post.author, img_url=current_post.img_url, body=current_post.body)
    if edit_form.validate_on_submit():
        current_post.title = edit_form.title.data
        current_post.subtitle = edit_form.subtitle.data
        current_post.author = edit_form.author.data
        current_post.img_url = edit_form.img_url.data
        current_post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template('edit-post.html', post=current_post, form=edit_form)


@app.route('/delete/<int:index>')
def delete(index):
    delete_post = BlogPost.query.filter_by(id=index).first()

    db.session.delete(delete_post)
    db.session.commit()
    return render_template('index.html', all_posts=all_posts())


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
