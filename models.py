from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime, func

db = SQLAlchemy()


class Adv(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(300), nullable=False)
    owner = db.Column(db.String(50), nullable=False)
    date_of_creation = db.Column(DateTime, server_default=func.now(), nullable=False)

    def __repr__(self):
        return (f"Adv(title='{self.title}', description='{self.description}', owner='{self.owner}',"
                f" date_of_creation='{self.date_of_creation}'")
