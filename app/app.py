from flask import Flask
from . import module_blog_post, main_pages, users
from app.extensions.database import db, migrate
from app.extensions.authentication import login_manager

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config')
    login_manager.login_view = "users.get_login"

    
    
    register_extensions(app)
    register_blueprints(app)

    return app

def register_blueprints(app: Flask):
    app.register_blueprint(main_pages.routes.blueprint)
    app.register_blueprint(module_blog_post.routes.blueprint)
    app.register_blueprint(users.routes.blueprint)
    login_manager.init_app(app)



def register_extensions(app: Flask):
      db.init_app(app)
      migrate.init_app(app, db)


