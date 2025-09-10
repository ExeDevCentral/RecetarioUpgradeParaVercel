from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
from pathlib import Path
import json
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'tu_clave_secreta_aqui')

# Configuración de la base de datos
if os.environ.get('DATABASE_URL'):
    # Producción (Vercel con PostgreSQL)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
else:
    # Desarrollo local (SQLite)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recetario.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Importar modelos después de configurar la app
from models import db, Categoria, Receta
db.init_app(app)

def contar_recetas():
    """Cuenta el total de recetas en todas las categorías"""
    return Receta.query.count()

def obtener_categorias():
    """Obtiene todas las categorías disponibles"""
    categorias_db = Categoria.query.all()
    categorias = []
    for categoria in categorias_db:
        categorias.append({
            'id': categoria.id,
            'nombre': categoria.nombre,
            'descripcion': categoria.descripcion,
            'recetas_count': len(categoria.recetas)
        })
    return categorias

def obtener_recetas(categoria_id):
    """Obtiene todas las recetas de una categoría"""
    categoria = Categoria.query.get_or_404(categoria_id)
    recetas = []
    for receta in categoria.recetas:
        recetas.append({
            'id': receta.id,
            'nombre': receta.nombre,
            'ingredientes': receta.ingredientes,
            'instrucciones': receta.instrucciones,
            'tiempo_preparacion': receta.tiempo_preparacion,
            'porciones': receta.porciones,
            'dificultad': receta.dificultad,
            'fecha_creacion': receta.fecha_creacion,
            'fecha_modificacion': receta.fecha_modificacion
        })
    return recetas

@app.route('/')
def index():
    """Página principal"""
    categorias = obtener_categorias()
    total_recetas = contar_recetas()
    return render_template('index.html', categorias=categorias, total_recetas=total_recetas)

@app.route('/categoria/<int:categoria_id>')
def ver_categoria(categoria_id):
    """Muestra las recetas de una categoría específica"""
    categoria = Categoria.query.get_or_404(categoria_id)
    recetas = obtener_recetas(categoria_id)
    return render_template('categoria.html', categoria=categoria, recetas=recetas)

@app.route('/receta/<int:receta_id>')
def ver_receta(receta_id):
    """Muestra una receta específica"""
    receta = Receta.query.get_or_404(receta_id)
    return render_template('receta.html', receta=receta)

@app.route('/crear_categoria', methods=['GET', 'POST'])
def crear_categoria():
    """Crea una nueva categoría"""
    if request.method == 'POST':
        nombre_categoria = request.form['nombre_categoria']
        descripcion = request.form.get('descripcion', '')
        
        if not nombre_categoria:
            flash('El nombre de la categoría es requerido', 'error')
            return render_template('crear_categoria.html')
        
        # Verificar si la categoría ya existe
        if Categoria.query.filter_by(nombre=nombre_categoria).first():
            flash('La categoría ya existe', 'error')
            return render_template('crear_categoria.html')
        
        nueva_categoria = Categoria(nombre=nombre_categoria, descripcion=descripcion)
        db.session.add(nueva_categoria)
        db.session.commit()
        
        flash(f'Categoría "{nombre_categoria}" creada exitosamente', 'success')
        return redirect(url_for('index'))
    
    return render_template('crear_categoria.html')

@app.route('/crear_receta', methods=['GET', 'POST'])
def crear_receta():
    """Crea una nueva receta"""
    if request.method == 'POST':
        categoria_id = request.form['categoria_id']
        nombre_receta = request.form['nombre_receta']
        ingredientes = request.form['ingredientes']
        instrucciones = request.form['instrucciones']
        tiempo_preparacion = request.form.get('tiempo_preparacion', type=int)
        porciones = request.form.get('porciones', type=int)
        dificultad = request.form.get('dificultad', '')
        
        if not all([categoria_id, nombre_receta, ingredientes, instrucciones]):
            flash('Los campos nombre, ingredientes e instrucciones son requeridos', 'error')
            return render_template('crear_receta.html', categorias=Categoria.query.all())
        
        # Verificar si la receta ya existe en esta categoría
        categoria = Categoria.query.get_or_404(categoria_id)
        if Receta.query.filter_by(nombre=nombre_receta, categoria_id=categoria_id).first():
            flash('La receta ya existe en esta categoría', 'error')
            return render_template('crear_receta.html', categorias=Categoria.query.all())
        
        nueva_receta = Receta(
            nombre=nombre_receta,
            ingredientes=ingredientes,
            instrucciones=instrucciones,
            tiempo_preparacion=tiempo_preparacion,
            porciones=porciones,
            dificultad=dificultad,
            categoria_id=categoria_id
        )
        
        db.session.add(nueva_receta)
        db.session.commit()
        
        flash(f'Receta "{nombre_receta}" creada exitosamente', 'success')
        return redirect(url_for('ver_categoria', categoria_id=categoria_id))
    
    return render_template('crear_receta.html', categorias=Categoria.query.all())

@app.route('/editar_receta/<int:receta_id>', methods=['GET', 'POST'])
def editar_receta(receta_id):
    """Edita una receta existente"""
    receta = Receta.query.get_or_404(receta_id)
    
    if request.method == 'POST':
        receta.nombre = request.form['nombre_receta']
        receta.ingredientes = request.form['ingredientes']
        receta.instrucciones = request.form['instrucciones']
        receta.tiempo_preparacion = request.form.get('tiempo_preparacion', type=int)
        receta.porciones = request.form.get('porciones', type=int)
        receta.dificultad = request.form.get('dificultad', '')
        
        db.session.commit()
        flash('Receta actualizada exitosamente', 'success')
        return redirect(url_for('ver_receta', receta_id=receta_id))
    
    return render_template('editar_receta.html', receta=receta)

@app.route('/eliminar_receta/<int:receta_id>', methods=['POST'])
def eliminar_receta(receta_id):
    """Elimina una receta"""
    receta = Receta.query.get_or_404(receta_id)
    categoria_id = receta.categoria_id
    nombre_receta = receta.nombre
    
    db.session.delete(receta)
    db.session.commit()
    
    flash(f'Receta "{nombre_receta}" eliminada exitosamente', 'success')
    return redirect(url_for('ver_categoria', categoria_id=categoria_id))

@app.route('/eliminar_categoria/<int:categoria_id>', methods=['POST'])
def eliminar_categoria(categoria_id):
    """Elimina una categoría"""
    categoria = Categoria.query.get_or_404(categoria_id)
    
    # Verificar si la categoría tiene recetas
    if categoria.recetas:
        flash('No se puede eliminar una categoría que contiene recetas', 'error')
    else:
        db.session.delete(categoria)
        db.session.commit()
        flash(f'Categoría "{categoria.nombre}" eliminada exitosamente', 'success')
    
    return redirect(url_for('index'))

@app.route('/api/recetas')
def api_recetas():
    """API endpoint para obtener todas las recetas"""
    recetas = Receta.query.all()
    return jsonify([receta.to_dict() for receta in recetas])

@app.route('/api/categorias')
def api_categorias():
    """API endpoint para obtener todas las categorías"""
    categorias = Categoria.query.all()
    return jsonify([categoria.to_dict() for categoria in categorias])

@app.route('/init-db')
def init_db_endpoint():
    """Endpoint temporal para inicializar la base de datos en producción"""
    if os.environ.get('FLASK_ENV') == 'production':
        try:
            from init_db import init_database
            init_database()
            return jsonify({"message": "Base de datos inicializada exitosamente"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    return jsonify({"message": "Este endpoint solo está disponible en producción"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)

