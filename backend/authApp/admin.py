from django.contrib import admin

from .models.user import User
from .models.account import Account

admin.site.register(User)  #crea una "vista" donde podemos observar esa tabla(como tableplus), no ejecuta querys
admin.site.register(Account)