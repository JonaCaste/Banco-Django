from django.contrib import admin

from .models.user import User
from .models.account import Account
from .models.transaction import Transaction
from .models.deposit     import Deposit

admin.site.register(User)  #crea una "vista" donde podemos observar esa tabla(como tableplus), no ejecuta querys
admin.site.register(Account)
admin.site.register(Transaction)
admin.site.register(Deposit)