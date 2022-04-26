from flask import Blueprint, render_template, redirect, url_for, send_file

blueprint = Blueprint('main_pages', __name__)


@blueprint.route("/")
def home():
    return render_template("main_pages/index.html")

@blueprint.route("/comments")
def comments():
    return render_template("main_pages/comment-page.html")

@blueprint.route("/contact")
def contact():
    return render_template("main_pages/contact.html")

@blueprint.route("/footer")
def footer():
    return render_template("main_pages/footer.html")

@blueprint.route("/impressum")
def impressum():
    return render_template("main_pages/impressum.html")

@blueprint.route("/legal")
def legal():
    return render_template("main_pages/legal.html")

@blueprint.route("/navbar")
def navbar():
    return render_template("main_pages/navbar.html")

