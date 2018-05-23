from resources import Resources
import io
from flask import render_template
from flask import Flask

resources = Resources()
resources.init()
app = Flask(__name__)
with app.app_context():
    with io.open('index.html', 'w') as output:
        output.write(render_template("archives.html", posts=resources.posts(), title="archives"))

    with io.open('archives.html', 'w') as output:
        output.write(render_template("archives.html", posts=resources.posts(), title="archives"))

    with io.open('about.html', 'w') as output:
    	post = resources.get_about()
        output.write(render_template("post.html", post=post, title="about"))

    with io.open('notes.html', 'w') as output:
        post = resources.get_note()
        output.write(render_template("post.html", post=post, title="notes"))

    with io.open('categories.html', 'w') as output:
        output.write(render_template("categories.html", categories=resources.categories(), title="categories"))

    for post in resources.posts():
        with io.open('archives/' + post.link, 'w') as output:
            output.write(render_template("post.html", post=post, title=post.title))
