from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.generics import *
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .serializers import *


class MahsulotApiView(APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='katalog',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description="Katalog bo'yicha filterlash"
            ),
            openapi.Parameter(
                name='subKatalog',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description="SubKatalog bo'yicha filterlash"
            ),
            openapi.Parameter(
                name='brend',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description="Brend bo'yicha filterlash"
            ),
            openapi.Parameter(
                name='min_narx',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                description="Min narx bo'yicha filterlash"
            ),
            openapi.Parameter(
                name='max_narx',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                description="Max narx bo'yicha filterlash"
            ),

        ]
    )
    def get(self, request):

        mahsulotlar = Mahsulot.objects.all()
        katalog = request.query_params.get('katalog', None)
        if katalog is not None:
            katalog = get_object_or_404(Katalog, id=int(katalog))
            mahsulotlar = mahsulotlar.filter(SubKatalog__katalog=katalog)

        subKatalog = request.query_params.get('subKatalog', None)
        if subKatalog is not None:
            subKatalog = get_object_or_404(SubKatalog, id=subKatalog)
            mahsulotlar = mahsulotlar.filter(subKatalog=subKatalog)

        brend = request.query_params.get('brend', None)
        if brend is not None:
            mahsulotlar = mahsulotlar.filter(brend__icontains=brend)

        min_narx = request.query_params.get('min_narx', None)
        if min_narx is not None:
            mahsulotlar = mahsulotlar.filter(narx__gte=min_narx)

        max_narx = request.query_params.get('max_narx', None)
        if max_narx is not None:
            mahsulotlar = mahsulotlar.filter(narx__lte=max_narx)

        serializer = MahsulotSerializer(mahsulotlar, many=True)
        return Response(serializer.data)


class KatalogApiView(APIView):
    def get(self, request):
        katalog = Katalog.objects.all()
        serizlizer = KatalogSerializer(katalog, many=True)
        return Response(serizlizer.data)


class SubKatalogApiView(APIView):
    def get(self, request):
        subkatalog = SubKatalog.objects.all()
        katalog_id = request.query_params.get('katalog', None)
        if katalog_id is not None:
            subkatalog = subkatalog.filter(katalog_id=katalog_id)
        serializer = SubKatalogSerializer(subkatalog, many=True)
        return Response(serializer.data)
