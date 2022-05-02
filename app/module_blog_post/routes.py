from app.extensions.database import db
from flask import Blueprint, redirect, url_for,render_template, flash, redirect, request, abort
from flask_login import login_required
from app.module_blog_post.models import Postobject

blueprint = Blueprint('module_blog_post', __name__)



@blueprint.route("/newpost")
@login_required
def newpost():
    posts = Postobject.query.all()
    return render_template("/module_blog_post/index.html", posts=posts)

@blueprint.get('/create')
@login_required
def get_create():
    return render_template('module_blog_post/create.html')


@blueprint.post('/create')
@login_required
def post_create():
    try:
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Please enter a title!')
        elif not content:
            flash('Please enter a message!')

        postobject = Postobject(
            title=request.form.get('title'),
            content=request.form.get('content'),
        )
        postobject.save()
        return redirect(url_for('module_blog_post.newpost'))

    except Exception as error_message:
        error = error_message or 'An error occurred while creating a user. Please make sure to enter valid data.'
        return render_template('users/register.html', error=error)


## Write a post app ends here ##

##Edit a post app starts here ##
@blueprint.get('/<int:id>/edit/')
@login_required
def get_edit(id):
    posts = Postobject.query.get(id)
    return render_template('module_blog_post/edit.html', post=posts)

@blueprint.post('/<int:id>/edit/')
@login_required
def post_edit(id):
    try:
        posts = Postobject.query.get(id)
        posts.title = request.form['title']
        posts.content = request.form['content']
        db.session.commit()
        return redirect(url_for('module_blog_post.newpost'))

    except Exception as error_message:
        error = error_message or 'An error occurred while creating a user. Please make sure to enter valid data.'
        return render_template('module_blog_post/edit.html', error=error)    

## Edit a post app ends here ##

## Deleteing posts starts here ##
@blueprint.post('/<int:id>/delete/')
@login_required
def delete(id):
    post = Postobject.query.get(id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('module_blog_post.newpost'))
## Deleteing posts ends here ##