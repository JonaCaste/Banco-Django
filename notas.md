# Bases de datos

## creamos archivo con las credenciales
evitamos tener las credenciales "publicas"
añadimos este archivo al .gitignore
este archivo se crea directamente en la app desplegada

## eliminamos db por defecto
eliminamos db.sqlite3


# Backend

## crear entorno virtual
`py -m venv env`

### salir de entorno virtual
`deactivate env`

### el entorno virtual no se despliega ni se agrega al env
agregar env a .gitignore

## permisos para instalar cosas
`cd env`
`Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process`

## activamos el entorno virtual
`Scripts/activate`  
Verificar que estemos en el entorno -> Sale (env) al principio de las lineas en la consola

## instalar django (libreria)
`cd ..`
`pip install django`
`pip install djangorestframework`

## crear proyecto django
`django-admin startproject authProject`
sacar los archivos de la carpeta, dejarlos en el nivel de backend

## agregar libreria a las config del proyecto -> authModule/settings.py/INSTALLED_APPS
'rest_framework',            # incluir el django-framework al proyecto

## crear aplicacion django
`django-admin startapp authApp`
sacar los archivos de la carpeta, dejarlos en el nivel de backend

## agregar app a las config del proyecto -> authModule/settings.py/INSTALLED_APPS
'authApp',            # incluir la app al proyecto

## ejecutar el server
`python manage.py runserver`

## creamos requirements
creamos `requirements.txt` en la raiz del backend
se agregan todas las librerias de python para ejecutar el proyecto
es lo equivalente a pip install ...

* `pip install -r requirements.txt` instalamos todas las libreiras
* `pip freeze` muestra las librerias instaladas

## config de simpleJWT
creamos la variable(diccionario) `REST_FRAMEWORK` en `backend/authProject/settings.py`

* `'DEFAULT_PERMISSION_CLASSES'` => permisos de acceso
    * `'rest_framework.permission.AllowAny'` => internamente todass las clases tienen acceso

* `'DEFAULT_AUTHENTICATION_CLASSES'` => autenticacion de las clases
    * `'rest_framework_simplejwt.authentication.JWTAuthentication'` => realizar las autenticaciones por medio de JWT

## config tiempos de los tokens
importamos timedelta desde datetime en `backend/authProject/settings.py`
creamos la variable(diccionario) `SIMPLE_JWT` en `backend/authProject/settings.py`

* `'ACCESS_TOKEN_LIFETIME'`     => tiempo de vida del access token
* `'REFRESH_TOKEN_LIFETIME'`    => tiempo de vida del refresh token
* `ROTATE_REFRESH_TOKENS`       => rotacion de los refresh tokens
* `BLACKLIST_AFTER_ROTATION`    => despues de hacer la rotacion, no reutilizar el token
* `ALGORITHM`                   => algoritmo de codificacion
    * `'HS256'`                 => algoritmo estandar (vieja comfiable)

## config de base de datos
modificamos la variable `DATABASES` en `backend/authProject/settings.py`
* `'ENGINE': 'django.db.backends.postgresql_psycopg2'` => base de datos + conector de python
* Demás variables => credenciales de base de datos
    * `'NAME'` = base de datos

## models y views
como no vamos a utilizar las vistas ni modelos tradicionales de django
se elimina de `backend/authApp`
* `models.py`
* `views.py`

ahora creamos una carpeta para las vistas y modelos
creamos carpetas en `backend/authApp`
* `models`
* `views`
* `serializers`
agregar el `__init__.py`

## models
creamos un archivo por cada tabla
* en los modelos que se necesiten validacion se crea clase manager, se utiliza como "Dao"
* se crean modelos equivalentes a las tablas de la db

importamos los modelos desde el `__init__.py`

## admin
importamos los modelos `User` y `Account` a `backend/authApp/admin.py`
dejamos la posibilidad de agregar los modelos al administrador por defecto de Django

## config de autenticacion
creamos la variable(diccionario) `AUTH_USER_MODEL` en `backend/authProject/settings.py`

* `'authApp.User'` => autenticacion sobre el ususario

## migracion
conectamos con la db, se crean tablas por defectos y de los modelos(si no existen)
ejecutamos:
* `python manage.py makemigrations authApp` => obtiene los modelos de la App y los agrega al modelo de datos global del proyecto
* `python manage.py migrate` => migramos los modelos a la db

## serializers
creamos un serializer por cada modelo en `backend/authApp/serializers/`
* importamos el modelo
* importamos los serializers

creamos los serializers a partir de los modelos

importamos en el `__init__.py`

### self
metodos en python llevan self
funcion = static
metodo = funcion de clase no estatica

## views
creamos las vistas que necesitemos en la carpeta `backend/authApp/views/`

importamos los modelos desde el `__init__.py`

