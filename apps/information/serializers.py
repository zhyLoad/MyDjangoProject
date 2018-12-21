from .models import Information, MultilanguageInformation, FileResource,PosterResource
from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
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

class InformationSerializer(WritableNestedModelSerializer):
    tenant = TenantSerializer(allow_null=False)
    multi_language_informations = MultilanguageInformationSerializer(allow_null=False,many=True)
    file_resources = FileResourceSerializer(allow_null=True,many=True)
    poster_resources = PosterResourceSerializer(allow_null=True,many=True)

    class Meta:
        model = Information
        fields = ('pk','information_type','information_status','tenant','audit_reason','multi_language_informations',
                  'file_resources','poster_resources'
                  )

    def create(self, validated_data):
        input_tenant = validated_data.pop('tenant')
        tenant = Tenant.objects.filter(name=input_tenant.name)
        information = Information.objects.create(tenant=tenant,**validated_data)
        multi_languages_data = validated_data.pop('multi_language_informations')
        for multi_language_data in multi_languages_data:
            MultilanguageInformation.objects.create(information=information,**multi_language_data)

        file_resources_data = validated_data.pop('file_resources')
        for file_resource_data in file_resources_data:
            FileResource.objects.create(information=information, **file_resource_data)

        poster_resources_data = validated_data.pop('poster_resources')
        for poster_resource_data in poster_resources_data:
            MultilanguageInformation.objects.create(information=information, **poster_resource_data)

        return information


# {
#     "information_type": 1,
#     "information_status": 1,
#     "tenant": {
#         "name": "张三"
#     },
#     "audit_reason": "大法师的法师的法师地方",
#     "multi_language_informations": [{
#         "name": "张三0001",
#       "language_code": "chi",
#       "description": "dafadfasdfa"
#     },{        "name": "张三0002",
#       "language_code": "chi",
#       "description": "dafdasdfas大发发达"
#     }]
# }