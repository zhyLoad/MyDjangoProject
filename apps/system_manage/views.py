from rest_framework import mixins
from rest_framework import viewsets
from .models import Tenant, Manager, Organization
from .serializers import TenantSerializer,ManagerSerializer,OrganizationSerializer

# Create your views here.


class TenantViewset( mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.CreateModelMixin,
                     viewsets.GenericViewSet):
       """
       租户的增删改查
       """
       queryset = Tenant.objects.all()
       serializer_class = TenantSerializer



class ManagerViewset(mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
        """
        管理员的增删改查
        """
        queryset = Manager.objects.all()
        serializer_class = ManagerSerializer



class OrganizationViewset(mixins.ListModelMixin,
                             mixins.RetrieveModelMixin,
                             mixins.UpdateModelMixin,
                             mixins.DestroyModelMixin,
                             mixins.CreateModelMixin,
                             viewsets.GenericViewSet):
        """
        组织机构的增删改查
        """
        queryset = Organization.objects.all()
        serializer_class = OrganizationSerializer