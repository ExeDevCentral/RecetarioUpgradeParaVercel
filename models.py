from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Categoria(db.Model):
    """Modelo para las categorías de recetas"""
    __tablename__ = 'categorias'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False, unique=True)
    descripcion = db.Column(db.Text, nullable=True)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relación con recetas
    recetas = db.relationship('Receta', backref='categoria', lazy=True, cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Categoria {self.nombre}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'descripcion': self.descripcion,
            'fecha_creacion': self.fecha_creacion.isoformat(),
            'recetas_count': len(self.recetas)
        }

class Receta(db.Model):
    """Modelo para las recetas"""
    __tablename__ = 'recetas'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(200), nullable=False)
    ingredientes = db.Column(db.Text, nullable=False)
    instrucciones = db.Column(db.Text, nullable=False)
    tiempo_preparacion = db.Column(db.Integer, nullable=True)  # en minutos
    porciones = db.Column(db.Integer, nullable=True)
    dificultad = db.Column(db.String(20), nullable=True)  # Fácil, Medio, Difícil
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
    fecha_modificacion = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Clave foránea
    categoria_id = db.Column(db.Integer, db.ForeignKey('categorias.id'), nullable=False)
    
    def __repr__(self):
        return f'<Receta {self.nombre}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'ingredientes': self.ingredientes,
            'instrucciones': self.instrucciones,
            'tiempo_preparacion': self.tiempo_preparacion,
            'porciones': self.porciones,
            'dificultad': self.dificultad,
            'fecha_creacion': self.fecha_creacion.isoformat(),
            'fecha_modificacion': self.fecha_modificacion.isoformat(),
            'categoria_id': self.categoria_id,
            'categoria_nombre': self.categoria.nombre if self.categoria else None
        }

