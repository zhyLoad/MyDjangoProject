from rest_framework import mixins
from rest_framework import viewsets
from .models import Category, MultilanguageCategory, CategoryPicture
from .serializers import CategoryAllSerializer,CategoryEditSerializer,MultilanguageCategorySerializer,CategoryPictureSerializer


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
    serializer_class = CategoryEditSerializer


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