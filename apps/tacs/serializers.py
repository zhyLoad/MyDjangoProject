from information.models import Information, MultilanguageInformation, FileResource,PosterResource
from lems.models import Category, CategoryPicture, MultilanguageCategory
from rest_framework import serializers
from system_manage.models import Tenant




class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = ('pk','name')


class MultilanguageInformationSerializer(serializers.ModelSerializer):
     class Meta:
        model = MultilanguageInformation
        fields = ('pk','name','language_code','description')

class FileResourceSerializer(serializers.ModelSerializer):
     class Meta:
        model = FileResource
        fields = ('pk','name','original_name','size','resource_url')

class PosterResourceSerializer(serializers.ModelSerializer):
      class Meta:
        model = PosterResource
        fields = ('pk','name','original_name','size','resource_url','horizontal_resoution','vertical_resoution')

class InformationSerializer(serializers.ModelSerializer):
    tenant = TenantSerializer(allow_null=False)
    multi_language_informations = MultilanguageInformationSerializer(allow_null=False,many=True,read_only=True)
    file_resources = FileResourceSerializer(allow_null=True,many=True,read_only=True)
    poster_resources = PosterResourceSerializer(allow_null=True,many=True,read_only=True)

    class Meta:
        model = Information
        fields = ('pk','information_type','information_status','tenant','audit_reason','multi_language_informations',
                  'file_resources','poster_resources'
                  )
