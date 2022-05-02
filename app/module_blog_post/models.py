from app.extensions.database import db, CRUDMixin
from flask_login import UserMixin

class Postobject(db.Model, CRUDMixin, UserMixin):
  id = db.Column(db.Integer, primary_key = True)
  title = db.Column(db.String,)
  content = db.Column(db.String)
  #created = ???
