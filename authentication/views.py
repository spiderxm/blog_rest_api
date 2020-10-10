from rest_framework import viewsets
# Create your views here.
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from .serializers import UserSerializer
from .models import User
from .permissions import UserPermissions


class ManageUsers(viewsets.ModelViewSet):
    """Manage users create, list, delete, update"""
    authentication_classes = [TokenAuthentication,]
    serializer_class = UserSerializer
    permission_classes = [UserPermissions, ]
    queryset = User.objects.all()


class Login(ObtainAuthToken):
    """
    Handle Login of users
    """
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
