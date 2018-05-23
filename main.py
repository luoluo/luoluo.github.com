import flask
from flask import Flask
from flask import request
from flask import render_template
from flask import url_for
from flask import redirect
from resources import Resources

app = Flask(__name__)
resources = Resources()
resources.init()

@app.route("/about")
def about():
    # return render_template("about.html")
    post = resources.get_about()
    return render_template("post.html", post=post, title="about")

@app.route("/archives/")
def archives():
    return render_template("archives.html", posts=resources.posts(), title="archives")

@app.route("/archives/<string:archive_id>")
def archive(archive_id):
    post = resources.get(archive_id)
    return render_template("post.html", post=post, title=post.title)

@app.route("/construct")
def construct():
    return render_template("construct.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("construct.html")

@app.route("/dev")
def dev():
    return redirect(url_for("archives"))

@app.route("/categories")
def categories():
    return render_template("categories.html", categories=resources.categories(), title="categories")

@app.route("/notes")
def notes():
    post = resources.get_note()
    return render_template("post.html", post=post, title="notes")

@app.route("/")
def hello():
    #return redirect(url_for("construct"))
    return redirect(url_for("dev"))

if __name__ == "__main__":
    app.run()
