from django.conf                                import settings
from rest_framework                             import generics, status
                                                #generics son clases genericas, con funcionalidades directas para
                                                #cada operacion del CRUD
from rest_framework.response                    import Response
from rest_framework.permissions                 import IsAuthenticated
from rest_framework_simplejwt.backends          import TokenBackend

from authApp.models.transaction                 import Transaction
from authApp.serializers.transactionSerializer  import TransactionSerializer


# leer GET

##devuelve las transacciondes de una cuenta
class TransactionsAccountView(generics.ListAPIView):
                                        #ListAPIView -> permite hacer busquedas filtradas
                                        #y retorna lista de registro que corresponda con el criterio de busqueda
    serializer_class    = TransactionSerializer
    permission_classes  = (IsAuthenticated,)

    def get_queryset(self):
        print("Request: ", self.request)
        print("Args: ", self.args)
        print("KWargs: ", self.kwargs)
        token = self.request.META.get('HTTP_AUTHORIZATION')[7:]  #trae de los metadatos el "header autorization", a partir el dato 7 nos interesa
        token_backend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])     #valida el token que se genera, con el algoritmo configurado en settings/simplejwt
        valid_data = token_backend.decode(token, verify=False)                      #verifica el token que recibimos y lo compara con el tokens decodificados con el algoritmo
        
        if valid_data['user_id'] != self.kwargs['user']:    #user_id es el id guardado por defecto por el token
                                                            #user = usuario con permiso en ese token
            string_response = {'detail' : 'Acceso no autorizado'}
            return Response(string_response, status=status.HTTP_401_UNAUTHORIZED)

        queryset = Transaction.objects.filter(origin_account_id=self.kwargs['account'])
                                        #filter = where
        return queryset


## devuelve una sola transaccion
class TransactionsDetailView(generics.RetrieveAPIView):
    serializer_class    = TransactionSerializer
    permission_classes  = (IsAuthenticated,)
    queryset = Transaction.objects.all() 

    def get(self, request, *args, **kwargs):
        print("Request: ", request)
        print("Args: ", args)
        print("KWargs: ", kwargs)
        token = self.request.META.get('HTTP_AUTHORIZATION')[7:]  #trae de los metadatos el "header autorization", a partir el dato 7 nos interesa
        token_backend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])     #valida el token que se genera, con el algoritmo configurado en settings/simplejwt
        valid_data = token_backend.decode(token, verify=False)                      #verifica el token que recibimos y lo compara con el tokens decodificados con el algoritmo
        
        if valid_data['user_id'] != kwargs['user']:    #user_id es el id guardado por defecto por el token
                                                            #user = usuario con permiso en ese token
            string_response = {'detail' : 'Acceso no autorizado'}
            return Response(string_response, status=status.HTTP_401_UNAUTHORIZED)

        return super().get(request, *args, **kwargs)



# crear POST
class TransactionsCreateView(generics.CreateAPIView):
    serializer_class    = TransactionSerializer
    permission_classes  = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        print("Request: ", request)
        print("Args: ", args)
        print("KWargs: ", kwargs)
        token = self.request.META.get('HTTP_AUTHORIZATION')[7:]  #trae de los metadatos el "header autorization", a partir el dato 7 nos interesa
        token_backend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])     #valida el token que se genera, con el algoritmo configurado en settings/simplejwt
        valid_data = token_backend.decode(token, verify=False)                      #verifica el token que recibimos y lo compara con el tokens decodificados con el algoritmo
        
        if valid_data['user_id'] != request.data['user_id']:    #user_id es el id guardado por defecto por el token
                                                            #user = usuario con permiso en ese token
            string_response = {'detail' : 'Acceso no autorizado'}
            return Response(string_response, status=status.HTTP_401_UNAUTHORIZED)

        serializer = TransactionSerializer(data=request.data['transaction_data'])
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response("Transacción exitosa", status=status.HTTP_201_CREATED)


# actualizar UPDATE
class TransactionsUpdateView(generics.UpdateAPIView):
    serializer_class    = TransactionSerializer
    permission_classes  = (IsAuthenticated,)
    queryset = Transaction.objects.all() 

    def get(self, request, *args, **kwargs):
        print("Request: ", request)
        print("Args: ", args)
        print("KWargs: ", kwargs)
        token = self.request.META.get('HTTP_AUTHORIZATION')[7:]  #trae de los metadatos el "header autorization", a partir el dato 7 nos interesa
        token_backend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])     #valida el token que se genera, con el algoritmo configurado en settings/simplejwt
        valid_data = token_backend.decode(token, verify=False)                      #verifica el token que recibimos y lo compara con el tokens decodificados con el algoritmo
        
        if valid_data['user_id'] != kwargs['user']:    #user_id es el id guardado por defecto por el token
                                                            #user = usuario con permiso en ese token
            string_response = {'detail' : 'Acceso no autorizado'}
            return Response(string_response, status=status.HTTP_401_UNAUTHORIZED)

        return super().update(request, *args, **kwargs)



#borrar DELETE
class TransactionsDeleteView(generics.DestroyAPIView):
    serializer_class    = TransactionSerializer
    permission_classes  = (IsAuthenticated,)
    queryset = Transaction.objects.all() 

    def get(self, request, *args, **kwargs):
        print("Request: ", request)
        print("Args: ", args)
        print("KWargs: ", kwargs)
        token = self.request.META.get('HTTP_AUTHORIZATION')[7:]  #trae de los metadatos el "header autorization", a partir el dato 7 nos interesa
        token_backend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])     #valida el token que se genera, con el algoritmo configurado en settings/simplejwt
        valid_data = token_backend.decode(token, verify=False)                      #verifica el token que recibimos y lo compara con el tokens decodificados con el algoritmo
        
        if valid_data['user_id'] != kwargs['user']:    #user_id es el id guardado por defecto por el token
                                                            #user = usuario con permiso en ese token
            string_response = {'detail' : 'Acceso no autorizado'}
            return Response(string_response, status=status.HTTP_401_UNAUTHORIZED)

        return super().destroy(request, *args, **kwargs)