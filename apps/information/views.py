from rest_framework import mixins
from rest_framework import viewsets
from .models import Information
from .serializers import InformationSerializer


class InformationViewset(
                    mixins.ListModelMixin,
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

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


