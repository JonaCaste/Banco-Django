from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager   #gestion de usuarios y tablas (ORM)
from django.contrib.auth.hashers import make_password                                        #encriptar contraseña

#manager
class UserManager(BaseUserManager):           #es equivalente a un dao

    def create_user(self, username, password=None):
        if not username:
            raise ValueError('el usuario no cuenta con un username')
        
        user = self.model(username=username)   #crea un modelo y asigna username a la var username
        user.set_password(password)            #le agrega el password al modelo
        user.save(using=self._db)              #guarde el modelo utilizando la db por defecto(la db configurada en el settings.py)

        return user

    def create_superuser(self, username_, password_):
        user = self.create_user(
            username = username_,
            password = password_
        )
        user.is_admin = True
        user.save(using=self._db)

        return user


#modelo
class User(AbstractBaseUser, PermissionsMixin):

    id = models.BigAutoField(primary_key=True)     #id autoincremental super seguro(aporx 64 caracteres)
    username = models.CharField('Username', max_length=20, unique=True)    #tipo de dato(nombre dentro de la tabla)
    password = models.CharField('Password', max_length=256)
    name = models.CharField('Nombre', max_length=50)
    email = models.EmailField('Email', max_length=100)

    def save(self, **kwargs):                   #** = recibe una lista(los parametros que lleguen) de parametros que guarda en un dic
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'    #basado en este texto se cifra la contraseña original
        self.password = make_password(self.password, some_salt)

        super().save(**kwargs)                  #super clase

    objects = UserManager()
    USERNAME_FIELD = 'username'                 #campo de logeo para iniciar sesion