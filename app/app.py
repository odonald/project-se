from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

app.config.from_object('app.config')

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


