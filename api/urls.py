from django.urls import path
from .views import KhojTheSearchAPI
app_name = 'api'

urlpatterns = [
    path('', KhojTheSearchAPI.as_view(), name='all')
]
