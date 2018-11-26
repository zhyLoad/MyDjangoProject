
from .models import Information, MultilanguageInformation, FileResource,PosterResource
from rest_framework import serializers


class InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = "__all__"

class MultilanguageInformationSerializer(serializers.ModelSerializer):
     class Meta:
        model = MultilanguageInformation
        fields = "__all__"

class FileResourceSerializer(serializers.ModelSerializer):
     class Meta:
        model = FileResource
        fields = "__all__"

class PosterResourceSerializer(serializers.ModelSerializer):
      class Meta:
        model = PosterResource
        fields = "__all__"