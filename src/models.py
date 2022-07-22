from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

detalles_personajes = db.Table('favorite_personaje',
    db.Column('users_id', db.Integer, db.ForeignKey('Users.id'),primary_key=True),
    db.Column('personajes_id', db.Integer, db.ForeignKey('Personajes.id', primary_key=True))
    )
detalles_planetas = db.Table('favorite_planeta',
    db.Column('users_id', db.Integer, db.ForeignKey('Users.id'), primary_key=True),
    db.Column('planetas_id', db.Integer, db.ForeignKey('Planetas.id'), primary_key=True)
    )
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    name = db.Column(db.String(250), nullable=False)
    last_name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250))

    def __repr__(self):
        return '<Users %r>' % self.username
    def serialize(self):
        return{
            "id":self.id,
            "username":self.username,
            "name":self.name,
            "last_name":self.last_name,
            "email":self.email
        }


class Planetas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
  
    def __repr__(self):
        return '<Planetas %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "name":self.name

            
          
        }
class Personajes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
  
    def __repr__(self):
        return '<Personajes %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "name":self.name
            
           
        }
