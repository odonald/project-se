import sqlite3
from flask import Flask, redirect, url_for,render_template, flash, redirect, request, abort

app = Flask(__name__)
app.config['SECRET_KEY'] = '74081e0e33c1046bd8f96bb3528e857c21b1064ad6f47f8f'

app.config.from_object('app.config')

## Connecting to database ##

def get_db_connection():
    conn = sqlite3.connect('app/database.db')
    conn.row_factory = sqlite3.Row
    return conn
## Connecting to database ends here ##

## Editing existing posts and handling non existing ID's starts here ##

def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post
## Editing existing posts and handling non existing ID's ends here ##


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/comments")
def comments():
    return render_template("comment-page.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/footer")
def footer():
    return render_template("footer.html")

@app.route("/impressum")
def impressum():
    return render_template("impressum.html")

@app.route("/legal")
def legal():
    return render_template("legal.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/navbar")
def navbar():
    return render_template("navbar.html")

@app.route("/register")
def register():
    return render_template("register.html")

## Write a post app starts here ##
@app.route("/newpost")
def new_post():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template("newpost.html", posts=posts)

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Please enter a title!')
        elif not content:
            flash('Please enter a message!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                         (title, content))
            conn.commit()
            conn.close()
            return redirect(url_for('new_post'))

    return render_template('create.html')
## Write a post app ends here ##

##Edit a post app starts here ##
@app.route('/<int:id>/edit/', methods=('GET', 'POST'))
def edit(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')

        elif not content:
            flash('Content is required!')

        else:
            conn = get_db_connection()
            conn.execute('UPDATE posts SET title = ?, content = ?'
                         ' WHERE id = ?',
                         (title, content, id))
            conn.commit()
            conn.close()
            return redirect(url_for('new_post'))

    return render_template('edit.html', post=post)
## Edit a post app ends here ##

## Deliting posts starts here ##
@app.route('/<int:id>/delete/', methods=('POST',))
def delete(id):
    post = get_post(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(post['title']))
    return redirect(url_for('new_post'))
## Deliting posts ends here ##

