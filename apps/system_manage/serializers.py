
from .models import Tenant, Manager, Organization
from rest_framework import serializers


class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = "__all__"

class ManagerSerializer(serializers.ModelSerializer):
     class Meta:
        model = Manager
        fields = "__all__"

class OrganizationSerializer(serializers.ModelSerializer):
     class Meta:
        model = Organization
        fields = "__all__"