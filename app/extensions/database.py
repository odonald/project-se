from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


migrate = Migrate()
db = SQLAlchemy()

class CRUDMixin():
    
  def save(self):
    db.session.add(self)
    db.session.commit()
    return self