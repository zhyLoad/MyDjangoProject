from rest_framework import mixins
from rest_framework import viewsets
from .models import *

# Create your views here.


class KitchenSinkViewset( mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.CreateModelMixin,
                     viewsets.GenericViewSet):
       """
       厨房的增删改查
       """
       queryset = KitchenSink.objects.all()



class CategoryViewset(mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
        """
        目录的增删改查
        """
        queryset = Category.objects.all()



class CityViewset(mixins.ListModelMixin,
                             mixins.RetrieveModelMixin,
                             mixins.UpdateModelMixin,
                             mixins.DestroyModelMixin,
                             mixins.CreateModelMixin,
                             viewsets.GenericViewSet):
        """
        城市的增删改查
        """
        queryset = City.objects.all()
