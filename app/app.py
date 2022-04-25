import sqlite3
from flask import Flask, redirect, url_for,render_template, flash, redirect, request, abort
from . import module_blog_post



app = Flask(__name__)

app.config.from_object('app.config')

## I'm not sure if the key should be in this file, but I tried moving it to the "module_blog_post" wich broke the code ## 

app.config['SECRET_KEY'] = '74081e0e33c1046bd8f96bb3528e857c21b1064ad6f47f8f'


app.register_blueprint(module_blog_post.routes.blueprint)



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