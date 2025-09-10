# 🍳 Mi Recetario - Web App

Una aplicación web moderna para gestionar y organizar recetas de cocina, desarrollada con Flask y Bootstrap.

## ✨ Características

- **📁 Gestión de Categorías**: Organiza tus recetas por tipo de comida
- **📖 CRUD de Recetas**: Crear, leer, actualizar y eliminar recetas
- **🎨 Interfaz Moderna**: Diseño responsive con Bootstrap 5
- **🔍 Búsqueda Avanzada**: Encuentra recetas rápidamente
- **📱 Responsive**: Funciona perfectamente en móviles y tablets
- **⚡ API REST**: Endpoint para integración con otras aplicaciones

## 🚀 Instalación y Uso

### Prerrequisitos

- Python 3.7 o superior
- pip (gestor de paquetes de Python)

### Instalación

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/ExeDevCentral/Recetario.git
   cd Recetario
   ```

2. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecuta la aplicación:**
   ```bash
   python app.py
   ```

4. **Abre tu navegador:**
   ```
   http://localhost:5000
   ```

## 📁 Estructura del Proyecto

```
Recetario/
├── app.py                 # Aplicación principal Flask
├── requirements.txt       # Dependencias de Python
├── README.md             # Este archivo
├── templates/            # Plantillas HTML
│   ├── base.html         # Plantilla base
│   ├── index.html        # Página principal
│   ├── categoria.html    # Vista de categoría
│   ├── receta.html       # Vista de receta
│   ├── crear_categoria.html
│   ├── crear_receta.html
│   └── editar_receta.html
└── static/               # Archivos estáticos
    ├── css/
    │   └── style.css     # Estilos personalizados
    └── js/
        └── main.js       # JavaScript personalizado
```

## 🎯 Funcionalidades

### Gestión de Categorías
- Crear nuevas categorías (ej: Desayunos, Postres, Bebidas)
- Ver todas las categorías con contador de recetas
- Eliminar categorías vacías

### Gestión de Recetas
- Crear recetas con ingredientes e instrucciones
- Editar recetas existentes
- Eliminar recetas
- Ver recetas organizadas por categoría

### Características Adicionales
- **Búsqueda**: Busca recetas por nombre o contenido
- **Responsive**: Adaptable a cualquier dispositivo
- **Notificaciones**: Mensajes de éxito y error
- **API REST**: Endpoint `/api/recetas` para obtener todas las recetas

## 🛠️ Tecnologías Utilizadas

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Framework CSS**: Bootstrap 5
- **Iconos**: Font Awesome 6
- **Almacenamiento**: Sistema de archivos local

## 📱 Capturas de Pantalla

### Página Principal
- Vista de todas las categorías
- Contador de recetas totales
- Acciones rápidas

### Vista de Categoría
- Lista de recetas por categoría
- Acciones de edición y eliminación

### Vista de Receta
- Contenido completo de la receta
- Opciones de edición y eliminación

## 🔧 Configuración

### Variables de Entorno
La aplicación usa la siguiente configuración por defecto:
- **Puerto**: 5000
- **Host**: 0.0.0.0 (accesible desde cualquier IP)
- **Modo Debug**: Activado en desarrollo

### Almacenamiento de Datos
Las recetas se almacenan en archivos de texto en:
```
~/Recetas/
├── Categoria1/
│   ├── receta1.txt
│   └── receta2.txt
└── Categoria2/
    └── receta3.txt
```

## 🚀 Despliegue

### Desarrollo Local
```bash
# Instalar dependencias
pip install -r requirements.txt

# Inicializar base de datos
python init_db.py

