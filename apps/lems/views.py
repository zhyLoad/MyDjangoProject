from rest_framework import mixins
from rest_framework import viewsets
from .models import MultiCategory, MultilanguageCategory, CategoryPicture
from .serializers import MultiCategorySerializer,MultilanguageCategorySerializer,CategoryPictureSerializer


class MultiCategoryViewset(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.CreateModelMixin,
                    viewsets.GenericViewSet):
    """
    目录的增删改查
    """
    queryset = MultiCategory.objects.all()
    serializer_class = MultiCategorySerializer


class MultilanguageCategoryViewset(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.CreateModelMixin,
                     viewsets.GenericViewSet):
    """
    目录多语言的增删改查
    """
    queryset = MultilanguageCategory.objects.all()
    serializer_class = MultilanguageCategorySerializer


class CategoryPictureViewset(mixins.ListModelMixin,
                          mixins.RetrieveModelMixin,
                          mixins.UpdateModelMixin,
                          mixins.DestroyModelMixin,
                          mixins.CreateModelMixin,
                          viewsets.GenericViewSet):
    """
    目录图片的增删改查
    """
    queryset = CategoryPicture.objects.all()
    serializer_class = CategoryPictureSerializer