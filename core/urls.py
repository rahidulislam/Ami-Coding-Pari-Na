from django.urls import path
from .views import HomeView,KhojView

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('khoj/', KhojView.as_view(), name='khoj')
]
