from django.urls import path, include
from .views import *

urlpatterns = [
    path('', MahsulotApiView.as_view())
]