## urls
agregamos los urls en `backend/authProject/urls.py`
importamos todas las vistas
enrutamos los links a cada vista

## creamos crud (transaccion)
creamos el modelo `transaction.py` a `backend/authApp/models/`
volvemos a hacer la migracion: 
* `python manage.py makemigrations authApp`
* `python manage.py migrate`
creamos el serializer `transactionSerializer.py` en `backend/authApp/serializers/`
creamos el view `transactionView.py` en `backend/authApp/views`

agregamos los endpoints a `backend/authProject/urls.py`
agregar los archivos a sus resoectivos `__init__.py`

# despliegue

## crear settings de produccion
crear una copia de `backend/authProject/settings.py`

cambiar las configuraciones para desplegar en `backend/authProject/settings_prod.py`

cambiar las cofiguraciones de inicio del proyecto en `backend/manage.py` a `settings_prod`

cambiar las cofiguraciones de inicio del proyecto en `backend/authProject/wsgi.py` a `settings_prod`
* en caso de utilizar otra db para produccion, volver a migrar los modelos

## pre config del despliegue en heroku
creamos una nueva app en heroku

agregar nuevas librerias a el `backend/requirements.txt`
* gunicorn -> se inicia con el server, corre como proceso que se ejecuta todo el tiempo en la maquina
* django-heroku -> conectar django con heroku

importar `django-heroku` en `backend/authProject/settings_prod.py`
agregar `django_heroku.settings(locals())` en `backend/authProject/settings_prod.py`
* `django_heroku.settings(locals())` -> basar el despliegue en las configs locales

crear `Procfile` en `backend`
* `web: gunicorn authProject.wsgi` -> servicio web: con settings del wsgi

agregar los archivos al `.gitignore` que no necesitamos subir(desde github se crea por defecto)

## despliegue en heroku
* salir del entorno virtual

despliegue desde el CLI de heroku
`heroku login`
* dejar la pestaña del nav abierta

`git init`
* si no se ha iniciado un repo (del backend)

`heroku git:remote -a banco-django-be`
* con el nombre de la app en heroku

`git add .`
* desde la carpeta backend

`git commit -am "Deploy first version"`
* -am -> el commit tiene una flag mas

`git push heroku master`

### genera conflicto si ya existe un repo en github
crear una rama master
subir desde master

`git checkout -b master`
* si no existe

`git checkout master`
* si existe

`git pull origin main`
* tener todo en el main actualizado

`git add .`

`git commit -am "Deploy first version"`

`git push heroku master`

### o

desplegar directamente desde github

### eliminar la db creada por defecto dentro de la app backend en heroku

## se agregaron validaciones al post de las transacciones
## se agrego toda la parte de deposito

## config de CORS
agregamos `django-cors-headers` en `backend/requirements.txt`

se agrega `corsheaders` a `backend/authProject/settings.py` y `settings_prod.py` en `INSTALLED_APPS`

se agrega `corsheaders.middleware.CorsMiddleware` a `backend/authProject/settings.py` y `settings_prod.py` en `MIDDLEWARE`

creamos la variable `CORS_ALLOWED_ORIGINS` en `backend/authProject/settings.py` y `settings_prod.py`
agregamos la URL que poede hacer peticiones CORS a nuestro backend, o True (para cualquier URL)


# Frontend

## instalar node y vue

instalamos node js en el computador
instalamos vue por medio de `npm global add @vue/cli`

iniciamos un proyecto vue con  `vue create ...` (nombre)
seleccionamos `manually select features` y seleccionamos:
* `choose Vue version`
* `Babel`
* `Router`
seleccionamos la versión `3.x`
Requires proper server setup for index fallback in production -> seleccionamos `n` (no)
seleccionamos `package.json` para la config del proyecto
Save this as a preset for future projects? (guardar plantilla para otros proyectos)-> seleccionamos `n` (no)

## iniciar servidor 
`npm run serve`

## router
movemos el archivo `frontend/src/router/index.js` a `frontend/src/`
lo renombramos a `router.js`

## arranque
cambiamos el componente `Home` a `App` en `frontend/src/router.js`
importar `App` en router

eliminamos las otras rutas, ya que se manejaran las rutas directamente desde `App.vue`

## config inicial
en el archivo `frontend/src/main.js` encontramos la config incial del proyecto

## componentes
eliminamos los archivos iniciales de `frontend/src/components/`

y creamos :
* `SignUp.vue`
* `Login.vue`
lo importamos en `frontend/src/router.js`

agregamos los redirecionamientos en `frontend/src/router.js`

## construimos la app
creamos un nav en `frontend/src/App.vue`

## instalamos axios
`npm install axios`

## modificamos el componente LogIn
en `frontend/src/components/Login.vue`