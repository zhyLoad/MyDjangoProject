from rest_framework import mixins
from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer

class UserViewset(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet):
    """
    图文的增删改查
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

