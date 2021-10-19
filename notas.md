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