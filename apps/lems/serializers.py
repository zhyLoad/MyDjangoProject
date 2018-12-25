from .models import MultiCategory, MultilanguageCategory, CategoryPicture
from rest_framework import serializers


class MultiCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MultiCategory
        fields = ("parent","category_type","show_order")


class MultilanguageCategorySerializer(serializers.ModelSerializer):
     class Meta:
        model = MultilanguageCategory
        fields = "__all__"

class CategoryPictureSerializer(serializers.ModelSerializer):
     class Meta:
        model = CategoryPicture
        fields = "__all__"
