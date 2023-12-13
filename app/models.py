from . import db
from datetime import datetime

class Usuario(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    nombre=db.Column(db.String(100))
    apellido=db.Column(db.String(100))
    email=db.Column(db.String(100))

class Sueno (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    texto_sueno = db.Column(db.Text, nullable=False)
    fecha_hora = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    # Relación con la clase Usuario (asume que tienes una clase Usuario definida)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    usuario = db.relationship('Usuario', backref=db.backref('suenos', lazy=True))

    def __repr__(self):
        return f"<Sueno {self.id}>"