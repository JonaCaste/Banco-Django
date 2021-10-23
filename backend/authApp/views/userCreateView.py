from rest_framework                         import status, views
from rest_framework.response                import Response
from rest_framework_simplejwt.serializers   import TokenObtainPairSerializer
from authApp.serializers.userSerializer     import UserSerializer


class UserCreateView(views.APIView):         #hace las veces de controlador
                                             #por eso API
    def post(self, request, *args, **kwargs):
                                #* = recibe una lista(parametros = algo) de parametros que guarda en una lista
                                #** = recibe una lista(parametros "suelto") de parametros que guarda en un dic
        serializer = UserSerializer(data=request.data)   #creamos un objeto serializar con la peticion que llega
        serializer.is_valid(raise_exception=True)        #los tipos de datos y todo lo que haya que validar, el lo valida
                                                         #si falla lanza una escepcion por el raise_exceotion=True
        serializer.save()                     #guarda en la db, termina llamando al create de userSerializer


        #devolvemos los tokens
        token_data = {
            'username' : request.data['username'],
            'password' : request.data['password']
        }

        token_serializer = TokenObtainPairSerializer(data=token_data)  #genera un par de tokens
        token_serializer.is_valid(raise_exception=True)                #valida que el token este bien
        return Response(token_serializer.validated_data, status=status.HTTP_201_CREATED)   
                                    #respuesta http con la data validada y el estatus