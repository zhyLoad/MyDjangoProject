from rest_framework import mixins
from rest_framework import viewsets
from .models import Information, MultilanguageInformation, FileResource,PosterResource
from .serializers import InformationSerializer,MultilanguageInformationSerializer,FileResourceSerializer,PosterResourceSerializer


class InformationViewset(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.CreateModelMixin,
                    viewsets.GenericViewSet):
    """
    图文的增删改查
    """
    queryset = Information.objects.all()
    serializer_class = InformationSerializer


class MultilanguageInformationViewset(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.CreateModelMixin,
                     viewsets.GenericViewSet):
    """
    图文多语言的增删改查
    """
    queryset = MultilanguageInformation.objects.all()
    serializer_class = MultilanguageInformationSerializer


class FileResourceViewset(mixins.ListModelMixin,
                          mixins.RetrieveModelMixin,
                          mixins.UpdateModelMixin,
                          mixins.DestroyModelMixin,
                          mixins.CreateModelMixin,
                          viewsets.GenericViewSet):
    """
    文件资源的增删改查
    """
    queryset = FileResource.objects.all()
    serializer_class = FileResourceSerializer

class PosterResourceViewset(mixins.ListModelMixin,
                           mixins.RetrieveModelMixin,
                           mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin,
                           mixins.CreateModelMixin,
                           viewsets.GenericViewSet):
     """
      图片资源的增删改查
     """
     queryset = PosterResource.objects.all()
     serializer_class = PosterResourceSerializer
