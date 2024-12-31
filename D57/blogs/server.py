from flask import Flask, render_template
from Blogs import Blogs

app = Flask(__name__)

allblogs = Blogs()
data = allblogs.get_data()


@app.route("/")
def all_blogs():
    return render_template('index.html', data=data)


@app.route("/blog/<int:id>")
def blog(id):
    blog = {}
    for b in data['blogs']:
        if b['id'] == id:
            blog = b
    return render_template('blog.html', blog=blog)
