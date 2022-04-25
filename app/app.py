from flask import Flask
from . import module_blog_post, main_pages

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config')
    app.config['SECRET_KEY'] = '74081e0e33c1046bd8f96bb3528e857c21b1064ad6f47f8f'

    register_blueprints(app)

    return app

def register_blueprints(app: Flask):
    app.register_blueprint(main_pages.routes.blueprint)
    app.register_blueprint(module_blog_post.routes.blueprint)

