from django.db import models
from .user import User

class Account(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='account', on_delete=models.CASCADE)
                            #llave a la que apunta, nombre de la relacion, modelo del on_delete
    balance = models.IntegerField(default = 0)
    lastChangeDate = models.DateTimeField()
    isActivate = models.BooleanField(default=True)