#!/usr/bin/env python3
"""
Script para inicializar la base de datos SQLite
Ejecutar: python init_db.py
"""

from app import app, db
from models import Categoria, Receta

def init_database():
    """Inicializa la base de datos y crea algunas categorías de ejemplo"""
    
    with app.app_context():
        # Crear todas las tablas
        db.create_all()
        print("✅ Base de datos creada exitosamente")
        
        # Verificar si ya existen categorías
        if Categoria.query.count() == 0:
            print("📝 Creando categorías de ejemplo...")
            
            # Crear categorías de ejemplo
            categorias_ejemplo = [
                Categoria(nombre="Desayunos", descripcion="Recetas para empezar el día con energía"),
                Categoria(nombre="Almuerzos", descripcion="Platos principales para el mediodía"),
                Categoria(nombre="Cenas", descripcion="Recetas ligeras para la noche"),
                Categoria(nombre="Postres", descripcion="Dulces y postres deliciosos"),
                Categoria(nombre="Bebidas", descripcion="Refrescantes bebidas y cócteles"),
                Categoria(nombre="Snacks", descripcion="Aperitivos y bocadillos"),
                Categoria(nombre="Vegetariano", descripcion="Recetas sin carne"),
                Categoria(nombre="Sin Gluten", descripcion="Recetas aptas para celíacos")
            ]
            
            for categoria in categorias_ejemplo:
                db.session.add(categoria)
            
            db.session.commit()
            print(f"✅ {len(categorias_ejemplo)} categorías creadas")
            
            # Crear algunas recetas de ejemplo
            print("🍳 Creando recetas de ejemplo...")
            
            # Receta de ejemplo en Desayunos
            desayuno_categoria = Categoria.query.filter_by(nombre="Desayunos").first()
            if desayuno_categoria:
                receta_ejemplo = Receta(
                    nombre="Pancakes Clásicos",
                    ingredientes="""• 1 taza de harina
• 2 cucharadas de azúcar
• 2 cucharaditas de polvo para hornear
• 1/2 cucharadita de sal
• 1 huevo
• 1 taza de leche
• 2 cucharadas de mantequilla derretida""",
                    instrucciones="""1. Mezcla los ingredientes secos en un bowl
2. En otro bowl, bate el huevo y añade la leche y mantequilla
3. Combina ambas mezclas hasta obtener una masa homogénea
4. Calienta una sartén a fuego medio
5. Vierte 1/4 de taza de masa por cada pancake
6. Cocina hasta que aparezcan burbujas en la superficie
7. Voltea y cocina el otro lado hasta dorar""",
                    tiempo_preparacion=20,
                    porciones=4,
                    dificultad="Fácil",
                    categoria_id=desayuno_categoria.id
                )
                db.session.add(receta_ejemplo)
            
            # Receta de ejemplo en Postres
            postres_categoria = Categoria.query.filter_by(nombre="Postres").first()
            if postres_categoria:
                receta_ejemplo2 = Receta(
                    nombre="Brownie de Chocolate",
                    ingredientes="""• 200g de chocolate negro
• 150g de mantequilla
• 200g de azúcar
• 3 huevos
• 100g de harina
• 1 cucharadita de esencia de vainilla""",
                    instrucciones="""1. Precalienta el horno a 180°C
2. Derrite el chocolate y la mantequilla al baño maría
3. Mezcla el azúcar con los huevos hasta que estén espumosos
4. Añade el chocolate derretido y la vainilla
5. Incorpora la harina tamizada
6. Vierte en un molde engrasado
7. Hornea por 25-30 minutos""",
                    tiempo_preparacion=45,
                    porciones=8,
                    dificultad="Medio",
                    categoria_id=postres_categoria.id
                )
                db.session.add(receta_ejemplo2)
            
            db.session.commit()
            print("✅ Recetas de ejemplo creadas")
        
        else:
            print("ℹ️  La base de datos ya contiene datos")
        
        # Mostrar estadísticas
        total_categorias = Categoria.query.count()
        total_recetas = Receta.query.count()
        print(f"\n📊 Estadísticas de la base de datos:")
        print(f"   • Categorías: {total_categorias}")
        print(f"   • Recetas: {total_recetas}")
        
        # Mostrar categorías
        print(f"\n📁 Categorías disponibles:")
        for categoria in Categoria.query.all():
            recetas_count = len(categoria.recetas)
            print(f"   • {categoria.nombre} ({recetas_count} recetas)")

if __name__ == "__main__":
    init_database()