# Ejecutar aplicación
python app.py
```

### 🌐 Despliegue en Vercel (GRATIS)

Vercel es una excelente opción gratuita para hostear tu aplicación Flask. Aquí te guiamos paso a paso:

#### 1. Preparación del Proyecto
Tu proyecto ya está configurado para Vercel con los siguientes archivos:
- ✅ `vercel.json` - Configuración de Vercel
- ✅ `wsgi.py` - Punto de entrada WSGI
- ✅ `requirements.txt` - Dependencias actualizadas
- ✅ Configuración de base de datos PostgreSQL

#### 2. Crear Cuenta en Vercel
1. Ve a [vercel.com](https://vercel.com)
2. Regístrate con GitHub (recomendado)
3. Conecta tu repositorio

#### 3. Configurar Base de Datos PostgreSQL
Vercel ofrece PostgreSQL gratuito:

1. En tu dashboard de Vercel, ve a **Storage**
2. Crea una nueva base de datos PostgreSQL
3. Copia la URL de conexión (DATABASE_URL)

#### 4. Configurar Variables de Entorno
En tu proyecto de Vercel:
1. Ve a **Settings** → **Environment Variables**
2. Agrega estas variables:
   ```
   DATABASE_URL=postgresql://usuario:password@host:puerto/database
   SECRET_KEY=tu_clave_secreta_muy_segura_para_produccion
   FLASK_ENV=production
   ```

#### 5. Desplegar
1. Haz push de tu código a GitHub
2. Vercel detectará automáticamente los cambios
3. El despliegue se realizará automáticamente

#### 6. Inicializar Base de Datos en Producción
Después del primer despliegue, necesitas inicializar la base de datos:

**Opción A: Usando Vercel CLI**
```bash
# Instalar Vercel CLI
npm i -g vercel

# Login
vercel login

# Desplegar
vercel

# Ejecutar script de inicialización
vercel env pull .env.local
python init_db.py
```

**Opción B: Crear endpoint de inicialización**
Agrega esta ruta temporal a `app.py`:
```python
@app.route('/init-db')
def init_db_endpoint():
    if os.environ.get('FLASK_ENV') == 'production':
        init_database()
        return "Base de datos inicializada"
    return "No disponible en desarrollo"
```

#### 7. Dominio Personalizado (Opcional)
- En Vercel, ve a **Settings** → **Domains**
- Agrega tu dominio personalizado
- Configura los DNS según las instrucciones

### 🔧 Otros Servicios de Hosting Gratuitos

#### Railway
- **URL**: [railway.app](https://railway.app)
- **Ventajas**: PostgreSQL incluido, fácil configuración
- **Límite**: 500 horas/mes gratis

#### Render
- **URL**: [render.com](https://render.com)
- **Ventajas**: PostgreSQL gratuito, SSL automático
- **Límite**: 750 horas/mes gratis

#### Heroku (Alternativa)
- **URL**: [heroku.com](https://heroku.com)
- **Nota**: Ya no es completamente gratuito, pero tiene plan básico económico

### 📊 Comparación de Servicios Gratuitos

| Servicio | Base de Datos | SSL | Dominio | Límite Mensual |
|----------|---------------|-----|---------|----------------|
| **Vercel** | ✅ PostgreSQL | ✅ | ✅ | Ilimitado |
| Railway | ✅ PostgreSQL | ✅ | ✅ | 500h |
| Render | ✅ PostgreSQL | ✅ | ✅ | 750h |
| Heroku | ❌ (Pago) | ✅ | ✅ | Pago |

### 🎯 Recomendación
**Vercel es la mejor opción** para tu proyecto porque:
- ✅ Completamente gratuito
- ✅ PostgreSQL incluido
- ✅ SSL automático
- ✅ Dominio personalizado
- ✅ Despliegue automático desde GitHub
- ✅ Excelente rendimiento

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si quieres mejorar el proyecto:

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -am 'Añadir nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 👨‍💻 Autor

**ExeDevCentral**
- GitHub: [@ExeDevCentral](https://github.com/ExeDevCentral)

## 🙏 Agradecimientos

- [Flask](https://flask.palletsprojects.com/) - Framework web
- [Bootstrap](https://getbootstrap.com/) - Framework CSS
- [Font Awesome](https://fontawesome.com/) - Iconos
- [Python](https://www.python.org/) - Lenguaje de programación

---

⭐ Si te gusta este proyecto, ¡dale una estrella en GitHub!

