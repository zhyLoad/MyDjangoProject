from .models import Category, MultilanguageCategory, CategoryPicture
from rest_framework import serializers


class CategoryAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class CategoryEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("parent_id","category_type","show_order")


class MultilanguageCategorySerializer(serializers.ModelSerializer):
     class Meta:
        model = MultilanguageCategory
        fields = "__all__"

class CategoryPictureSerializer(serializers.ModelSerializer):
     class Meta:
        model = CategoryPicture
        fields = "__all__"
