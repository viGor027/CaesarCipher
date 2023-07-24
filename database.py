from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(50), nullable=False)
    shift = db.Column(db.Integer)

    def __repr__(self):
        return '<Task %r>' % self.id
