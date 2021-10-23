from authApp.models.account import Account
from rest_framework         import serializers


class AccountSerializer(serializers.ModelSerializer):

    class Meta:            #metadata "generalizacion de la clase"
        model = Account
        fields = ['balance', 'lastChangeDate', 'isActivate']        
                            #datos a serializar
                            #las llaves foraneas e id`s autogenerados no se suelen añadir, 
                            #por que es info que no "utilizamos"(en peticiones), 
                            #ya que es info sensible