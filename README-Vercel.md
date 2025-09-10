# 🍳 Recetario Web - Listo para Vercel

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/ExeDevCentral/RecetarioUpgradeParaVercel)

Una aplicación web moderna para gestionar y organizar recetas de cocina, **optimizada específicamente para despliegue en Vercel**.

## ✨ Características

- **📁 Gestión de Categorías**: Organiza tus recetas por tipo de comida
- **📖 CRUD de Recetas**: Crear, leer, actualizar y eliminar recetas
- **🎨 Interfaz Moderna**: Diseño responsive con Bootstrap 5
- **🔍 Búsqueda Avanzada**: Encuentra recetas rápidamente
- **📱 Responsive**: Funciona perfectamente en móviles y tablets
- **⚡ API REST**: Endpoint para integración con otras aplicaciones
- **🚀 Optimizado para Vercel**: Configuración lista para producción

## 🚀 Despliegue en Vercel (1 Click)

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/ExeDevCentral/RecetarioUpgradeParaVercel)

### Pasos Rápidos:

1. **Haz clic en el botón "Deploy with Vercel"** arriba
2. **Conecta tu cuenta de GitHub**
3. **Importa el repositorio**
4. **Configura las variables de entorno** (ver abajo)
5. **¡Despliega!**

## 🔧 Configuración de Variables de Entorno

En tu proyecto de Vercel, ve a **Settings** → **Environment Variables** y agrega:

```
DATABASE_URL=postgresql://usuario:password@host:puerto/database
SECRET_KEY=tu_clave_secreta_muy_segura_para_produccion
FLASK_ENV=production
```

### 📊 Configurar Base de Datos PostgreSQL

1. En Vercel Dashboard → **Storage**
2. Crear nueva base de datos PostgreSQL
3. Copiar la URL de conexión
4. Agregarla como `DATABASE_URL`

## 🎯 Inicializar Base de Datos

Después del despliegue, visita:
```
https://tu-app.vercel.app/init-db
```

## 🛠️ Tecnologías

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Framework CSS**: Bootstrap 5
- **Base de Datos**: PostgreSQL (Vercel)
- **Hosting**: Vercel
- **Iconos**: Font Awesome 6

## 📁 Estructura del Proyecto

```
RecetarioWeb-Vercel/
├── app.py                 # Aplicación Flask optimizada
├── wsgi.py               # Punto de entrada WSGI
├── vercel.json           # Configuración de Vercel
├── requirements.txt      # Dependencias con PostgreSQL
├── models.py             # Modelos de base de datos
├── init_db.py           # Script de inicialización
├── .env.example         # Variables de entorno
├── .gitignore           # Archivos a ignorar
├── templates/           # Plantillas HTML
└── static/              # CSS y JavaScript
```

## 🎨 Capturas de Pantalla

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

## 🔧 Desarrollo Local

```bash
# Clonar repositorio
git clone https://github.com/ExeDevCentral/RecetarioUpgradeParaVercel.git
cd RecetarioUpgradeParaVercel

# Instalar dependencias
pip install -r requirements.txt

# Inicializar base de datos
python init_db.py

# Ejecutar aplicación
python app.py
```

## 📱 Demo en Vivo

[Ver Demo](https://tu-app.vercel.app) - *Actualiza con tu URL de Vercel*

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
- [Vercel](https://vercel.com/) - Hosting gratuito
- [Python](https://www.python.org/) - Lenguaje de programación

---

⭐ Si te gusta este proyecto, ¡dale una estrella en GitHub!

## 🚀 Despliegue Alternativo

### Railway
[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/your-template)

### Render
[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)
