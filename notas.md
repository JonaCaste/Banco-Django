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

## simpleJWT
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
importamos 
* `models` desde `django.db`
* `AbstractBaseUser` desde `django.contrib.auth.models`   
* `PermissionsMixin` desde `django.contrib.auth.models`   
* `BaseUserManager` desde `django.contrib.auth.models`    => gestinar ususarios
* `make_password` desde `django.contrib.auth.hashers`     => encriptar la clave