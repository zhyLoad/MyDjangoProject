from .serializers import AddressesSerializer
from .models import Addresses
from rest_framework import mixins
from rest_framework import viewsets

class AddressesViewset( mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.CreateModelMixin,
                     viewsets.GenericViewSet):
    """
    地址的增删改查
    """
    queryset = Addresses.objects.all()
    serializer_class = AddressesSerializer