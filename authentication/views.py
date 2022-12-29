from rest_framework import viewsets, filters, views, status, generics
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authtoken.models import Token
from rest_framework.settings import api_settings

from .models import *
from .serializers import *

class LoginApiView(ObtainAuthToken):
    """Crea tokens de autenticacion de usuario"""
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        
        img_user = ''
        
        if user.profile_img != None:
            img_user = token.user.profile_img.url
        return Response(
            {
            'id':user.id,
            'token': token.key,
            'name': token.user.name,
            'email': token.user.email,
            'img': img_user,
            'message':'Sucessful login',
            },
            status= status.HTTP_201_CREATED)

    renderer_classes= api_settings.DEFAULT_RENDERER_CLASSES
    
class RegisterCreateApiView(generics.CreateAPIView):
    """APIView para los registros de usuarios"""
    serializer_class = RegisterSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.create(serializer.validated_data)
        
        # message = f'Hola { name }'
        # send_mail(f'Bienvenido { name }',
        # 'Creacion de cuenta exitosa',None,
        # [email])
        print(serializer.validated_data)
        
        img_user = ''
        
        if user.profile_img != None:
            img_user = user.profile_img.url
        
        token, created = Token.objects.get_or_create(user=user)
        headers = self.get_success_headers(serializer.data)
        return Response({'token': token.key, 'name':user.name,'email':user.email, 'img': img_user}, status=status.HTTP_201_CREATED, headers=headers)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
