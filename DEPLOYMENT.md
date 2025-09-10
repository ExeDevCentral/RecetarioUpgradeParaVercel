# 🚀 Guía de Despliegue en Vercel

## ✅ Tu proyecto está listo para Vercel!

### Archivos creados/modificados:
- ✅ `vercel.json` - Configuración de Vercel
- ✅ `wsgi.py` - Punto de entrada WSGI
- ✅ `requirements.txt` - Dependencias actualizadas (PostgreSQL)
- ✅ `app.py` - Configuración de base de datos dinámica
- ✅ `.env.example` - Variables de entorno de ejemplo
- ✅ `.gitignore` - Archivos a ignorar en Git
- ✅ `DEPLOYMENT.md` - Esta guía

## 🎯 Pasos para Desplegar:

### 1. Subir a GitHub
```bash
git add .
git commit -m "Preparar proyecto para Vercel"
git push origin main
```

### 2. Crear cuenta en Vercel
1. Ve a [vercel.com](https://vercel.com)
2. Regístrate con GitHub
3. Conecta tu repositorio

### 3. Configurar Base de Datos
1. En Vercel Dashboard → **Storage**
2. Crear nueva base de datos PostgreSQL
3. Copiar la URL de conexión

### 4. Configurar Variables de Entorno
En tu proyecto de Vercel → **Settings** → **Environment Variables**:
```
DATABASE_URL=postgresql://usuario:password@host:puerto/database
SECRET_KEY=tu_clave_secreta_muy_segura_para_produccion
FLASK_ENV=production
```

### 5. Desplegar
- Vercel detectará automáticamente los cambios
- El despliegue se realizará automáticamente

### 6. Inicializar Base de Datos
Después del despliegue, visita:
```
https://tu-app.vercel.app/init-db
```

## 🔧 Comandos Útiles

### Desarrollo Local
```bash
# Instalar dependencias
pip install -r requirements.txt

# Inicializar base de datos
python init_db.py

# Ejecutar aplicación
python app.py
```

### Vercel CLI (Opcional)
```bash
# Instalar Vercel CLI
npm i -g vercel

# Login
vercel login

# Desplegar
vercel

# Ver logs
vercel logs
```

## 🆘 Solución de Problemas

### Error de Base de Datos
- Verifica que `DATABASE_URL` esté configurada correctamente
- Asegúrate de que la base de datos PostgreSQL esté creada

### Error de Dependencias
- Verifica que `requirements.txt` tenga todas las dependencias
- Revisa los logs de Vercel para errores específicos

### Error de Variables de Entorno
- Verifica que todas las variables estén configuradas
- Asegúrate de que `SECRET_KEY` sea una cadena segura

## 📞 Soporte
- [Documentación de Vercel](https://vercel.com/docs)
- [Flask en Vercel](https://vercel.com/docs/functions/serverless-functions/runtimes/python)

## 🎉 ¡Listo!
Tu aplicación estará disponible en `https://tu-app.vercel.app`
