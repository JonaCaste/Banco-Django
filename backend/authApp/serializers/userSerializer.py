from authApp.models.user    import User
from authApp.models.account import Account            #como el user tiene asociado account, se importa
from rest_framework         import serializers
from .accountSerializer     import AccountSerializer  #se importa el serializar ya creado


class UserSerializer(serializers.ModelSerializer):

    account = AccountSerializer()

    class Meta:                #metadata
        model = User
        fields = ['id', 'username', 'password', 'name', 'email', 'account']
                                #serializamos todos los datos, ya que utilizamos todos en las peticiones,
                                #adicionalmente traemos los datos de account


    #deserializar, creamos objetos basado en el modelo
    def create(self, validate_data):                            # es un "controlador" entre vista y serializer, crea user
        accountData = validate_data.pop('account')              # pop del diccionario account(info de la cuenta)
        userInstance = User.objects.create(**validate_data)     # instanciamos el objeto user(sin account)
        Account.objects.create(user=userInstance, **accountData)  # instanciamos el objeto account
                                                                                    #(asociamos un user al account con la llave foranea de user)
        return userInstance


    #serializar, creamos json
    def to_representation(self, obj):       # como queremos ver el objeto
                                            # equivalente al to_String de java

        user = User.objects.get(id = obj.id)          #guarde en user el usuario que pertenece a ese id
        account = Account.objects.get(user = obj.id)  #guarde en account todas las cuentas que pertenecen a esa llave foranea
                                                        #equivalente al select where id

        return {                                     #lo que retornamos en el servicio web (formato json)
            "id" : user.id,
            "username" : user.username,
            "name" : user.name,
            "email" : user.email,
            "account" :{
                "id" : account.id,
                "balance" : account.balance,
                "lastChangeDate" : account.lastChangeDate,
                "isActivate" : account.isActivate
            }
        }