from django.urls import path
from .views import RegisterView, LoginView, LogoutView

urlpatterns = [
    path('signup/', RegisterView.as_view(), name='api-signup'),
    path('login/', LoginView.as_view(), name='api-login'),
    path('logout/', LogoutView.as_view(), name='api-logout'),
]
