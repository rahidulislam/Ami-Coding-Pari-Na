from django.urls import path
from .views import LogOutView, SignUpView,LoginView
app_name = 'accounts'

urlpatterns = [
    path('sign_up/', SignUpView.as_view(), name='sign-up'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogOutView.as_view(), name='logout')
]
