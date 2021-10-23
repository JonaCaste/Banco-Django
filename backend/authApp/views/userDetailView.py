from django.conf                        import settings
from rest_framework                     import generics, status
                                                #generics son clases genericas, con funcionalidades directas para
                                                #cada operacion del CRUD
from rest_framework.response            import Response
from rest_framework.permissions         import IsAuthenticated
from rest_framework_simplejwt.backends  import TokenBackend

from authApp.models.user                import User
from authApp.serializers.userSerializer import UserSerializer


class UserDetailView(generics.RetrieveAPIView):    #visualizacion de un solo elemento de la coleccion
    queryset = User.objects.all()                  #por defecto, trae todos los elemento de la tabla
    serializer_class = UserSerializer              #clase que serializa
    permission_classes = (IsAuthenticated,)        #permisos que manejamos(tupla) - sade del settings

    def get(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]  #trae de los metadatos el "header autorization", a partir el dato 7 nos interesa
        token_backend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])     #valida el token que se genera, con el algoritmo configurado en settings/simplejwt
        valid_data = token_backend.decode(token, verify=False)                      #verifica el token que recibimos y lo compara con el tokens decodificados con el algoritmo

        if valid_data['user_id'] != kwargs['pk']:    #user_id es el id guardado por defecto por el token
                                                     #pk = usuario con permiso en ese token
            string_response = {'detail' : 'Acceso no autorizado'}
            return Response(string_response, status=status.HTTP_401_UNAUTHORIZED)

        return super().get(request, *args, **kwargs)  #devuelve el registro con los argumentos que recibimos
                                                      #hacemos un get gracias al generics