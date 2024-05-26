from rest_framework.serializers import ModelSerializer
from .models import *


class MahsulotSerializer(ModelSerializer):
    class Meta:
        model = Mahsulot
        fields = "__all__"


class KatalogSerializer(ModelSerializer):
    class Meta:
        model = Katalog
        fields = '__all__'


class SubKatalogSerializer(ModelSerializer):
    class Meta:
        model = SubKatalog
        fields = '__all__'
