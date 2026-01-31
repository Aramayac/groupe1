from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(80), nullable=False)
    prenom = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    nationalite = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f"<User {self.nom} {self.prenom}>"
