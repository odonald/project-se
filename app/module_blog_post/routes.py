import sqlite3
from flask import Blueprint, redirect, url_for,render_template, flash, redirect, request, abort
from flask_login import login_required

blueprint = Blueprint('module_blog_post', __name__)


## Connecting to database ##

def get_db_connection():
    conn = sqlite3.connect('app/database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post
## Connecting to database ends here ##

## Write a post app starts here ##
@blueprint.route("/newpost")
@login_required
def newpost():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template("/module_blog_post/index.html", posts=posts)

@blueprint.route('/create', methods=('GET', 'POST'))
@login_required
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
            return redirect(url_for('module_blog_post.newpost'))

    return render_template('module_blog_post/create.html')


## Write a post app ends here ##

##Edit a post app starts here ##
@blueprint.route('/<int:id>/edit/', methods=('GET', 'POST'))
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
            return redirect(url_for('module_blog_post.newpost'))

    return render_template('module_blog_post/edit.html', post=post)
## Edit a post app ends here ##

## Deleteing posts starts here ##
@blueprint.route('/<int:id>/delete/', methods=('POST',))
def delete(id):
    post = get_post(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(post['title']))
    return redirect(url_for('module_blog_post.newpost'))
## Deleteing posts ends here ##